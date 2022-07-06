# Basicly is where I'll put the endpoint to conect with the FE made in RN.
# API mean Application Programming Interface
# Remember, when is possible, link a method to a variable!
# Rest API -> Web API
# HTTP Request -> HTML
# REST API HTTP Request HTTP Request->JSON
# JavaScript Object Nototion Python Dict


import requests


# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query": "Hello world"}) # Here we will emulate a HTTP Request
# print(get_response.headers)

# print(get_response.text) # print the raw text code

print(get_response.json())
# print(get_response.status_code)