#coding:utf-8
#!/usr/bin/env python

import urllib.request
import json


def get_api_data():
    data = {
        'url': 'https://fr.wikipedia.org/w/api.php',
        'action': 'action=query',
        'get_titles': 'titles=',
        'get_prop': 'prop=extracts',
        'get_version': 'formatversion=2',
        'get_format': 'format=json',
        'get_exsentences': 'exsentences=5',
        'get_exlimit': 'exlimit=1',
        'get_explaintext': 'explaintext=1'
    }
    return data

def get_url(title):
    data = get_api_data()
    url = f"{data['url']}?{data['action']}&{data['get_titles']}{title}"\
        f"&{data['get_prop']}&{data['get_version']}&{data['get_format']}"\
        f"&{data['get_exsentences']}&{data['get_exlimit']}"\
        f"&{data['get_explaintext']}"
    return url

# history search on wikimedia API
def get_history(search_history):
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
    print(f'\nsearch_histoty get history = {search_history}\n')
    # display history
    history_found = urllib.request.urlopen(get_url(search_history))
    result = json.loads(history_found.read().decode('utf8'))
    
    if result['query']['pages'][0]['extract'] != '':
        return result
    # replacing space by "% 20" in the string of characters
    # ~ history_encode = urllib.parse.quote(
        # ~ search_history['address']['parser']
    # ~ )
    # ~ # display history
    # ~ history_found = urllib.request.urlopen(get_url(history_encode))
    # ~ result = json.loads(history_found.read().decode('utf8'))
    # ~ if result[3] != []:
        # ~ return result[3]
    else:
        return ['',[], [], []]
