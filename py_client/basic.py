import requests

# endpoint = 'https://httpbin.org/'
endpoint = "http://127.0.0.1:8000/api"
get_response = requests.get(endpoint, params={"abc":123}, json={"query":"hello"}) # give a request
# print(get_response.text) # print raw text response

print(get_response.json()) # print raw python dictonary

