import requests

# GET request to fetch data from an API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print("Status Code:", response.status_code) # 200 OK
print("Response Body:", response.json()) # data as a Python dictionary

# POST request to send data to an API
response = requests.post('https://jsonplaceholder.typicode.com/posts', 
                        json={"title": "food", "body": "bar", "userId": 1},
                        headers={"Content-type": "application/json; charset=UTF-8"})

print("Status Code:", response.status_code) # 201 Created
print("Response Body:", response.json()) # data as a Python dictionary