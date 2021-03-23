#coding:utf-8
#!/usr/bin/env python
"""
    API result module
"""
import urllib.parse

from .googlemapsapi import GoogleMapAdressProcessing
from .wikimediaapi import WikiMediaAddressProcessing

class ReturnAllApis:
    """
        return of the googlemap and wikiMedia APIs algorithms
    """
    def __init__(self, user, address):
        self.user = user
        self.result_map_address = GoogleMapAdressProcessing(address)
        self.result_wiki_content = WikiMediaAddressProcessing(address)

    # address coordinate calculation
    def get_from_map_coordinates(self):
        """
            calculating the coordinates of the question asked to grandpy
            Vars :
                - parser_answer
                - place_id_dict
                - map_status
            creation of api google map coordinate address display setting
        """
        _user = self.user.user
        googlemap = self.result_map_address
        user_question = _user.get_question('parser')
        # keyword isolation for question
        parse_answer = urllib.parse.quote(user_question)
        place_id_dict = googlemap.get_from_url_placeid_api(parse_answer)
        # creation and test public key api google map
        try:
            place_id_dict['candidates'][0]['place_id']
        except IndexError:
            googlemap.map_status = {
                'address': {
                    'result': {
                        'formatted_address': '',
                        'geometry': {'location': {'lat': 0, 'lng': 0}}
                    },
                    'parser' : user_question
                },
                'history': ''
            }
        else:
            googlemap.map_status['address'] =\
                googlemap.get_from_url_address_api()
            googlemap.map_status['address']['parser'] = parse_answer
            googlemap.map_status['history'] = ''

    def get_from_wiki_response(self):
        """
            wikimedia address history display setting
        """
        result_wiki_list = self.result_map_address.map_status
        # ~ common_address_content =\
            # ~ self.result_wiki_content.get_from_common_string_creation()
        # ~ list_address_page_wiki =\
        wiki_page_content = self.result_wiki_content.get_from_page_url_api()
        result_wiki_list['history'] = wiki_page_content
        return result_wiki_list

# API return value
def get_from_map_status(user, question):
    """
        return value of APIS Google Map and Wiki Media
    """
    coordinates = ReturnAllApis(user, question)
    coordinates.get_from_map_coordinates()
    map_status = coordinates.get_from_wiki_response()
    return map_status


if __name__ == '__main__':
    pass
