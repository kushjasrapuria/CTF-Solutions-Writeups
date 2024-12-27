# Challange Info

Name : Bookmarklet

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/406?category=1&page=1

# Writeup

Navigating the webpage http://titan.picoctf.net:51975/.

It provides us with javascript code.

```javascript
javascript:(function() {
            var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÒËÉ§©í";
            var key = "picoctf";
            var decryptedFlag = "";
            for (var i = 0; i < encryptedFlag.length; i++) {
                decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
            }
            alert(decryptedFlag);
        })();
```

Using Chrome Dev Tools > Console.

```
allow pasting
```

Then paste the javascript code in console and a alert will appear with the flag.
