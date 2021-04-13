#coding:utf-8
#!/usr/bin/env python
"""
    API result module
"""
import urllib.parse
from . import googlemapsapi, wikimediaapi
from . import dataapi


class ReturnAllApis:
    """
        return of the googlemap and wikiMedia APIs algorithms
    """
    def __init__(self, user, address):
        self.user = user
        self.address = urllib.parse.quote(address)
        self.google_api = googlemapsapi
        self.wikimedia_api = wikimediaapi
        self.wikimedia_config = dataapi.ApiDataConfig()
        self.url_wikimedia = self.wikimedia_config.get_from_url_api()
        self.map_status = {}

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
        user = self.user
        google_api = self.google_api.GoogleMapsAddressProcessing()
        user_question = user.get_user_question('parser')
        place_id_dict = google_api.get_from_url_placeid_api(self.address)
        # creation and test public key api google map
        try:
            placeid = place_id_dict['candidates'][0]['place_id']
        except IndexError:
            self.map_status = {
                'address': '',
                'map': '',
                'parser' : '',
                'history': ''
            }
        else:
            result_map_address = google_api.get_from_url_address_api(placeid)
            address_map = result_map_address['result']['formatted_address']
            location_map = result_map_address['result']['geometry']['location']
            static_map =\
                google_api.get_from_url_static_api(address_map, location_map)
            self.map_status= {
                'address': address_map,
                'map': static_map,
                'parser': user_question,
                'history': '',
                'location': location_map
            }
        return self.map_status

    def get_from_wiki_response(self):
        """
            wikimedia address history display setting
        """
        map_coordinates = self.get_from_map_coordinates()
        address = map_coordinates['address']
        latitude = map_coordinates['location']['lat']
        longitude = map_coordinates['location']['lng']
        data_wiki =\
            self.wikimedia_api.WikiMediaAddressProcessing(latitude, longitude)
        list_pages_wiki = data_wiki.get_from_address_list_creation()
        address_content_compared =\
            self.wikimedia_api.ApiResultComparison(address, list_pages_wiki)
        common_list = address_content_compared.get_from_common_string_creation()
        url = self.url_wikimedia['url_api_wiki']
        params = data_wiki.get_from_page_data_api(common_list)
        pages_wiki =\
            self.wikimedia_config.get_from_url_json(url, params)
        try:
            pages_wiki['query']['pages'][0]['extract']
        except KeyError:
            pages_wiki = {
                'query': {
                    'pages': [
                    {
                        'extract': ''
                    }
                    ]
                }
            }
        self.map_status['history'] = pages_wiki['query']['pages'][0]['extract']
        return self.map_status

# API return value
def get_from_map_status(user, question):
    """
        return value of APIS Google Map and Wiki Media
    """
    coordinates = ReturnAllApis(user, question)
    map_status = coordinates.get_from_wiki_response()
    del map_status['location']
    return map_status


if __name__ == '__main__':
    pass
