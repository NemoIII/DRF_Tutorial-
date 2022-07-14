# Basicly is where I'll put the endpoint to conect with the FE made in RN.
# API mean Application Programming Interface
# Remember, when is possible, link a method to a variable!
# Rest API -> Web API
# HTTP Request -> HTML
# REST API HTTP Request HTTP Request->JSON
# JavaScript Object Nototion Python Dict


import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world"})

print(get_response.json())