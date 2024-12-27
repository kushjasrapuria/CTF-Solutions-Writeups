# Challange Info

Name : Scavenger Hunt

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/161?category=1&page=1

# Writeup

Navigating the webpage http://mercury.picoctf.net:39491/.

Inspecting the source code we get.

```html
<!-- Here's the first part of the flag: picoCTF{fl -->
```

In the head section of the HTML code there was a script and CSS included from external source.

```html
<script type="application/javascript" src="myjs.js"></script>
```

```html
<link rel="stylesheet" type="text/css" href="mycss.css">
```

Checking the CSS file we get.

```css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: ag */
```

Checking the javascript file we get.

```javascript
function openTab(tabName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
	tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
	tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(tabName).style.display = "block";
    if(elmnt.style != null) {
	elmnt.style.backgroundColor = color;
    }
}

window.onload = function() {
    openTab('tabintro', this, '#222');
}

/* How can I keep Google from indexing my website? */
```

To keep google from indexing our website we use robots.txt file.

Checking robots.txt file we get.

```
User-agent: *
Disallow: /index.html
# Part 3: ow
# I think this is an apache server... can you Access the next flag?
```

Apache server has .htaccess file.

Checking .htaccess file we get.

```
# Part 4: ne
# I love making websites on my Mac, I can Store a lot of information there.
```

On mac .DS_Store file is created to store metadata of folder.

Checking .DS_Store file we get.

```
Congrats! You completed the scavenger hunt. Part 5: d}
```
