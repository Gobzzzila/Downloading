import requests
r = requests.get(url)
with open("code3.zip", "wb") as code:
    code.write(r.content)
