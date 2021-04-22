# https://www.geeksforgeeks.org/response-json-python-requests/
import requests


# Making a get request
response = requests.get("http://127.0.0.1:8000/heroes/")

# print response
print(response)

# print json content

print(response.json())
jsonres = response.json()

# for host in jsonData:
# Name = host.get("name")
# StatusText = host.get("status_text")
for i in jsonres:
     print(i["name"])
     print(i['alias'])


