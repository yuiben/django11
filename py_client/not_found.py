import requests

endpoint ="http://127.0.0.1:8000/api/products/121313213213"
get_response = requests.get(endpoint) #HTTP Request

print(get_response.status_code)
print(get_response.json())
