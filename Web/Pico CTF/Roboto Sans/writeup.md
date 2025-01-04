# Challange Info

Name : Roboto Sans

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/291?category=1&page=1

# Writeup

Mirroring the website with wget.

There is a robots.txt file.

```
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

Decoding base64 value `anMvbXlmaWxlLnR4dA==` I got `js/myfile.txt`.

Navigating to this page I got the flag.
