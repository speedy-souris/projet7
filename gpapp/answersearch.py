#coding:utf-8
#!/usr/bin/env python

import os
import urllib.parse

from .googlemapsapi import ApiGoogleMaps
# ~ from .wikimediaapi import ApiWikiMedia


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
                objet google map api
                objet key api google
        """
        self.user = user
        self.api_google = ApiGoogleMaps()
        self.api_wiki = ApiWikiMedia()
        self.map_status = {}
        self.keyManagement = KeyManagement()
        self.keyMap = self.keyManagement.get_keys['map']
        self.keyStatic = self.keyManagement.get_keys['staticMap']

    def import_params(self):
        params = {
            'api_google': self.api_google,
            'api_wiki': self.api_wiki
        }
        return params

    # address coordinate calculation
    def map_coordinates(self, api_google):
        """
            calculating the coordinates of the question asked to grandpy
            Vars :
                - parser_answer
                - place_id_dict
                - map_status
            creation of api google map coordinate address display setting
            and wikipedia address history display setting
        """
        user_question = self.user.get_question('parser')
        api_key = self.keyMap
        
        # keyword isolation for question
        parse_answer = urllib.parse.quote(user_question)
        place_id_dict = api_google.get_url_placeid(parse_answer, api_key)
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
                    'parser' : user_question
                }
            }
        else:
            self.map_status['address'] = api_google.get_url_address(
                place_id, api_key
            )
            self.map_status['address']['parser'] = parse_answer

        map_status = self.map_status
        return map_status

    # API return value
    def get_map_status(self):
        """
            return value of APIS Google Map and Wiki Media
        """
        choice_api = self.import_params()
        api_google = choice_api['api_google']
        api_wiki = choice_api['api_wiki']

        location_map = self.map_coordinates(api_google)
        self.map_status['map'] = api_google.get_url_static(
            location_map, self.keyStatic
        )
        # ~ self.map_status['history'] = api_wiki.get_history(location_map)

        map_status = self.map_status
        return map_status


if __name__ == '__main__':
    pass
