# Challange Info

Name : Search source

Difficulty : Medium

Category : Web Exploitation

Link : 

# Writeup

Mirroring the website using wget.

```bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent http://saturn.picoctf.net:60905/
```

Going inside every folder and trying grep to find the flag.

```bash
cat * | grep pico
```

In CSS folder there is file which contains the flag.
