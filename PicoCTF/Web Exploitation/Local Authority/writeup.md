# Challange Info

Name : Local Authority

Difficulty : Easy

Category : Web Exploitation

Link : https://play.picoctf.org/practice/challenge/278?category=1&page=1

# Writeup

Navigating the webpage http://saturn.picoctf.net:62279/.

Inspecting the source code.

```javascript
      function filter(string) {
        filterPassed = true;
        for (let i =0; i < string.length; i++){
          cc = string.charCodeAt(i);
          
          if ( (cc >= 48 && cc <= 57) ||
               (cc >= 65 && cc <= 90) ||
               (cc >= 97 && cc <= 122) )
          {
            filterPassed = true;     
          }
          else
          {
            return false;
          }
        }
        
        return true;
      }
    
      window.username = "fgfdg";
      window.password = "fdgdfg";
      
      usernameFilterPassed = filter(window.username);
      passwordFilterPassed = filter(window.password);
      
      if ( usernameFilterPassed && passwordFilterPassed ) {
      
        loggedIn = checkPassword(window.username, window.password);
        
        if(loggedIn)
        {
          document.getElementById('msg').innerHTML = "Log In Successful";
          document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881";
          document.getElementById('hiddenAdminForm').submit();
        }
        else
        {
          document.getElementById('msg').innerHTML = "Log In Failed";
        }
      }
      else {
        document.getElementById('msg').innerHTML = "Illegal character in username or password."
      }
```

This code only checks weather the provided username and password is in given range.

0-9, A-Z, a-z

If not it will return Illegal character in username or password webpage.

There is a function name `loggedIn = checkPassword(window.username, window.password);` defined somewhere else.

Within body of HTML there is a script imported from external file.

```html
<script src="secure.js"></script>
```

This external script has the code for `checkPassword` function.

```javascript
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

Logging in using these credentials we get our flag.
