#coding:utf-8
#!/usr/bin/env python

import requests


class ApiGoogleMaps:
    """
        management of Google APIs settings
    """
    def __init__(self):
        self.url_api1 =\
            'https://maps.googleapis.com/maps/api/place/findplacefromtext/'
        self.url_api2 = 'https://maps.googleapis.com/maps/api/place/details/'
        self.url_api3 = 'https://maps.googleapis.com/maps/api/staticmap'
        self.request = requests.Session()

    @staticmethod
    def get_data_placeid_api(title, key_api):
        data = {
            'format': 'json',
            'key': f'{key_api}',
            'input': f'{title}',
            'inputtype': 'textquery'
        }
        return data

    @staticmethod
    def get_data_address_api(placeid, key_api):
        data = {
            'format': 'json',
            'key': f'{key_api}',
            'placeid': f'{placeid}',
            'fields': 'formatted_address,geometry',
        }
        return data

    @staticmethod
    def get_data_static_api(address, localization, key_api):
        markers_data = f"color:red%7Clabel:A%7C{localization['lat']},\
                       {localisation['lng']}"
        data = {
            'key': f'{key_api}',
            'center': f"{address['address']['result']['formatted_address']}",
            'zoom': '18.5',
            'size': '600x300',
            'maptype': 'roadmap',
            'markers': f'{markers_data}'
        }
        return data

    def get_url_json(self, params, url):
        request = self.request.get(url=url, params=params)
        url = request.json()
        print(f'\nrequest.text = {request.text}\n')
        return url

    def get_url_placeid_api(self, address, key_api):
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
        params = self.get_data_placeid_api(address, key_api)
        placeid_url = self.get_url_json(params, self.url_api1)
        return placeid_url
    
    def get_url_address_api(self, placeid, key_api):
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
        params = self.get_data_address_api(placeid, key_api)
        address_url = self.get_url_json(params, self.url_api2)
        return address_url
    
    def get_url_static_api(self, address, key_api):
        """
            Display of the static map at the user's request
        """
        address_data = address['address']['result']['formatted_address']
        localization = address['address']['result']['geometry']['location']
        params = self.get_data_static_api(
            address_data, localization, key_api
        )
        static_url = self.get_url_json(params, self.url_api3)
        return static_url


if __name__ == '__main__':
    # ~ from answersearch import KeyManagement

    # ~ keys_api = KeyManagement()
    # ~ key_map = keys_api.get_keys['map']
    # ~ api_google = ApiGoogleMaps()
    # ~ api_google.get_url_placeid('OpenClassrooms', key_map)
    pass
