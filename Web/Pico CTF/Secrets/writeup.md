# Challange Info

Name : Secrets

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/296?category=1&page=1

# Writeup

The webpage dosen't have any usefull functions and has only 3 static pages.

Inspecting source code.

```html
<link href="secret/assets/index.css" rel="stylesheet">
```

Going back to secret we get a gif inspecting again.

```html
<link rel="stylesheet" href="hidden/file.css">
```

Going back to hidden and inspecting again.

```html
<link href="superhidden/login.css" rel="stylesheet">
```

A login form in order to see how it works I inspected source but found something else.

I tried going back to supperhidden and inspecting and I got the flag.

http://saturn.picoctf.net:54196/secret/hidden/superhidden/
