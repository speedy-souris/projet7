#coding:utf-8
#!/usr/bin/env python

import requests


def get_requests():
    request = {
        'url1': 'https://maps.googleapis.com/maps/api/place/findplacefromtext/',
        'url2': 'https://maps.googleapis.com/maps/api/place/details/',
        'url3': 'https://maps.googleapis.com/maps/api/staticmap',
        'session': requests.Session()
    }
    return request

def get_api_data_placeid(title, key_api):
    data = {
        'format': 'json',
        'key': f'{key_api}',
        'input': f'{title}',
        'inputtype': 'textquery'
    }
    return data

def get_api_data_address(placeid, key_api):
    data = {
        'format': 'json',
        'key': f'{key_api}',
        'placeid': f'{placeid}',
        'fields': 'formatted_address,geometry',
    }
    return data

def get_api_data_static(address, localization, key_api):
    data = {
        'key': f'{key_api}'
        'center': f"{address['address']['result']['formatted_address']}",
        'zoom': '18.5',
        'size': '600x300',
        'maptype': 'roadmap',
        'markers': f"color:red%7Clabel:A%7C{localization['lat']},\
                   {localisation['lng']}"
    }
    return data

def get_url_placeid(address, key_api):
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
    data = get_api_data_placeid(address, key_api)
    request_data = get_requests()
    url_api = request_data['url1']
    request = request_data['session']
    placeid_found = request.get(url=url_api, params=data)
    url_placeid = placeid_found.json()
    return url_placeid

def get_url_address(placeid, key_api):
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
    data = get_api_data_address(placeid, key_api)
    request_data = get_requests()
    url_api = request_data['url2']
    request = request_data['session']
    address_found = request.get(url=url_api, params=data)
    url_address = address_found.json()
    return url_address

def get_url_static(address, key_api):
    """
        Display of the static map at the user's request
    """
    address_data = address['address']['result']['formatted_address']
    localization = address['address']['result']['geometry']['location']
    data = get_api_data_static(address_data, localization, key_api)
    request_data = get_requests()
    url_api = request_data['url3']
    request = request_data['session']
    static_found = request.get(url=url_api, params=data)
    url_static = static_found.json()
    return url_static


if __name__ == '__main__':
    pass
