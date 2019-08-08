#!/usr/bin/env python
import json
import urllib.request, urllib.parse


from config import key_API_MAP, address_default
from config import placeId_default

# place_id search on Google Map API
def get_place_id(key=key_API_MAP, address=address_default):
    """
    Google map API place_id search function
    """

    address_encode = urllib.parse.quote(address)

    place_id = urllib.request.urlopen(
    "https://maps.googleapis.com/maps/api/place/findplacefromtext/"\
    +"json?input={}&inputtype=textquery&key={}".format(address_encode, key))

    result = json.loads(place_id.read().decode("utf8"))

    return result

# place_id search on Google Map API
def get_address(key=key_API_MAP, place_id=placeId_default):
    """
    Google map API address search with place_id function
    """

    address_found= urllib.request.urlopen(
    "https://maps.googleapis.com/maps/api/place/details/"\
    +"json?placeid={}&fields=formatted_address&key={}".format(place_id, key))

    result = json.loads(address_found.read().decode("utf8"))

    return result

if __name__ == "__main__":

    test = get_place_id()
    print(test)
    test2 = get_address()
    print(test2)
