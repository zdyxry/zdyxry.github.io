---
title: Exponential backoff
date: 2018-12-01 20:26:02
tags:
---


## 背景
昨天看到 Ansible 关于 Linux reboot plugin  [相关文章](https://www.ansible.com/blog/reboot-plugin-for-linux-in-ansible-2-7?utm_medium=Email&utm_campaign=weekly&sc_cid=701f2000000RRCNAA4) 时，看到了它关于重试等待的设计，了解了下 Exponential backoff，特此记录。

## 简介

假设存在需求：
1. 获取服务器 A 启动时间
2. 重启服务器 A
3. 获取服务器 A 当前时间

其中第 2 点，我一般会重启服务器 A 后，不断的重连服务器 A 来判断服务器 A 是否正常启动，每次重连后等待，再次重试，设置一个最大超时时间，超过最大超时时间认为服务器 A 启动失败，任务失败。

那么什么是 Exponential backoff 呢？ 中文应该叫“指数退避”，意思就是每次重连失败后，等待的时候随着重试次数的增加而成指数增长，如果我们第1次重试等待时间为2s，则第2次重试等待时间为4s，第三次重试等待时间为8s，以此类推。

我理解最大的好处就是防止短时间内大量的重复错误，有时候当你知道你的操作是短时间无法完成的（比如重启服务器 A），那么该操作执行过程中，短时间内重试多次是没有意义的。当然我们也不能让重试等待时间无限的增长，我们可以设置一个最大的重试时间（不是最大超时时间），如果大于等于最大重试时间，则等待最大重试时间后再次重试。

## 具体实现

### 伪代码
```
Do some asynchronous operation.

retries = 0

DO
    wait for (2^retries * 100) milliseconds

    status = Get the result of the asynchronous operation.

    IF status = SUCCESS
        retry = false
    ELSE IF status = NOT_READY
        retry = true
    ELSE IF status = THROTTLED
        retry = true
    ELSE
        Some other error occurred, so stop calling the API.
        retry = false
    END IF

    retries = retries + 1

WHILE (retry AND (retries < MAX_RETRIES))
```

### Ansible linux reboot  plugin

```pyth
fail_count = 0
max_fail_sleep = 12

while datetime.utcnow() < max_end_time:
    try:
        action()
        if action_desc:
            display.debug('%s: %s success' % (self._task.action, action_desc))
        return
    except Exception as e:
        # Use exponential backoff with a max timout, plus a little bit of randomness
        random_int = random.randint(0, 1000) / 1000
        fail_sleep = 2 ** fail_count + random_int
        if fail_sleep > max_fail_sleep:
            fail_sleep = max_fail_sleep + random_int
        if action_desc:
            display.debug("{0}: {1} fail '{2}', retrying in {3:.4} seconds...".format(self._task.action, action_desc, to_text(e), fail_sleep))
        fail_count += 1
        time.sleep(fail_sleep)
```

