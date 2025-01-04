# Challange Info

Name : Forbidden Paths

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/270?category=1&page=1

# Writeup

The website allows us to read files from specified path.

The description says the flag is stored in root directory and blocks absolute path.

So I used relative path and get our flag.

Sending payload `../../../../flag.txt`.

And I got the flag.
