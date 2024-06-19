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

# sometimes will have 'x-', but not always.
# We can use dicts to define headers and send them with .get()

headers = {"X-Request-Id": "<my-request-id>"}
resposta = requests.get("https://example.org", headers = headers)
print(resposta.request.headers)


