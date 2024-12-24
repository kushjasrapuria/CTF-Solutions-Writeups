# Challange Info

Name : Cookies

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/173?category=1&page=1

# Writeup

Navigating the webpage http://mercury.picoctf.net:64944/.

The input feild has a placeholder snickerdoodle se we enter `snickerdoodle` and press Search.

The webpage returned says :

```
I love snickerdoodle cookies!
```

For inspecting website cookies i use web extension called Cookie-Editor.

Extension Link : https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm

Looking at the cookie the name cookie value before searching `snickerdoodle` was -1 and after searching it became 0.

So i tried changing the value to 1 and the webpage returned had different message.

```
I love chocolate chip cookies!
```

I found out the max value for name cookie is 28.

Then I tried random numbers between 0 and 28 and got the flag at name value 18.
