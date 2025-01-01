# Challange Info

Name : findme

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/349?category=1&page=1

# Writeup

The webapp requires you to login and provides login creds `test` and `test!` as username and passwd respectively.

Capturing requests after login via burpsuite.

There were two request after login with 2 different id's these id's are flag seprated in two parts.

Base64 decode both parts and flag will be revealed
