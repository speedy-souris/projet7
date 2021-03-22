#coding:utf-8
#!/usr/bin/env python

from copy import deepcopy

import dataapi
import googlemapsapi

class WikiMediaListAddressProcessing(dataapi.ApiWikiMedia):
    """
        creation of the address list of wikipedia pages
            - map_latitude
            - map_longitude
        generated by googlemap API
    """
    def __init__(self):
        super().__init__()
        self.coordinates = googlemapsapi.googlemapAdressProcessing()
        self._map_status = self.coordinates.get_from_url_placeid_api()
        _map_status = self._map_status
        print(_map_status)
        self._latitude = \
            _map_status['address']['result']['geometry']['location']['latitude']
        self._longitude =\
            _map_status['address']['result']['geometry']['location']['longitude']

    def get_from_address_list_creation(self):
        """
            common address list set found by wikimedia API
                - pages_wiki ==> wikimedia page address list set
                - common_address ==> set of wikimedia page address lists
        """
        latitude, longitude = self._latitude, self._longitude
        params = self.get_from_localization_data_api(latitude, longitude)
        address_url = self.get_from_url_json(params)
        common_address = [
            address_url['query']['geosearch'][page]['title'].split(' ')\
            for page in range(len(address_url['query']['geosearch']))
        ]
        return common_address

class WikiMediaCommonAddressProcessing(dataapi.ApiWikiMedia):
    """
        determination of the content
        of the common wikimedia address
        at the address found by googlemap API
    """
    def __init__(self, list_address=WikiMediaListAddressProcessing()):
        super().__init__()
        self._googlemap_address = list_address._map_status['address']
        self.common_address_list = list_address.get_from_address_list_creation()

    def get_from_list_address_convertion(self):
        address = self._googlemap_address
        address_convert = address.lower().replace(',', '')
        converted_address_list = address_convert.split(' ')
        return converted_address_list

    def get_from_common_string_creation(self):
        """
            comparison of the result of the wikimedia API
            with the address of the googlemap API found
                - common_address ==> common address list
                - common_word    ==> common word list
                - word           ==> common address
        """
        common_address = []
        common_word = []
        compared_content = ''
        common_address_list = self.common_address_list
        _googlemap_address = self._googlemap_address
        for index in range(len(common_address_list)):
            for w in range(len(common_address_list[index])):
                if common_address_list[index][w].lower()\
                    in _googlemap_address:
                    common_word.append(common_address_list[index][w])
            common_address.append(deepcopy(common_word))
            common_word = []
        for i in range(len(common_address)):
            if (len(word) < len(common_address[i])):
                compared_content = common_address[i]
        compared_content = ' '.join(compared_content)
        return compared_content

class WikiMediaAddressHistoryProcessing(dataapi.ApiWikiMedia):
    """
        display of the history for the googlemap address found
    """
    def __init__(self, common_content=WikiMediaCommonAddressProcessing()):
        super().__init__()
        self.content = common_content.get_from_common_string_creation()

    def get_from_page_url_api(self):
        """
            wikipedia API (Wikimedia) history search
            Result Ok
            {
                "batchcomplete": True,
                "query": {
                    "pages": [
                        {
                            "pageid": 4338589,
                            "ns": 0,
                            "title": "OpenClassrooms",
                            "extract": "OpenClassrooms est un site web de formation..."
                        }
                    ]
                }
            }
            wrong result
            {
                "batchcomplete": True,
                "query": {
                    "normalized": [
                        {
                            "fromencoded": False,
                            "from": "rueOpenClassrooms",
                            "to": "RueOpenClassrooms"
                        }
                    ],
                    "pages": [
                        {
                            "ns": 0,
                            "title": "RueOpenClassrooms",
                            "missing": True
                        }
                    ]
                }
            }
        """
        title = self.content
        params = self.get_from_page_data_api(title)
        page_url = self.get_from_url_json(params)
        try:
            page_url['query']['pages'][0]['extract'] != ''
        except KeyError:
            page_url = {
                'query': {
                    'pages': [
                        {
                            'missing': True
                        }
                    ]
                }
            }
        return page_url


if __name__ == '__main__':
    pass
