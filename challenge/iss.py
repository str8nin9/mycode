#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    time = resp['timestamp']
    date = datetime.datetime.fromtimestamp(time)
    lat = resp["iss_position"]["latitude"]
    lon = resp["iss_position"]["longitude"]
    coord_tuple = (lat, lon)
    city = rg.search(coord_tuple)
    print(f'Current Location of the ISS on {date}: \nlon: {lon}\nlat: {lat}')
    print(f'City, Country: {city[0]["name"]}, {city[0]["cc"]}')
if __name__ == "__main__":
    main()
