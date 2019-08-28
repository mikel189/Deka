import requests
import json

url = 'http://127.0.0.1:5000/predict_desc'
payload = {'id' : 'cj9swsow968mg0131kaw103ld'}

response = requests.post(url, json = payload)
# print(data.status_)
print(response.content)
# print(response.request.path_url)
