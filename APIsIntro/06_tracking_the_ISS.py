#!/usr/bin/env python3

# This is taken from w3schools - learning about APIs
# TODO: create a crontab that will add info to a file. In that info is the date and the changes in astronauts. Basically: what was changed in the ISS or the Tiangong.

import json           # Handling JSON data from ISS API
import turtle         # Creating simple map
import requests # Fetching data from ISS API
import time           # Time-related functionality
import webbrowser     # Opening map in web browser
import geocoder       # Retrieving latitude and longitude

url = "http://api.open-notify.org/astros.json"

try:
    # Open API url; check got HTTP request errors; read data from url
    response = requests.get(url)
    response.raise_for_status()
    result = response.json()

    # Filter for ISS astronauts; and for Tiangong astronauts
    iss_astronauts = [person for person in result['people'] if person['craft'] == 'ISS']
    tiangong_astronauts = [person for person in result['people'] if person['craft'] == 'Tiangong']

    # txt file for ISS and txt file for Tiangong
    fileISS = open("iss.txt", "w")
    fileISS.write(f"There are currently {len(iss_astronauts)} astronauts on the ISS: \n\n")
    for astronaut in iss_astronauts:
        fileISS.write(f"{astronaut['name']} - on board\n")
    print("ISS astronaut data written to iss.txt successfully.")

    fileTian = open("tiangong.txt", "w")
    fileTian.write(f"There are currently {len(tiangong_astronauts)} astronauts on the Tiangong: \n\n")
    for astronaut in tiangong_astronauts:
        fileTian.write(f"{astronaut['name']} - on board\n")
    print("Tiangong astronaut data written to tiangong.txt successfully.")

    # Getting our current longitude and latitude
    g = geocoder.ip('me')
    fileISS.write(f"\nYour current lat / long is: {str(g.latlng)}")
    fileISS.close()
    webbrowser.open("iss.txt")

    # Setting up the world map
    screen = turtle.Screen()
    screen.setup(width=1280, height=720)
    screen.setworldcoordinates(-180, -90, 180, 90)

    # world map image
    screen.bgpic("images/map.gif")

    # Setting up the ISS turtle
    screen.register_shape("images/iss.gif")
    iss = turtle.Turtle()
    iss.shape("images/iss.gif")
    iss.setheading(45)
    iss.penup()

    while True:

        # Current status of the ISS in real-time
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()

        # Extract the ISS location
        location = result["iss_position"]
        lat = float(location["latitude"])
        lon = float(location["longitude"])

        # Output coordinates to the terminal
        print(f"\nLatitude: {str(lat)}")
        print(f"\nLongitude: {str(lon)}")

        # Update the ISS location on the map
        iss.goto(lon, lat)

        # Refresh every 5 seconds
        time.sleep(5)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    time.sleep(5)


