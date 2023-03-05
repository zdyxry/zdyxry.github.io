---
title: Flask 流式响应
date: 2018-07-08 09:44:24
tags:
- Flask
- Python
---


## 背景
在 web 场景下，经常会碰到下载文件的需求，通常小文件我们会采用 Flask `send_file` 或者 `send_from_directory`的方式，下载，但是当下载的文件是一个大压缩文件（>1GiB）时，这种方式就显得不友好了，我们需要采用流式下载的方式返回给客户端。

## 流式下载
简单实现：
```python
from flask import Response

@app.route("/download/<file_path>", methods=["GET"])
def download(file_path):
    def generate():
        if not os.path.exists(file_path):
            raise "File not found."
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(chunk_size=10 * 1024 * 1024)
                if not chunk:
                    break
                yield chunk

    return Response(generate(), content_type="application/octet-stream")
```   

运行 Flask app，可以正确下载文件，但是下载只有实时速度，没有文件总大小，导致无法知道下载进度，也没有文件类型，这些我们都可以通过增加 header 字段实现：
```python
response = Response(generate(), mimetype='application/gzip')
response.headers['Content-Disposition'] = 'attachment; filename={}.tar.gz'.format("download_file")
response.headers['content-length'] = os.stat(str(file_path)).st_size
return response
```

这样，我们下载文件就可以看到文件类型、文件总大小及已下载大小了，其中 `mimetype` 根据实际压缩文件类型修改匹配即可。

---

## 转发流式下载
当我们下载本地节点文件，可以通过上述方法实现，但是如果我们的产品是集群形式的，要求在集群中的任一节点均可下载集群中所有节点的指定文件，我们就需要支持将流式下载转发并实时下载，避免访问节点占用太多内存。

如果是单节点转发流式请求，我们可以通过 flask 的 `stream_with_context` 实现：
```python
from flask import (
    Flask,
    Response,
    stream_with_context
    )
import requests

app = Flask(__name__)

@app.route("/download/<file_path>", method=["GET"])
def download(file_path):
    url_prefix = "http://1.1.1.1/"
    remote_url = url_prefix + file_path
    req = requests.get(remote_url, stream = True)
    return Response(stream_with_context(req.iter_content()), 
                    content_type = req.headers['content-type'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

在我们访问 `http://localhost:5000/download/file_name`  时，通过 requests 访问远端节点 1.1.1.1 的地址，并将请求通过流式的方式转发至客户端，实现下载。

如果是转发多节点流式请求，我们该如何保证多个请求最终 merge 后是一个正确的文件呢？ 
通过查询资料，排除了标准库中的 tarfile 和 zipfile 打包压缩方式，最终采用 zipstream（https://github.com/allanlei/python-zipstream） 第三方库实现。

---

zipstream 支持通过迭代器的方式写入文件，并可实时压缩读取，官方示例如下：
```python
def iterable():
    for _ in xrange(10):
        yield b'this is a byte string\x01\n'

z = zipstream.ZipFile()
z.write_iter('my_archive_iter', iterable())

with open('zipfile.zip', 'wb') as f:
    for data in z:
        f.write(data)
```

---

根据上述特性，我们结合转发单节点请求，实现同时请求多节点并实时压缩下载：

```python
@app.route("/cluster_download/<file_path>", method=["GET"])
def cluster_download(reqs):
    def generate(req):
        z = zipstream.ZipFile(mode="w", compression=zipstream.ZIP_DEFLATED)
        for req in reqs:
            host = req.raw._fp.fp._sock.getpeername()[0]
            z.write_iter("%s.tar.gz" % host, req.iter_content(chunk_size=10 * 1024 * 1024)
        for chunk in z:
            yield chunk

    def get_file_size(reqs):
        size = 0
        for req in reqs:
            size += int(req.headers.get("content-length"))
        return size

    remote_hosts = ["1.1.1.1", "2.2.2.2"]
    reqs = []
    for host in remote_hosts:
        req = requests.get("http://%s/%s" % (host, file_path), timeout=5, stream=True)
        if req.status_code == 200:
            reqs.append(req)
    response = Response(generate(reqs))
    response.headers['mimetype'] = 'application/zip'
    response.headers['Content-Disposition'] = 'attachment; filename=cluster_logs.zip)
    response.hreads['content-length'] = get_file_size(reqs)
    
```

当我们访问 `http://localhost/cluster_download/file_name` 时，会先去 remote_hosts 中各个节点下载该文件，并通过 `write_iter` 的方式写入到 zip 文件中，Flask Response 返回的是 zip 文件中的数据块。

---

如果我们要在 zip 文件中增加某些运行过程中产生的数据，我们可以通过再定义一个生成器的方式：
```python
def generate_file(content):
    yield content

z.write_iter("running_status", generate_file)
```

这样我们就可以在最终的 zip 文件中，包含一个名为 `running_status` 的文件，文件内容为 content 的内容。


## 总结
这个需求在日常使用中是很常见的，跟下载类似，上传文件的话我们也可以采用类似的方式实现。


