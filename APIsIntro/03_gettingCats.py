#!/usr/bin/env python3


import requests
import json        # We want to make the code more readable and bearable



response = requests.get('https://api.thecatapi.com/')

meow = response.text

# In this case we're just get a generic message, since we're calling the base URL - used for basic API info
print(meow)

# We need endpoints!

# Let's create an endpoint variable for it
endpoint = 'https://api.thecatapi.com/v1/breeds'


response2 = requests.get(endpoint)

if response2.status_code == 200:
    data = response2.json()

    print(json.dumps(data, indent=4))

    for breed in data:
        if 'image' in breed and 'url' in breed['image']:
            print(f"Breed: {breed['name']}, Image URL: {breed['image']['url']}")

else:
    print(f"Failed to retrieve data. HTTP Status code: {response2.status_code}")
