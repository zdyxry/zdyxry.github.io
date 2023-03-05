---
title: Python socket 编程
date: 2018-09-30 20:33:00
tags:
- Python
- Socket
---

## 背景

平时工作很少涉及到 Socket 相关，基本上都是 HTTP 之上的业务，最近看到 [Real Python](https://realpython.com/python-sockets/) 的一篇博客，非常详细的讲解了 Python 下的 socket 编程，其中有两个示例觉得很好，帮助我理解了一些要点，记录一下。

## 多连接情况

### Server

multiconn-server.py
```python
#!/usr/bin/env python3

import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept()  # 前提条件：可读状态
    print('accepted connection from', addr)
    conn.setblocking(False)     # 置为非阻塞
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)  # 注册事件到 select

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  #  前提条件：可读状态
        if recv_data:
            data.outb += recv_data    # 保存数据
        else:
            print('closing connection to', data.addr) # 如果没有接受到数据，则需关闭该 socket 连接
            sel.unregister(sock) # 将该 socket 事件从 select 删除
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)  #前提条件：可写状态
            data.outb = data.outb[sent:] # 在数据发送完后， 将其删除

if len(sys.argv) != 3:
    print('usage:', sys.argv[0], '<host> <port>')
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print('listening on', (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:    
            if key.data is None:         # 如果没有传输数据，则该请求为连接请求
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)  # 处理数据
except KeyboardInterrupt:
    print('caught keyboard interrupt, exiting')
finally:
    sel.close()
```

### Client

multiconn-client.py
```python
#!/usr/bin/env python3

import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()
messages = [b'Message 1 from client.', b'Message 2 from client.']

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print('starting connection', connid, 'to', server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(connid=connid,
                                     msg_total=sum(len(m) for m in messages),
                                     recv_total=0,
                                     messages=list(messages),
                                     outb=b'')
        sel.register(sock, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # 前提条件：可读状态
        if recv_data:
            print('received', repr(recv_data), 'from connection', data.connid)
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print('closing connection', data.connid)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0) # 如果没有可发送数据，则取 messages 中的第一条用户发送请求
        if data.outb:
            print('sending', repr(data.outb), 'to connection', data.connid)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

if len(sys.argv) != 4:
    print('usage:', sys.argv[0], '<host> <port> <num_connections>')
    sys.exit(1)

host, port, num_conns = sys.argv[1:4]
start_connections(host, int(port), int(num_conns))

try:
    while True:
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print('caught keyboard interrupt, exiting')
finally:
    sel.close()
```

## 协议封装处理

在多连接基础上，增加特殊协议处理，比如 json header 、 protocol header 等。

### Server

libserver.py
```python
import sys
import selectors
import json
import io
import struct

request_search = {
    'morpheus': 'Follow the white rabbit. \U0001f430',
    'ring': 'In the caves beneath the Misty Mountains. \U0001f48d',
    '\U0001f436': '\U0001f43e Playing ball! \U0001f3d0',
}

class Message:

    def __init__(self, selector, sock, addr):
        self.selector = selector
        self.sock = sock
        self.addr = addr
        self._recv_buffer = b''
        self._send_buffer = b''
        self._jsonheader_len = None
        self.jsonheader = None
        self.request = None
        self.response_created = False

    def _set_selector_events_mask(self, mode):
        """Set selector to listen for events: mode is 'r', 'w', or 'rw'."""
        if mode == 'r':
            events = selectors.EVENT_READ
        elif mode == 'w':
            events = selectors.EVENT_WRITE
        elif mode == 'rw':
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
        else:
            raise ValueError(f'Invalid events mask mode {repr(mode)}.')
        self.selector.modify(self.sock, events, data=self)

    def _read(self):
        try:
            # Should be ready to read
            data = self.sock.recv(4096)
        except BlockingIOError:
            # Resource temporarily unavailable (errno EWOULDBLOCK)
            pass
        else:
            if data:
                self._recv_buffer += data
            else:
                raise RuntimeError('Peer closed.')

    def _write(self):
        if self._send_buffer:
            print('sending', repr(self._send_buffer), 'to', self.addr)
            try:
                # Should be ready to write
                sent = self.sock.send(self._send_buffer)
            except BlockingIOError:
                # Resource temporarily unavailable (errno EWOULDBLOCK)
                pass
            else:
                self._send_buffer = self._send_buffer[sent:]
                # Close when the buffer is drained. The response has been sent.
                if sent and not self._send_buffer:
                    self.close()

    # JSON 编码、解码
    def _json_encode(self, obj, encoding):
        return json.dumps(obj, ensure_ascii=False).encode(encoding)

    def _json_decode(self, json_bytes, encoding):
        tiow = io.TextIOWrapper(io.BytesIO(json_bytes), encoding=encoding,
                                newline='')
        obj = json.load(tiow)
        tiow.close()
        return obj

    def _create_message(self, *, content_bytes, content_type,
                        content_encoding):
        jsonheader = {
            'byteorder': sys.byteorder,
            'content-type': content_type,
            'content-encoding': content_encoding,
            'content-length': len(content_bytes)
        }
        jsonheader_bytes = self._json_encode(jsonheader, 'utf-8')
        message_hdr = struct.pack('>H', len(jsonheader_bytes))
        message = message_hdr + jsonheader_bytes + content_bytes # 生成编码后信息
        return message

    def _create_response_json_content(self):
        action = self.request.get('action')
        if action == 'search':  # 根据客户端发送请求返回相应响应信息
            query = self.request.get('value')
            answer = request_search.get(query) or f'No match for "{query}".'
            content = {'result': answer}
        else:
            content = {'result': f'Error: invalid action "{action}".'}
        content_encoding = 'utf-8'
        response = {
            'content_bytes': self._json_encode(content, content_encoding),
            'content_type': 'text/json',
            'content_encoding': content_encoding
        }
        return response

    def _create_response_binary_content(self): # 如果为 binary，则直接返回
        response = {
            'content_bytes': b'First 10 bytes of request: ' +
                             self.request[:10],
            'content_type': 'binary/custom-server-binary-type',
            'content_encoding': 'binary'
        }
        return response

    def process_events(self, mask):
        if mask & selectors.EVENT_READ:
            self.read()
        if mask & selectors.EVENT_WRITE:
            self.write()

    def read(self):
        self._read()

        if self._jsonheader_len is None:
            self.process_protoheader()

        if self._jsonheader_len is not None:
            if self.jsonheader is None:
                self.process_jsonheader()

        if self.jsonheader:
            if self.request is None:
                self.process_request()

    def write(self):
        if self.request:
            if not self.response_created:
                self.create_response()

        self._write()

    def close(self):
        print('closing connection to', self.addr)
        try:
            self.selector.unregister(self.sock)
        except Exception as e:
            print(f'error: selector.unregister() exception for',
                  f'{self.addr}: {repr(e)}')

        try:
            self.sock.close()
        except OSError as e:
            print(f'error: socket.close() exception for',
                  f'{self.addr}: {repr(e)}')
        finally:
            # Delete reference to socket object for garbage collection
            self.sock = None

    def process_protoheader(self): # 解析协议头部信息，得到 json header 大小
        hdrlen = 2
        if len(self._recv_buffer) >= hdrlen:
            self._jsonheader_len = struct.unpack('>H',
                                                 self._recv_buffer[:hdrlen])[0]
            self._recv_buffer = self._recv_buffer[hdrlen:]

    def process_jsonheader(self): # 解析 json header 信息，得到真实请求信息
        hdrlen = self._jsonheader_len
        if len(self._recv_buffer) >= hdrlen:
            self.jsonheader = self._json_decode(self._recv_buffer[:hdrlen],
                                                'utf-8')
            self._recv_buffer = self._recv_buffer[hdrlen:]
            for reqhdr in ('byteorder', 'content-length', 'content-type',
                           'content-encoding'):
                if reqhdr not in self.jsonheader:
                    raise ValueError(f'Missing required header "{reqhdr}".')

    def process_request(self):
        content_len = self.jsonheader['content-length']
        if not len(self._recv_buffer) >= content_len:
            return
        data = self._recv_buffer[:content_len]
        self._recv_buffer = self._recv_buffer[content_len:]
        if self.jsonheader['content-type'] == 'text/json':
            encoding = self.jsonheader['content-encoding']
            self.request = self._json_decode(data, encoding)
            print('received request', repr(self.request), 'from', self.addr)
        else:
            # Binary 或者未知请求类型
            self.request = data
            print(f'received {self.jsonheader["content-type"]} request from',
                  self.addr)
        # 设置 selector 监听写入事件，读事件已经完成
        self._set_selector_events_mask('w')

    def create_response(self):
        if self.jsonheader['content-type'] == 'text/json':
            response = self._create_response_json_content()
        else:
            # Binary or unknown content-type
            response = self._create_response_binary_content()
        message = self._create_message(**response)
        self.response_created = True
        self._send_buffer += message
```

app-server.py
```python
#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback

import libserver

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    message = libserver.Message(sel, conn, addr)
    sel.register(conn, selectors.EVENT_READ, data=message)

if len(sys.argv) != 3:
    print('usage:', sys.argv[0], '<host> <port>')
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Avoid bind() exception: OSError: [Errno 48] Address already in use
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind((host, port))
lsock.listen()
print('listening on', (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None) # 将 socket 监听事件注册到 selector

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None: # 如果没有请求数据，则为客户端连接请求
                accept_wrapper(key.fileobj)
            else:
                message = key.data
                try:
                    message.process_events(mask) # 处理请求信息
                except Exception:
                    print('main: error: exception for',
                          f'{message.addr}:\n{traceback.format_exc()}')
                    message.close()
except KeyboardInterrupt:
    print('caught keyboard interrupt, exiting')
finally:
    sel.close()
```

### Client

libclient.py
```python
import sys
import selectors
import json
import io
import struct

class Message:

    def __init__(self, selector, sock, addr, request):
        self.selector = selector
        self.sock = sock
        self.addr = addr
        self.request = request
        self._recv_buffer = b''
        self._send_buffer = b''
        self._request_queued = False
        self._jsonheader_len = None
        self.jsonheader = None
        self.response = None

    def _set_selector_events_mask(self, mode):
        """Set selector to listen for events: mode is 'r', 'w', or 'rw'."""
        if mode == 'r':
            events = selectors.EVENT_READ
        elif mode == 'w':
            events = selectors.EVENT_WRITE
        elif mode == 'rw':
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
        else:
            raise ValueError(f'Invalid events mask mode {repr(mode)}.')
        self.selector.modify(self.sock, events, data=self)

    def _read(self):
        try:
            # Should be ready to read
            data = self.sock.recv(4096)
        except BlockingIOError:
            # Resource temporarily unavailable (errno EWOULDBLOCK)
            pass
        else:
            if data:
                self._recv_buffer += data
            else:
                raise RuntimeError('Peer closed.')

    def _write(self):
        if self._send_buffer:
            print('sending', repr(self._send_buffer), 'to', self.addr)
            try:
                # Should be ready to write
                sent = self.sock.send(self._send_buffer)
            except BlockingIOError:
                # Resource temporarily unavailable (errno EWOULDBLOCK)
                pass
            else:
                self._send_buffer = self._send_buffer[sent:]

    def _json_encode(self, obj, encoding): # JSON 编码
        return json.dumps(obj, ensure_ascii=False).encode(encoding)

    def _json_decode(self, json_bytes, encoding): # JSON 解码
        tiow = io.TextIOWrapper(io.BytesIO(json_bytes), encoding=encoding,
                                newline='')
        obj = json.load(tiow)
        tiow.close()
        return obj

    def _create_message(self, *, content_bytes, content_type,
                        content_encoding): # 打包处理请求信息
        jsonheader = {
            'byteorder': sys.byteorder,
            'content-type': content_type,
            'content-encoding': content_encoding,
            'content-length': len(content_bytes)
        }
        jsonheader_bytes = self._json_encode(jsonheader, 'utf-8')
        message_hdr = struct.pack('>H', len(jsonheader_bytes))
        message = message_hdr + jsonheader_bytes + content_bytes
        return message

    def _process_response_json_content(self):
        content = self.response
        result = content.get('result')
        print(f'got result: {result}')

    def _process_response_binary_content(self):
        content = self.response
        print(f'got response: {repr(content)}')

    def process_events(self, mask):
        if mask & selectors.EVENT_READ:
            self.read()
        if mask & selectors.EVENT_WRITE:
            self.write()

    def read(self):
        self._read()

        if self._jsonheader_len is None:
            self.process_protoheader()

        if self._jsonheader_len is not None:
            if self.jsonheader is None:
                self.process_jsonheader()

        if self.jsonheader:
            if self.response is None:
                self.process_response()

    def write(self):
        if not self._request_queued:
            self.queue_request()

        self._write()

        if self._request_queued:
            if not self._send_buffer:
                # Set selector to listen for read events, we're done writing.
                self._set_selector_events_mask('r')

    def close(self):
        print('closing connection to', self.addr)
        try:
            self.selector.unregister(self.sock)
        except Exception as e:
            print(f'error: selector.unregister() exception for',
                  f'{self.addr}: {repr(e)}')

        try:
            self.sock.close()
        except OSError as e:
            print(f'error: socket.close() exception for',
                  f'{self.addr}: {repr(e)}')
        finally:
            # Delete reference to socket object for garbage collection
            self.sock = None

    def queue_request(self):
        content = self.request['content']
        content_type = self.request['type']
        content_encoding = self.request['encoding']
        if content_type == 'text/json':
            req = {
                'content_bytes': self._json_encode(content, content_encoding),
                'content_type': content_type,
                'content_encoding': content_encoding
            }
        else:
            req = {
                'content_bytes': content,
                'content_type': content_type,
                'content_encoding': content_encoding
            }
        message = self._create_message(**req)
        self._send_buffer += message
        self._request_queued = True

    def process_protoheader(self):
        hdrlen = 2
        if len(self._recv_buffer) >= hdrlen:
            self._jsonheader_len = struct.unpack('>H',
                                                 self._recv_buffer[:hdrlen])[0]
            self._recv_buffer = self._recv_buffer[hdrlen:]

    def process_jsonheader(self):
        hdrlen = self._jsonheader_len
        if len(self._recv_buffer) >= hdrlen:
            self.jsonheader = self._json_decode(self._recv_buffer[:hdrlen],
                                                'utf-8')
            self._recv_buffer = self._recv_buffer[hdrlen:]
            for reqhdr in ('byteorder', 'content-length', 'content-type',
                           'content-encoding'):
                if reqhdr not in self.jsonheader:
                    raise ValueError(f'Missing required header "{reqhdr}".')

    def process_response(self):
        content_len = self.jsonheader['content-length']
        if not len(self._recv_buffer) >= content_len:
            return
        data = self._recv_buffer[:content_len]
        self._recv_buffer = self._recv_buffer[content_len:]
        if self.jsonheader['content-type'] == 'text/json':
            encoding = self.jsonheader['content-encoding']
            self.response = self._json_decode(data, encoding)
            print('received response', repr(self.response), 'from', self.addr)
            self._process_response_json_content()
        else:
            # Binary or unknown content-type
            self.response = data
            print(f'received {self.jsonheader["content-type"]} response from',
                  self.addr)
            self._process_response_binary_content()
        # Close when response has been processed
        self.close()
```

app-client.py

```python
#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback

import libclient

sel = selectors.DefaultSelector()

def create_request(action, value):
    if action == 'search':
        return dict(
            type='text/json',
            encoding='utf-8',
            content=dict(action=action, value=value)
        )
    else:
        return dict(
            type='binary/custom-client-binary-type',
            encoding='binary',
            content=bytes(action + value, encoding='utf-8')
        )

def start_connection(host, port, request):
    addr = (host, port)
    print('starting connection to', addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = libclient.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)

if len(sys.argv) != 5:
    print('usage:', sys.argv[0], '<host> <port> <action> <value>')
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
action, value = sys.argv[3], sys.argv[4]
request = create_request(action, value)
start_connection(host, port, request)

try:
    while True:
        events = sel.select(timeout=1)
        for key, mask in events:
            message = key.data
            try:
                message.process_events(mask)
            except Exception as e:
                print('main: error: exception for',
                      f'{message.addr}:\n{traceback.format_exc()}')
                message.close()
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print('caught keyboard interrupt, exiting')
finally:
    sel.close()
```


## 总结

学习了通过 selector 多路 I/O 复用方式来处理 socket 多连接情况，如果请求量少的情况下，也可以使用多线程方式处理。

selector 是 Python3.6 标准库，等之后更了解 select、poll、epoll 之后写一篇总结。
（不知道何年何月啊）
