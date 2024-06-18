#!/usr/bin/env python3

import requests
import json 

cat_response = requests.get("https://api.thecatapi.com/v1/breeds")

cat_text = cat_response.text

cat_status_code = cat_response.status_code

cat_headers = cat_response.headers

cat_request = cat_response.request

cat_url = cat_request.url

cat_url_path = cat_request.path_url

cat_method = cat_request.method

cat_request_headers = cat_request.headers


# Check https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages for more information on these APIs

print(f"Response: {cat_response}\n")
print(f"Status Code: {cat_status_code}\n")
print(f"Text: {cat_text}\n")
print(f"Headers: {cat_headers}\n")
print(f"Response Request: {cat_request}\n")
print(f"Request URL: {cat_url}\n")
print(f"Request Path URL: {cat_url_path}\n")
print(f"request Method: {cat_method}\n")
print(f"Request Headers: {cat_request_headers}\n")

