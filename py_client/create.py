from webbrowser import get
import requests

endpoint ="http://127.0.0.1:8000/api/products/"
data = {
    "title" : "OK het ROi doa"
}
get_response = requests.post(endpoint, json=data) #HTTP Request

print(get_response.status_code)
print(get_response.json())
