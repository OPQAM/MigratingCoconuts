#!/usr/bin/env python3

import requests

# requests is a library module that provides an easy way to send HTTP requests, handle responses, and manage various aspects of the request process

endpoint = 'https://v6.exchangerate-api.com/v6/9ef5d2df2b0efb6f101fdc46/latest/USD'

# Make a GET request to the API endpoint
response = requests.get(endpoint)


print(type(response))
print(response)
