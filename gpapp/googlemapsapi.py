#coding:utf-8
#!/usr/bin/env python
"""
    GoogleMap API module
"""
import requests
from .dataapi import ApiDataGoogleMaps, ApiDataConfig


class GoogleMapsAddressProcessing(ApiDataGoogleMaps, ApiDataConfig):
    """
        determining the location
        of the address user request
    """
    def __init__(self):
        """
            Initialization
            objet key api google
        """
        ApiDataGoogleMaps.__init__(self)
        ApiDataConfig.__init__(self)
        self.url_api = self.get_from_url_api()
        self.map_key = self.get_keys

    def get_from_url_placeid_api(self, address):
        """
            Google map API place_id search function

        Result Ok
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
        map_key = self.map_key['map']
        url_placeid_api = self.url_api['url_api_google1']
        params = self.get_from_data_placeid_api(address, map_key)
        result_placeid = self.get_from_url_json(url_placeid_api, params)
        return result_placeid

    def get_from_url_address_api(self, placeid):
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
        map_key = self.map_key['map']
        url_address_api = self.url_api['url_api_google2']
        params = self.get_from_data_address_api(placeid, map_key)
        result_address = self.get_from_url_json(url_address_api, params)
        return result_address

    def get_from_url_static_api(self, address, localization):
        """
            Display of the static map at the user's request
        """
        static_key = self.map_key['static_map']
        url_static_api = self.url_api['url_api_google3']
        params =\
            self.get_from_data_static_api(address, localization, static_key)
        map_static = requests.get(url=url_static_api, params=params)
        return map_static

if __name__ == '__main__':
    pass
