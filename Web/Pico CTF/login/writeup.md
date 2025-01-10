# Challange Info

Name : login

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/200?category=1&page=1

# Writeup

The webapp provides a login form with username and password.

Inspecting the source code for further analysis. I found out the following javascript code.

```javascript
(async () => {
    await new Promise((e => window.addEventListener("load", e))),
    document.querySelector("form").addEventListener("submit", (e => {
        e.preventDefault();
        const r = {
            u: "input[name=username]",
            p: "input[name=password]"
        }
          , t = {};
        for (const e in r)
            t[e] = btoa(document.querySelector(r[e]).value).replace(/=/g, "");
        return "YWRtaW4" !== t.u ? alert("Incorrect Username") : "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" !== t.p ? alert("Incorrect Password") : void alert(`Correct Password! Your flag is ${atob(t.p)}.`)
    }
    ))
}
)();
```

The username and password the base64 encoded in the javascript.

`YWRtaW4` base64 decodes to `admin` which is username.

The base64 decode of `cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ` is password and flag for this challange.
