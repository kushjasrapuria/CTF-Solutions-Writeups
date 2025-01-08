# Challange Info

Name : PHP - Command injection

Difficulty : Very easy

Category : Web Server

Link : https://www.root-me.org/en/Challenges/Web-Server/PHP-Command-injection

# Writeup

The webapp provides functionality of pinging servers.

There is possible command injection.

Sending payload `1 | ls -al` and found out there is .passwd file.

Sending `1 | cat .passwd` I got the flag.
