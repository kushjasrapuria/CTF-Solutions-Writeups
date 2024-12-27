# Challange Info

Name : Includes

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/274?category=1&page=1

# Writeup

Navigating the webpage http://saturn.picoctf.net:54975/.

Inspecting the source code.

There was a `Say hello` button which pops up alert which says.

```
This code is in a separate file!
```

In the body of the HTML code there was a script included from external source and in the head section a CSS file is also included.

```html
<script src="script.js"></script>
```

```html
<link rel="stylesheet" href="style.css">
```

Checking the javascript file we get.

```javascript
function greetings()
{
  alert("This code is in a separate file!");
}

//  owned}
```

This seems like half part of the flag so i decided to try opening CSS file also.

```css
body {
  background-color: lightblue;
}

/*  picoCTF{flag  */
```
