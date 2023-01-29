import requests

token = input("Enter the meta for devs generated access token: ")
url = "https://graph.facebook.com/v15.0/me?access_token=" + token.strip()
req = requests.get(url)
print("Request output:\n{}".format(req.content))