#coding:utf-8
#!/usr/bin/env python

import urllib.request
import json

URL = 'https://maps.googleapis.com/maps/api/'
JSON = 'json?'
KEY_GET_PARAM = '&key='
FIND_PLACE_TEXT = 'place/findplacefromtext/'
INPUT_ADDRESS = 'input='
TYPE_GET_INPUT = '&inputtype=textquery'
DETAIL = 'place/details/'
PLACE_ID = 'placeid='
GET_FIELDS = '&fields=formatted_address,geometry'
STATIC_MAP = 'staticmap?'
POSITION = 'center='
GET_ZOOM = '&zoom=18.5'
GET_SIZE = '&size=600x300'
TYPE_GET_MAP = '&maptype=roadmap'
GET_MARKER = '&markers=color:red%7Clabel:A%7C'

# place_id search on Google Map API
def get_place_id_list(address, key_value):
    """
        Google map API place_id search function
    
    Resultat Ok
    {
       "candidates" : [
          {
             "place_id" : "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"
          }
       ],
       "status" : "OK"
    }
    API Key Invalid 
    {
       "candidates" : [],
       "error_message" : "The provided API key is invalid.",
       "status" : "REQUEST_DENIED"
    }
    Key API not allowed
    {
        "candidates": [],
        "error_message": "This API key is not authorized to use this service or API.",
        "status": "REQUEST_DENIED"
    }
    Address Invalid 
    {
       "candidates" : [],
       "status" : "ZERO_RESULTS"
    }
    """
    place_id = urllib.request.urlopen(
        f'{URL}{FIND_PLACE_TEXT}{JSON}{INPUT_ADDRESS}{address}{TYPE_GET_INPUT}'\
        f'{KEY_GET_PARAM}{key_value}'
    )
    result = json.loads(place_id.read().decode('utf8'))
    
    return result

# address on Google Map API
def get_address(place_id, key_value):
    """
        Google map API address search with place_id function
        Result OK
        {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}}}},
            'status': 'OK'
        }
        API Key Invalid
        {
           "error_message" : "The provided API key is invalid.",
           "html_attributions" : [],
           "status" : "REQUEST_DENIED"
        }
        Key API not allowed
        {
            "error_message": "This API key is not authorized to use this service or API.",
            "html_attributions": [],
            "status": "REQUEST_DENIED"
        }
        Place Id Invalid 
        {
           "html_attributions" : [],
           "status" : "INVALID_REQUEST"
        }
    """
    address_found = urllib.request.urlopen(
        f'{URL}{DETAIL}{JSON}{PLACE_ID}{place_id}{GET_FIELDS}'\
        f'{KEY_GET_PARAM}{key_value}'
    )
    result = json.loads(address_found.read().decode('utf8'))
    return result

# map static search on Google Map API
def get_static(address, key_value):
    """
        Display of the static map at the user's request
    """
    display_address = address['address']['result']['formatted_address']
    # longitude and latitude display
    localization =\
        address['address']['result']['geometry']['location']
    # ~ # display map
    display_map = f'{URL}{STATIC_MAP}{POSITION}{display_address}{GET_ZOOM}'\
        f"{GET_SIZE}{TYPE_GET_MAP}{GET_MARKER}{localization['lat']},"\
        f"{localization['lng']}{KEY_GET_PARAM}{key_value}"
    return display_map


if __name__ == '__main__':
    pass
