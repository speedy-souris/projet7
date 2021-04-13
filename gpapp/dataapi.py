#coding:utf-8
#!/usr/bin/env python
"""
    API internal data processing module
"""
import os
import requests


class ApiDataConfig:
    """
        API data configuration
    """
    def __init__(self):
        self.key_value = {}

    @property
    def get_keys(self):
        """
            management of environment variables
            local and online
                - key_value["map"]         ==> =|
                - key_value["staticMap"]   ==> =|- private keys for Google APIs
                                                  (local or online)
                - key_value["status_prod"] ==> boolean for data database
                                              data_dataion method
        """
        # keys for local use (Dev)
        if os.environ.get('HEROKU_KEY_API_MAP') is None:
            self.key_value = {
                'map': os.getenv('KEY_API_MAP'),
                'static_map': os.getenv('KEY_API_STATIC_MAP'),
                'status_prod': False
            }
        # keys for online use (Prod)
        else:
            self.key_value = {
                'map': os.getenv('HEROKU_KEY_API_MAP'),
                'static_map': os.getenv('HEROKU_KEY_API_STATIC_MAP'),
                'status_prod': True
            }
        return self.key_value

    @staticmethod
    def get_from_url_json(url, params):
        """
            conversion of the address found in JSON format
        """
        request = requests.get(url, params)
        url = request.json()
        return url

    @staticmethod
    def get_from_url_api():
        """
            creation of API urls
        """
        url = {
            'url_api_wiki': 'https://fr.wikipedia.org/w/api.php',
            'url_api_google1':\
                'https://maps.googleapis.com/maps/api/place/findplacefromtext/json',
            'url_api_google2':\
                'https://maps.googleapis.com/maps/api/place/details/json',
            'url_api_google3': 'https://maps.googleapis.com/maps/api/staticmap' 
        }
        return url

class ApiDataGoogleMaps:
    """
        management of Google APIs settings
    """
    @staticmethod
    def get_from_data_placeid_api(title, key):
        """
            determining placeid for the address found
        """
        data = {
            'input': f'{title}',
            'inputtype': 'textquery',
            'key': f'{key}'
        }
        return data

    @staticmethod
    def get_from_data_address_api(placeid, key):
        """
            determining the localized address for the found placeid
        """
        data = {
            'placeid': f'{placeid}',
            'fields': 'formatted_address,geometry',
            'key': f'{key}'
        }
        return data

    @staticmethod
    def get_from_data_static_api(address, localization, key):
        """
            determination of the static map for the address found
        """
        markers_data =\
            f"color:red|label:A|{localization['lat']},"\
            f"{localization['lng']}"
        data = {
            'center': f'{address}',
            'zoom': '18.5',
            'size': '600x300',
            'maptype': 'roadmap',
            'markers': f'{markers_data}',
            'key': f'{key}'
        }
        return data

class ApiDataWikiMedia:
    """
        management of wikimedia APIs settings
    """
    def __init__(self):
        self.url_api = 'https://fr.wikipedia.org/w/api.php'

    @staticmethod
    def get_from_localization_data_api(lat, lng):
        """
            data for wiki page localization url
        """
        data = {
            'action': 'query',
            'list': 'geosearch',
            'gscoord': f'{lat}|{lng}',
            'gslimit': '10',
            'gsradius': '10000',
            'format': 'json'
        }
        return data

    @staticmethod
    def get_from_page_data_api(title):
        """
            data for wiki page content url
        """
        data = {
            'action': 'query',
            'titles': f'{title}',
            'prop': 'extracts',
            'formatversion': '2',
            'exsentences': '5',
            'exlimit': '1',
            'explaintext': '1',
            'format': 'json'
        }
        return data
