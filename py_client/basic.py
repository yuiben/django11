from webbrowser import get
import requests

endpoint ="http://127.0.0.1:8000/api/"
#endpoint ="http://httpbin.org/status/200/"

get_response = requests.post(endpoint, params={"abc": 123}, json={"content":"hello nhe"}) #HTTP Request
#print(get_response.text) #Print raw text response
print(get_response.status_code)

#http Request ->html
# REST API HTTP Request -> JSON
# JavaScripts Object Nototion ~ Python Dict
print(get_response.json())
#print(get_response.json()['message'])
