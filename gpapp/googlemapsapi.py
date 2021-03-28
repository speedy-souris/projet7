#coding:utf-8
#!/usr/bin/env python
"""
    GoogleMap API module
"""
from .dataapi import ApiGoogleMaps, ApiDataConfig

class GoogleMapsAddressProcessing:
    """
        determining the location
        of the address user request
    """
    def __init__(self, address):
        """
            Initialization
            objet key api google
        """
        self.api_data = ApiGoogleMaps()
        self.api_config = ApiDataConfig()
        self.map_status = {}
        self.address = address

    def get_from_url_placeid_api(self, address, url):
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
        params = self.api_data.get_from_data_placeid_api(address=address)
        placeid_url = self.api_config.get_from_url_json(url=url, params=params)
        return placeid_url

    def get_from_url_address_api(self):
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
        placeid = self.get_from_url_placeid_api()
        print(f'\nplaceid (googleMap) = {placeid}\n')
        params = self.api_data.get_from_data_address_api(placeid)
        print(f'params (googleMap) = {params}\n')
        address_url = self.api_config.get_from_url_json(self.url_api2, params)
        print(f'address (googleMap) = {address_url}')
        return address_url

    def get_from_url_static_api(self, address):
        """
            Display of the static map at the user's request
        """
        address_data = address['result']['formatted_address']
        localization = address['result']['geometry']['location']
        params = self.api_data.get_from_data_static_api(address_data, localization)
        static_address = self.request.get(self.url_api3, params=params)
        static_url = static_address.json()
        return static_url


if __name__ == '__main__':
    pass
