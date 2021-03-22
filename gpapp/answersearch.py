#coding:utf-8
#!/usr/bin/env python

import urllib.parse

import googlemapsapi
import wikimediaapi

class ReturnAllApis:
    """
        return of the googlemap and wikiMedia APIs algorithms
    """
    def __init__(self, user, address):
        self.address = address
        self.user = user
        self.result_map_address = googlemapsapi.googlemapAdressProcessing()
        self.result_wiki_list = wikimediaapi.WikiMediaListAddressProcessing()
        self.result_wiki_content =\
            wikimediaapi.WikiMediaCommonAddressProcessing()
        self.result_wiki_history =\
            wikimediaapi.WikiMediaAddressHistoryProcessing()

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
        _googlemap = self.result_map_address
        user_question = _user.get_question('parser')
        # keyword isolation for question
        parse_answer = urllib.parse.quote(user_question)
        place_id_dict = _googlemap.get_from_url_placeid_api(parse_answer)
        # creation and test public key api google map
        try:
            place_id = place_id_dict['candidates'][0]['place_id']
        except IndexError:
            _googlemap.map_status = {
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
            _googlemap.map_status['address'] =\
                _googlemap.get_from_url_address_api(place_id)
            _googlemap.map_status['address']['parser'] = parse_answer
            _googlemap.map_status['history'] = ''

    def get_from_wiki_response(self):
        """
            wikimedia address history display setting
        """
        latitude, longitude, address =\
            self.result_wiki_list.latitude,\
            self.result_wiki_list.longitude,\
            self.address
        list_address_page_wiki =\
            self.result_wiki_list.get_from_address_list_creation()
        wiki_common_address =\
            self.result_common_content.get_from_common_list_creation()
        wiki_page_content = self.result_wiki_history.get_from_page_url_api()
        self.result_wiki_list['history'] = wiki_page_content

# API return value
def get_from_map_status(user):
    """
        return value of APIS Google Map and Wiki Media
    """
    coordinates = ReturnAllApis(user)
    coordinates.get_from_map_coordinates()
    map_status = coordinates.get_from_wiki_response()
    return map_status.result_list_wiki.map_status


if __name__ == '__main__':
    pass
