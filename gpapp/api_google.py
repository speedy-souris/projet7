#coding:utf-8
#!/usr/bin/env python

import requests

def get_requests():
    request = {
        'url': 'https://fr.wikipedia.org/w/api.php',
        'session': requests.Session()
    }
    return request

def get_api_title(lat, lng):
    data = {
        'format': 'json',
        'list': 'geosearch',
        'gscoord': f'{lat}|{lng}',
        'gslimit': '10',
        'gsradius': '10000',
        'action': 'query'
    }
    return data
    
def get_api_page(title):
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

def get_url(title):
    data = get_api_page(title)
    request_data = get_requests()
    url_api = request_data['url']
    request = request_data['session']
    page_found = request.get(url=url_api, params=data)
    return page_found.json()

def get_url_place():
    data = get_api_title(48.8975156, 2.3833993)
    request_data = get_requests()
    url_api = request_data['url']
    request = request_data['session']
    address_found = request.get(url=url_api, params=data)
    return address_found.json()

if __name__ == '__main__':
    address = get_url_place()
    for title in (address['query']['geosearch']):
        if title['pageid'] == 3120618:
            result = get_url(title['title'])
            print(result['query']['pages'][0]['extract'])
