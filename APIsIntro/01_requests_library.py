#!/usr/bin/env python3

import requests
import json

# requests is a library module that provides an easy way to send HTTP requests, handle responses, and manage various aspects of the request process

endpoint = 'https://v6.exchangerate-api.com/v6/9ef5d2df2b0efb6f101fdc46/latest/USD'

# Make a GET request to the API endpoint
response = requests.get(endpoint)


# Not including writing on the terminal if the request was successful
# print(type(response))
# print(response)

# Checking if request was useful
if response.status_code == 200:
    data = response.json()

    # Print the JSON content to the console
    print(json.dumps(data, indent=4))

    # Write the JSON content to a file
    with open('exchange_rates.json', 'w') as file:
        json.dump(data, file, indent=4)
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

