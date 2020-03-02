import requests


input_data = "{\"data\": [230.1,37.8,69.2]}"

headers = {'Content-Type': 'application/json'}
resp = requests.post('http://885571cc-4fa3-4417-9766-b8bbd00fb2ba.westeurope.azurecontainer.io/score', input_data, headers=headers)
print("prediction:", resp.text)