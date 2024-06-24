#!/usr/bin/env python3

# This is taken from w3schools - learning about APIs

import json           # Handling JSON data from ISS API
import turtle         # Creating simple map
import requests # Fetching data from ISS API
import time           # Time-related functionality
import webbrowser     # Opening map in web browser
import geocoder       # Retrieving latitude and longitude

url = "http://api.open-notify.org/astros.json"

try:
    # Open API url
    response = requests.get(url)
    # Check for HTTP request errors
    response.raise_for_status()
    # Read data from url
    result = response.json()

    # Filter for only ISS astronauts
    iss_astronauts = [person for person in result['people'] if person['craft'] == 'ISS']
    # Filter for only Tiangong astronauts
    tiangong_astronauts = [person for person in result['people'] if person['craft'] == 'Tiangong']

        # TODO: create a crontab that will add info to a file. In that info is the date and the changes in astronauts. Basically: what was changed in the ISS or the Tiangong.

    # txt file for ISS
    file = open("iss.txt", "w")
    file.write(f"There are currently {len(iss_astronauts)} astronauts on the ISS: \n\n")   # change logic if you only want ISS
    
    for astronaut in iss_astronauts:
        file.write(f"{astronaut['name']} - on board\n")

    print("Data written to iss.txt successfully.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")

