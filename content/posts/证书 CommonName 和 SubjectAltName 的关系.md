---
title: 证书 CommonName 和 subjectAltName 的关系
date: 2023-03-25
tags:
- HTTPS
description: 
---


## 背景

因为产品中的 HTTPS 所用证书是自签发证书，不满足一些场景的安全要求，需要导入用户证书。本身这个变更很容易，只需要按照[Nginx 官方文档]([http://nginx.org/en/docs/http/configuring_https_servers.html](http://nginx.org/en/docs/http/configuring_https_servers.html))  配置下指定证书即可，但遇到了一个特殊的场景：集群存在3个节点，每个节点用户配置了相应的 Domain Name，其中集群中存在 VIP(Virtual IP Address) ，用户给对应的 VIP 配置了相应的 Domain Name。用户在签发证书时，使用的 CN(CommonName) 是 VIP 对应的 Domain Name，subjectAltName 是集群中3个节点的 Domain Name。此时如果通过各个节点相应的 Domain Name 访问，证书有效，但是通过 VIP 对应的 Domain Name 访问，证书无效（因环境特殊，未能看到具体错误提示）。

印象中 `CommonName` 必须指定对应的 Domain Name，`subjectAltName` 是 `CommonName` 的补充，所以这个现象感觉不合理，然后查阅了相关资料进行调查。

## GPT4

在调查之前，按照现在的主流操作，遇事不决先问 GPT，于是得到了如下答复，也符合我的理解：

问：
>在 https 证书中，如果 `CommonName` 一定存在于 `SubjectAltName` 中么？如果同时存在 `CommonName` 和 `SubjectName` ，使用哪个作为唯一标识校验？

答：
>在HTTPS证书中，`CommonName`（CN）和`Subject Alternative Name`（SAN）是用于标识证书所表示的域名的字段。在早期的SSL/TLS证书中，`CommonName`通常用于表示证书关联的单个域名。然而，随着时间的推移，`Subject Alternative Name`扩展被广泛采用，它允许证书关联多个域名和子域名。  
> 从技术上讲，`CommonName`不一定需要出现在`Subject Alternative Name`列表中。但是，实际上，许多现代浏览器和客户端会首先检查`Subject Alternative Name`字段，如果没有找到匹配的域名，才会检查`CommonName`字段。因此，为了确保证书的兼容性和正确性，建议将`CommonName`包含在`Subject Alternative Name`字段中。   
> RFC 6125（表示和确认服务器标识的通用方法）建议在比较服务器标识时使用`Subject Alternative Name`，并认为`CommonName`已经过时。因此，如果`CommonName`和`Subject Alternative Name`同时存在，客户端应首先使用`Subject Alternative Name`进行匹配和校验。

## RFC 调查

在 X509 的相关RFC [https://www.rfc-editor.org/rfc/rfc2459](https://www.rfc-editor.org/rfc/rfc2459) ，[https://www.rfc-editor.org/rfc/rfc3280](https://www.rfc-editor.org/rfc/rfc3280) 和 [https://www.rfc-editor.org/rfc/rfc5280](https://www.rfc-editor.org/rfc/rfc5280) 定义中没有很多关于 CommonName 与 SubjectAltName 关系描述。

在 [https://www.rfc-editor.org/rfc/rfc6125](https://www.rfc-editor.org/rfc/rfc6125) 中，关于两者的关系有如下描述：

```
For TLS authentication with X.509 certificates, an identity from the
DNS namespace MUST be checked against each subjectAltName extension
of type dNSName present in the certificate.  If no such extension is
present, then the identity MUST be compared to the (most specific)
Common Name in the Subject field of the certificate.  When matching
DNS names against dNSName or Common Name fields, matching is case-
insensitive.  Also, a "*" wildcard character MAY be used as the left-
most name component in the certificate or identity in the APD.  For
example, *.example.com in the APD would match certificates for
a.example.com, foo.example.com, *.example.com, etc., but would not
match example.com.  Similarly, a certificate for *.example.com would
be valid for APD identities of a.example.com, foo.example.com,
*.example.com, etc., but not example.com.
```

在 HTTPS 的 RFC [https://www.rfc-editor.org/rfc/rfc2818](https://www.rfc-editor.org/rfc/rfc2818) 中，关于两者的关系有如下描述：

```
If a subjectAltName extension of type dNSName is present, that MUST
be used as the identity. Otherwise, the (most specific) Common Name
field in the Subject field of the certificate MUST be used. Although
the use of the Common Name is existing practice, it is deprecated and
Certification Authorities are encouraged to use the dNSName instead.
```

TLS/SSL 证书中的 `subjectAltName` 扩展除了包含 `dNSName` 类型之外，还可以包含其他类型的名称，比如IP地址、电子邮件地址或URI等。当客户端使用 HTTPS 连接到服务器时，它首先检查服务器的证书以验证其身份。在这个过程中，客户端会检查证书中的subjectAltName扩展，如果证书中存在 `subjectAltName` 扩展， `subjectAltName` 扩展中的dNSName类型用于指定与证书相关联的域名，如果存在 dNSName，则使用 dNSName 作为身份校验方式。

如果客户端的目标域名与 `subjectAltName` 扩展中的域名匹配，则证书被视为有效，连接可以继续进行。如果没有匹配，则连接被视为不受信任。

如果证书中不存在 `subjectAltName` dNSName 字段，则使用证书的Subject字段中的Common Name字段来标识服务器。

## 浏览器支持调查

### Chrome

在 58 版本中，删除了对 CommonName 匹配的支持，[https://chromestatus.com/feature/4981025180483584](https://chromestatus.com/feature/4981025180483584)： 

> RFC 2818 describes two methods to match a domain name against a certificate - using the available names within the subjectAlternativeName extension, or, in the absence of a SAN extension, falling back to the commonName.  
The fallback to the commonName was deprecated in RFC 2818 (published in 2000), but support still remains in a number of TLS clients, often incorrectly.


在Chrome 论坛中关于这个改动的讨论写的非常清晰：

```go
Link to "Intent to Deprecate" thread
No deprecate thread; it's been deprecated since HTTPS was first introduced (RFC 2818) in 2000.

Summary
Certificates have two ways to express the domain/IP they're bound to - one which is unstructured and ambiguous (commonName), and one which is well-defined (subjectAltName). In the absence of any subjectAltNames, Chrome currently falls back to comparing the domain against the commonName, if present.

This proposal is to remove that fallback path; in effect, requiring a subjectAltName. Ideally, we would do this for all certificates (publicly trusted and privately trusted), but if there are concerns about compat risk, we can restrict it to publicly trusted certificates.

Motivation
Since 1997 (X.509v3's ratification), certificates have had two ways to express a binding to a domain name - either via the commonName attribute within the certificate's subject, or via the explicitly typed (dNSName or iPAddress) of the SubjectAlternativeName Extension.

Since RFC 2818 (published in 2000, first drafted in January 1998), the use of the commonName field has been considered deprecated, because it's ambiguous and untyped - that is, it might contain a human-readable name or it might be a domain name.

The use of the subjectAlternativeName fields leaves it unambiguous whether a certificate is expressing a binding to an IP address or a domain name, and is fully defined in terms of its interaction with Name Constraints. commonName, however, is ambiguous, and because of this, support for the commonName has been a source of security bugs - in both Chrome and the libraries it uses and within the TLS ecosystem at large.

Compatibility Risk
Low. RFC 2818 has deprecated this for nearly two decades, and the Baseline Requirements (which all publicly trusted CAs must abide by) has required the presence of a subjectAltName since 2012.

Mozilla Firefox already requires the subjectAltName for any newly issued publicly trusted certificates since Firefox 48 ( https://bugzilla.mozilla.org/show_bug.cgi?id=1245280 ).

Usage information
From a metrics perspective, less than .002% of publicly trusted certificate validations would require this behaviour (Net.CertCommonNameFallback minus Net.CertCommonNameFallbackPrivateCA).

As 1.57% of privately-trusted CA certificates rely on this behaviour (or 0.1% of all certificate validations), it may be premature to deprecate it for privately-trusted CAs; alternatively, we could remove it with an enterprise policy to allow it for a limited number of releases. Unfortunately, despite being deprecated for nearly 20 years, it's unlikely we'd be able to drive this number down (and improve the security of the ecosystem) without taking further action.

OWP launch tracking bug
https://bugs.chromium.org/p/chromium/issues/detail?id=308330

Entry on the feature dashboard
https://www.chromestatus.com/feature/4981025180483584 (Apologies if I botched this; not sure how to capture "The standard says this is deprecated, and Mozilla supports deprecating")
```

### Firefox

[https://bugzilla.mozilla.org/show_bug.cgi?id=1245280](https://bugzilla.mozilla.org/show_bug.cgi?id=1245280)

## 结论

CommonName 已经不被作为身份验证标识，统一使用 SubjectAltName 。

参考链接：

- [https://chromestatus.com/feature/4981025180483584](https://chromestatus.com/feature/4981025180483584)
- [https://bugzilla.mozilla.org/show_bug.cgi?id=1245280](https://bugzilla.mozilla.org/show_bug.cgi?id=1245280)