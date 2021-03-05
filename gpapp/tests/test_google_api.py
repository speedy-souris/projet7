#coding:utf-8
#!/usr/bin/env python

import urllib.request
from io import BytesIO
import json
from .. import googlemapsapi
from ..answersearch import KeyManagement


def get_api_data():
    api_key = KeyManagement()
    data  = {
        'map_key': api_key.keys['map'],
        'static_key': api_key.keys['staticMap'],
        'bad_key': 0,
        'url': 'https://maps.googleapis.com/maps/api/staticmap',
        'position': 'center=',
        'get_zoom': 'zoom=18.5',
        'get_size': 'size=600x300',
        'type_get_map': 'maptype=roadmap',
        'get_marker': 'markers=color:red%7Clabel:A%7C',
        'key_get_param': 'key='
    }
    return data

def get_url_static(address, key):
    data = get_api_data()
    url_static =\
        f"{data['url']}?{data['position']}"\
        f"{address['address']['result']['formatted_address']}"\
        f"&{data['get_zoom']}&{data['get_size']}&{data['type_get_map']}"\
        f"&{data['get_marker']}"\
        f"{address['address']['result']['geometry']['location']['lat']},"\
        f"{address['address']['result']['geometry']['location']['lng']}&"\
        f"{data['key_get_param']}{key}"
    return url_static
    
def get_mockreturn(result):
    def mockreturn(request):
        """
            Mock function on api object
        """
        return BytesIO(json.dumps(result).encode())
    return mockreturn

class TestApiGoogle:
    """
        management of APi parameters test 
    """
    # google map API test on place id location
    def test_geolocal_id(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference ID of the address asked
        """
        data = get_api_data()
        demand1 = googlemapsapi.get_place_id_list(
            'openClassRooms', data['map_key']
        )
        demand2 = googlemapsapi.get_place_id_list(
            'openClassRooms', data['bad_key']
        )
        demand3 = googlemapsapi.get_place_id_list(
        'openClassRooms', data['static_key']
        )
        demand4 = googlemapsapi.get_place_id_list(
        'rueopenClassRooms', data['map_key']
        )
        result_place_id1 = {
            'candidates': [{
                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
            }],
            'status' : 'OK'
        }
        result_place_id2 = {
            'candidates' : [],
            'error_message' : 'The provided API key is invalid.',
            'status' : 'REQUEST_DENIED'
        }
        result_place_id3 = {
            'candidates' : [],
            'error_message' : 'This API key is not authorized to use this service or API.',
            'status' : 'REQUEST_DENIED'
        }
        result_place_id4 = {
            'candidates': [],
            'status' : 'ZERO_RESULTS'
        }
        mockreturn = get_mockreturn('result_place_id1')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand1 == result_place_id1
        mockreturn = get_mockreturn('result_place_id2')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand2 == result_place_id2
        mockreturn = get_mockreturn('result_place_id3')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand3 == result_place_id3
        mockreturn = get_mockreturn('result_place_id4')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand4 == result_place_id4

    # google map API test on address location
    def test_geolocal_address(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference of the requested address
        """
        data = get_api_data()
        place_id1 = 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
        place_id2 = 'c8'
        
        demand1 = googlemapsapi.get_address(place_id1, data['map_key'])
        demand2 = googlemapsapi.get_address(place_id1, data['bad_key'])
        demand3 = googlemapsapi.get_address(place_id1, data['static_key'])
        demand4 = googlemapsapi.get_address(place_id2, data['map_key'])

        result_address1 = {
            'html_attributions': [],
            'result': {
                'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                'geometry': {
                    'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    'viewport': {
                        'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}
                    }
                }
            },
            'status': 'OK'
        }
        result_address2 = {
            'error_message' : 'The provided API key is invalid.',
           'html_attributions' : [],
           'status' : 'REQUEST_DENIED'
        }
        result_address3 = {
            'error_message' : 'This API key is not authorized to use this service or API.',
           'html_attributions' : [],
           'status' : 'REQUEST_DENIED'
        }
        result_address4 = {
            'html_attributions': [],
            'status': 'INVALID_REQUEST'
        }
        mockreturn = get_mockreturn('result_address1')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand1 == result_address1
        
        mockreturn = get_mockreturn('result_address2')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand2 == result_address2

        mockreturn = get_mockreturn('result_address3')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand3 == result_address3

        mockreturn = get_mockreturn('result_address4')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand4 == result_address4

    # google map API test on map static
    def test_geolocal_static(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a image static
            containing the reference ID of the address asked
        """
        data = get_api_data()
        address1 = {
            'address': {
                'result': {
                    'formatted_address': '10QuaidelaCharente,75019Paris,France',
                    'geometry': {
                        'location': {'lat': 48.8975156, 'lng': 2.3833993}
                    }
                }
            }
        }
        address2 = {
            'address': {
                'result': {
                    'formatted_address': 'rueopenClassRooms',
                    'geometry': {
                        'location': {'lat': 48.8975156, 'lng': 2.3833993}
                    }
                }
            }
        }
        demand1 = googlemapsapi.get_static(address1, data['static_key'])
        demand2 = googlemapsapi.get_static(address1, data['bad_key'])
        demand3 = googlemapsapi.get_static(address1, data['map_key'])
        demand4 = googlemapsapi.get_static(address2, data['static_key'])

        result_static1 = get_url_static(address1, data['static_key'])
        result_static2 = get_url_static(address1, data['bad_key'])
        result_static3 = get_url_static(address1, data['map_key'])
        result_static4 = get_url_static(address2, data['static_key'])

        mockreturn = get_mockreturn('result_static1')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand1 == result_static1
        mockreturn = get_mockreturn('result_static2')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand2 == result_static2
        mockreturn = get_mockreturn('result_static3')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand3 == result_static3
        mockreturn = get_mockreturn('result_static4')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand4 == result_static4


if __name__ == "__main__":
    pass
