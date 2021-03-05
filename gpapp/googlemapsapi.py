#coding:utf-8
#!/usr/bin/env python

import urllib.request
import json

def api_data():
    data = {
        'url' = 'https://maps.googleapis.com/maps/api/',
        'json' = 'json',
        'key_get_param' = 'key=',
        'find_place_text' = 'place/findplacefromtext/',
        'input_address' = 'input=',
        'type_get_input' = 'inputtype=textquery',
        'detail' = 'place/details/',
        'place_id' = 'placeid=',
        'get_fields' = 'fields=formatted_address,geometry',
        'static_map' = 'staticmap',
        'position' = 'center=',
        'get_zoom' = 'zoom=18.5',
        'get_zoom' = 'size=600x300',
        'type_get_map' = 'maptype=roadmap',
        'get_marker' = 'markers=color:red%7Clabel:A%7C'
    }

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
    data = api_data()
    place_id = urllib.request.urlopen(
        f"{data['url']}{data['find_place_text']}{data['json']}?"\
        f"{data['input_address']}{address}&{data['type_get_input']}"\
        f"&{data['key_get_param']}{key_value}"
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
    data = api_data()
    address_found = urllib.request.urlopen(
        f"{data['url']}{data['detail']}{data['json']}?{data['place_id']}"\
        f"{place_id}&{data['get_fields']}&{data['key_get_param']}{key_value}"
    )
    result = json.loads(address_found.read().decode('utf8'))
    return result

# map static search on Google Map API
def get_static(address, key_value):
    """
        Display of the static map at the user's request
    """
    data = api_data()
    display_address = address['address']['result']['formatted_address']
    # longitude and latitude display
    localization =\
        address['address']['result']['geometry']['location']
    # ~ # display map
    display_map = f"{data['url']}{data['static_map']}?{data['position']}"\
    f"{display_address}&{data['get_zoom']}&{GET_SIZE}&{TYPE_GET_MAP}"\
    f"&{GET_MARKER}{localization['lat']},{localization['lng']}&{KEY_GET_PARAM}"\
    f'{key_value}'

    return display_map 


if __name__ == '__main__':
    pass
