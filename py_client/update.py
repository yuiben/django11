from webbrowser import get
import requests

endpoint ="http://127.0.0.1:8000/api/products/1/update/"
data = {
    "title" : "Update Test 1",
    "price" : 25.99
}
get_response = requests.put(endpoint, json=data) #HTTP Request

print(get_response.status_code)
print(get_response.json())
