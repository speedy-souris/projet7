#coding:utf-8
#!/usr/bin/env python

import requests

def get_api_data():
    request = requests.Session()
    url_api = "https://fr.wikipedia.org/w/api.php"
    data_params = {
        "format": "json",
        "list": "geosearch",
        "gscoord": "48.8975156|2.3833993",
        "gslimit": "10",
        "gsradius": "10000",
        "action": "query"
    }
    address_found = request.get(url=url_api, params=data_params)
    result = address_found.json()
    return result

if __name__ == '__main__':
    place = get_api_data()
    for address in place['query']['geosearch']:
        print(address['title'])
    
