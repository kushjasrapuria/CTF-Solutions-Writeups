# Challange Info

Name : dont-use-client-side

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/66?category=1&page=1

# Writeup

Navigating the webpage https://jupiter.challenges.picoctf.org/problem/17682/.

Inspecting the source code we get javascript code.

```javascript
function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'fl') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ag') {
          if (checkpass.substring(split*3, split*4) == 'ow') {
            if (checkpass.substring(split*5, split*6) == 'n') {
              if (checkpass.substring(split*2, split*3) == 'e') {
                if (checkpass.substring(split*7, split*8) == 'd}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
}
```

The flag is scrambled if we get all parts together in correct order and submit it on webapp we get a alert with `Password Verified` and the flag.
