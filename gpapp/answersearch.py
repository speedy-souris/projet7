#coding:utf-8
#!/usr/bin/env python

import os
import json
import urllib.request, urllib.parse
from . import googlemapsapi, wikimediaapi


class KeyManagement:
    """
        API Private Key and Constants Management :
        local (development) / external (production)
            keys()
                - key_value['map']         ==> KEY_API_MAP / HEROKU_KEY_API_MAP
                - key_value['staticMap']   ==> KEY_API_STATIC_MAP / HEROKU_KEY_API_STATIC_MAP
                - key_value['status_prod'] ==> True / False
    """
    def __init__(self):
        """
            API Key initialization 
        """
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
                'staticMap': os.getenv('KEY_API_STATIC_MAP'),
                'status_prod': False
            }
        # keys for online use (Prod)
        else:
            self.key_value = {
                'map': os.getenv('HEROKU_KEY_API_MAP'),
                'staticMap': os.getenv('HEROKU_KEY_API_STATIC_MAP'),
                'status_prod': True
            }
        return self.key_value

class Research:
    """
        class for managing the internal API process
        Google Map and wikimedia
    """
    def __init__(self, user):
        """
            Initialization
                objet user
                objet datadiscussion
        """
        self.user = user
        # ~ self.dataDiscussion = dataDiscussion
        self.map_status = {}
        self.keyManagement = KeyManagement()
        self.keyMap = self.keyManagement.get_keys['map']
        self.keyStatic = self.keyManagement.get_keys['staticMap']

    # address coordinate calculation
    def map_coordinates(self):
        """
            calculating the coordinates of the question asked to grandpy
            Vars :
                - parser_answer
                - place_id_dict
                - map_status
            creation of api google map coordinate address display setting
            and wikipedia address history display setting
        """
        # keyword isolation for question
        question = self.user.question('parser')
        parse_answer = urllib.parse.quote(question)
        place_id_dict = googlemapsapi.get_place_id_list(parse_answer, self.keyMap)
        # creation and test public key api google map
        try:
            place_id = place_id_dict['candidates'][0]['place_id']
        except IndexError:
            self.map_status = {
                'address': {
                    'result': {
                        'formatted_address': '',
                        'geometry': {'location': {'lat': 0, 'lng': 0}}
                    },
                    'parser' : question
                }
            }
        else:
            self.map_status['address'] = googlemapsapi.get_address(
                place_id, self.KeyMap
            )
            self.map_status['address']['parser'] = parse_answer
        return self.map_status

    # API return value
    def get_map(self):
        """
            return value of APIS Google Map and Wiki Media
        """
        location_map = self.map_coordinates()
        self.map_status['map'] = googlemapsapi.get_static(
            location_map, self.keyStatic
        )
        self.map_status['history'] = wikimediaapi.get_history(location_map)
        return self.map_status


if __name__ == '__main__':
    pass
