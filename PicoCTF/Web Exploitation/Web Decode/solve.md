# Challange Info

Name : Web Decode

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/427?category=1&page=1

# Writeup

Navigating the web app http://titan.picoctf.net:50129/about.html.

The page displays following message : Try inspecting the page!! You might find it there.

Inspecting the webpage we get.

```HTML
<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDJjZGNiNTl9">
```

To automatically detect possible ciphers we can use dcode's cipher identifier.

Website Link : https://www.dcode.fr/cipher-identifier

It's base64 cipher using base64 decoder we can get our flag.
