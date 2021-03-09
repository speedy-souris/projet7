#coding:utf-8
#!/usr/bin/env python

import requests


class ApiWikiMedia:
    """
        management of wikimedia APIs settings
    """
    def __init__(self):
        self.url_api = 'https://fr.wikipedia.org/w/api.php'
        self.request = requests

    @staticmethod
    def get_localization_data(lat, lng):
        data = {
            'format': 'json',
            'list': 'geosearch',
            'gscoord': f'{lat}|{lng}',
            'gslimit': '10',
            'gsradius': '10000',
            'action': 'query'
        }
        return data

    @staticmethod
    def get_page_data(title):
        data = {
            'action': 'query',
            'titles': f'{title}',
            'prop': 'extracts',
            'formatversion': '2',
            'format': 'json',
            'exsentences': '5',
            'exlimit': '1',
            'explaintext': '1'
        }
        return data

    def get_url_json(self, params):
        request = self.request.get(url=self.url_api, params=params)
        url = request.json()
        return url

    def get_page_url(self, title):
        """
            wikipedia API (Wikimedia) history search
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
        """
        params = self.get_page_data(title)
        page_url = self.get_url_json(params)
        if page_url['query']['pages'][0]['extract'] != '':
            return page_url
        if page_url[3] != []:
            return page_url[3]
        else:
            return ['',[], [], []]

    def get_address_url(self, lat, lng):
        params = self.get_localization_data(lat, lng)
        address_url = self.get_url_json(params)
        return address_url


if __name__ == '__main__':
    pass
