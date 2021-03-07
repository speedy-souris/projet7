#coding:utf-8
#!/usr/bin/env python

import requests

class ApiGoogleMaps:
    """

    """
    def __init__(self):
        self.url_api = ''
        self.url_params = ''

    @staticmethod
    def get_api_urls():
        urls = {
            'url1': 'https://maps.googleapis.com/maps/api/place/findplacefromtext/',
            'url2': 'https://maps.googleapis.com/maps/api/place/details/',
            'url3': 'https://maps.googleapis.com/maps/api/staticmap'
        }
        return urls

    @staticmethod
    def get_api_data_placeid(title, key_api):
        data = {
            'format': 'json',
            'key': key_api,
            'input': title,
            'inputtype': 'textquery'
        }
        return data

    @staticmethod
    def get_api_data_address(placeid, key_api):
        data = {
            'format': 'json',
            'key': key_api,
            'placeid': placeid,
            'fields': 'formatted_address,geometry',
        }
        return data

    @staticmethod
    def get_api_data_static(address, localization, key_api):
        markers_data = f"color:red%7Clabel:A%7C{localization['lat']},\
                       {localisation['lng']}"
        data = {
            'key': key_api,
            'center': address['address']['result']['formatted_address'],
            'zoom': '18.5',
            'size': '600x300',
            'maptype': 'roadmap',
            'markers': markers_data
        }
        return data
    
    def get_url_placeid(self, address, key_api):
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
        self.url_params = self.get_api_data_placeid(address, key_api)
        urls_api = self.get_api_urls()
        self.url_api = urls_api['url1']
        request = requests.get(self.url_api, self.url_params)
        url_placeid = request.json()
        print(request)
        return request.json()
    
    def get_url_address(self, placeid, key_api):
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
        self.url_params = self.get_api_data_address(placeid, key_api)
        urls_api = self.get_api_urls()
        self.url_api = urls_api['url2']
        request = requests.get(self.url_api, self.url_params)
        url_address = request.json()
        return url_address
    
    def get_url_static(self, address, key_api):
        """
            Display of the static map at the user's request
        """
        address_data = address['address']['result']['formatted_address']
        localization = address['address']['result']['geometry']['location']
        self.url_params = self.get_api_data_static(
            address_data, localization, key_api
        )
        urls_api = self.get_api_urls()
        self.url_api = urls_api['url3']
        request = requests.get(self.url_api, self.url_params)
        url_static = request.json()
        return url_static


if __name__ == '__main__':
    from answersearch import KeyManagement

    keys_api = KeyManagement()
    key_map = keys_api.get_keys['map']
    api_google = ApiGoogleMaps()
    api_google.get_url_placeid('OpenClassrooms', key_map)
