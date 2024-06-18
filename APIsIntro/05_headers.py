#!/usr/bin/env python3

import requests

#Mozilla's extended list of headers
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

response = requests.get("https://api.thecatapi.com/v1/breeds/abys")

print("\n")
# Inspecting the headers of a response:
print(response.headers)

print("\n")
# Inspecting the request headers:
print(response.request.headers)


# Custom headers
