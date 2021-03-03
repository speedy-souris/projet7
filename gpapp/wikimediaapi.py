#coding:utf-8
#!/usr/bin/env python

import urllib.request
import json


URL = 'https://fr.wikipedia.org/w/api.php?'
ACTION = 'action='
LIST = 'list=search'
SRSEARCH = 'srsearch'
QUERY = 'query'
SEARCH = 'opensearch&search='
FORMAT = '&format=json'

# history search on wikimedia API
def get_history(self, search_history):
    """
        wikipedia API (Wikimedia) history search
    """
    # replacing space by "% 20" in the string of characters
    history_encode = urllib.parse.quote(
        search_history['address']['result']['formatted_address']
    )
    # display history
    history_found = urllib.request.urlopen(
        'https://fr.wikipedia.org/w/api.php?action=opensearch&search='\
        f'{history_encode}&format=json'
    )
    result = json.loads(history_found.read().decode('utf8'))
    print(f'\nresult = {result[3]}\n')
    if result[3] != []:
        return result
    # replacing space by "% 20" in the string of characters
    history_encode = urllib.parse.quote(
        search_history['address']['parser']
    )
    # display history
    history_found = urllib.request.urlopen(
        'https://fr.wikipedia.org/w/api.php?action=opensearch&search='\
        f'{history_encode}&format=json'
    )
    result = json.loads(history_found.read().decode('utf8'))
    if result[3] != []:
        return result[3]
    else:
        return ['',[], [], []]
