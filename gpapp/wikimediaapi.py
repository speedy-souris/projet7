#coding:utf-8
#!/usr/bin/env python

import requests


class ApiWikiMedia:
    """
        management of wikimedia APIs settings
    """
    def __init__(self):
        self.url_api = 'https://fr.wikipedia.org/w/api.php'
        self.request = requests.Session()

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

    # ~ # history search on wikimedia API
    # ~ def get_history(search_history):
        # ~ """
            # ~ wikipedia API (Wikimedia) history search
            # ~ {
                # ~ "batchcomplete": True,
                # ~ "query": {
                    # ~ "pages": [
                        # ~ {
                            # ~ "pageid": 4338589,
                            # ~ "ns": 0,
                            # ~ "title": "OpenClassrooms",
                            # ~ "extract": "OpenClassrooms est un site web de formation..."
                        # ~ }
                    # ~ ]
                # ~ }
            # ~ }
        # ~ """
        # ~ # display history
        # ~ history_found = urllib.request.urlopen(get_url(search_history))
        # ~ result = json.loads(history_found.read().decode('utf8'))
        
        # ~ if result['query']['pages'][0]['extract'] != '':
            # ~ return result
        # ~ # replacing space by "% 20" in the string of characters
        # ~ history_encode = urllib.parse.quote(
            # ~ search_history['address']['parser']
        # ~ )
        # display history
        # ~ history_found = urllib.request.urlopen(get_url(history_encode))
        # ~ result = json.loads(history_found.read().decode('utf8'))
        # ~ if result[3] != []:
            # ~ return result[3]
        # ~ else:
            # ~ return ['',[], [], []]

if __name__ == '__main__':
    # ~ api_wiki = ApiWikiMedia()
    # ~ address = api_wiki.get_page_url('OpenClassrooms')
    # ~ print(address['query']['pages'][0]['extract'])
    pass
