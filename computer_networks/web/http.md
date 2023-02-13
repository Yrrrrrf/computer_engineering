# HyperText Transfer Protocol

Is an application layer protocol in the [Internet protocol](./web.md#http) suite model for distributed, collaborative hypermedia information systems.


### Request
The request use the headers to specify to the server where & what data does the host needs.
- $GET$ is the method that asks to the server to bring that data.
```http
GET / HTTP/1.1
Host: www.google.com
AcceptLanguage: en-US
```

### Response
The response also uses the same structure to answer the request. This asnwer contains lots of information from the request and the status code.
The response always have a **body**, this usually is a **.json**

```http
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
ETag: "34aa387-d-1568eb00"
Accept-Ranges: bytes
Content-Length: 51
Vary: Accept-Encoding
Content-Type: text/plain

Hello World! The time is: Mon, 27 Jul 2009 12:28:53 GMT
```


### HTTP Status Codes
![http status codes](/resources/img/computer%20network/http%20status.png)