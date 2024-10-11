import time
from geopy.geocoders import Nominatim
import logging
from plot_utils import add_space_before_second_uppercase
import pandas as pd

logging.basicConfig(level=logging.DEBUG)  # para ver el error

df = pd.read_csv("weatherAUS.csv")
locations = df['Location'].unique()


formatted_locations = [add_space_before_second_uppercase(location) for location in locations]
print(formatted_locations)

def get_location_coordinates():
    geolocator = Nominatim(user_agent="myGeocoderApp")
    loc_coordinates = {}

    for location, formatted_location in zip(locations, formatted_locations):
        coords = geolocator.geocode(formatted_location)
        if coords:
            loc_coordinates[location] = (coords.latitude, coords.longitude)
        else:
            print(location + " no fue encontrada.")

        # Se añade un retraso para evitar exceder los límites de solicitudes
        time.sleep(2)  # Espera 1 segundo entre solicitudes
    return loc_coordinates


import os.path
import json


def check_if_already_generated(file_path, generate_file):
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as f:
            try:
                file = generate_file()
                json.dump(file, f)
            except:
                print('API Error')
                os.remove(file_path)

    if os.path.isfile(file_path):
        with open(file_path) as f:
            ans = json.load(f)

    return ans


# coordinates = check_if_already_generated("coordinates.json", get_location_coordinates)
