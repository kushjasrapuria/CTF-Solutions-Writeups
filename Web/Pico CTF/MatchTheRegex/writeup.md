# Challange Info

Name : MatchTheRegex

Difficulty : Medium

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/356?category=1&page=2

# Writeup

The webapp provides you a input feild with submit form so we inspect source code for any clues.

The webapp has this javascript code.

```javascript
function send_request() {
	let val = document.getElementById("name").value;
	// ^p.....F!?
	fetch(`/flag?input=${val}`)
		.then(res => res.text())
		.then(res => {
			const res_json = JSON.parse(res);
			alert(res_json.flag)
			return false;
		})
	return false;
}
```

This provides with the regex it's being tested against.

`p.....F` anything starts with p and ends with F with 5 any sort of charater except new line in between should work to pass the check for this regex. 
