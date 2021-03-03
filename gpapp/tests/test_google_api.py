#coding:utf-8
#!/usr/bin/env python

import urllib.request
from io import BytesIO
import json
from .. import googlemapsapi
from ..answersearch import KeyManagement

API_KEY = KeyManagement()
MAP_KEY = API_KEY.keys['map']
STATIC_KEY= API_KEY.keys['staticMap']
BAD_KEY = 0

def mock(result):
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
        demand1 = googlemapsapi.get_place_id_list('openClassRooms', MAP_KEY)
        demand2 = googlemapsapi.get_place_id_list('openClassRooms', BAD_KEY)
        demand3 = googlemapsapi.get_place_id_list('openClassRooms', STATIC_KEY)
        demand4 = googlemapsapi.get_place_id_list('rueopenClassRooms', MAP_KEY)
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
        mockreturn = mock('result_place_id1')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand1 == result_place_id1
        mockreturn = mock('result_place_id2')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand2 == result_place_id2
        mockreturn = mock('result_place_id3')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand3 == result_place_id3
        mockreturn = mock('result_place_id4')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand4 == result_place_id4

    # google map API test on address location
    def test_geolocal_address(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference of the requested address
        """
        place_id1 = 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
        place_id2 = 'c8'
        demand1 = googlemapsapi.get_address(place_id1, MAP_KEY)
        demand2 = googlemapsapi.get_address(place_id1, BAD_KEY)
        demand3 = googlemapsapi.get_address(place_id1, STATIC_KEY)
        demand4 = googlemapsapi.get_address(place_id2, MAP_KEY)
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
        mockreturn = mock('result_address1')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand1 == result_address1
        mockreturn = mock('result_address2')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand2 == result_address2
        mockreturn = mock('result_address3')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand3 == result_address3
        mockreturn = mock('result_address4')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand4 == result_address4

    # google map API test on map static
    def test_geolocal_static(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a image static
            containing the reference ID of the address asked
        """
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
        demand1 = googlemapsapi.get_static(address1, STATIC_KEY)
        demand2 = googlemapsapi.get_static(address1, BAD_KEY)
        demand3 = googlemapsapi.get_static(address1, MAP_KEY)
        demand4 = googlemapsapi.get_static(address2, STATIC_KEY)
        result_static1 = 'https://maps.googleapis.com/maps/api/staticmap?center='\
            f"{address1['address']['result']['formatted_address']}&zoom=18.5"\
            f'&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C'\
            f"{address1['address']['result']['geometry']['location']['lat']},"\
            f"{address1['address']['result']['geometry']['location']['lng']}"\
            f'&key={STATIC_KEY}'
        result_static2 = 'https://maps.googleapis.com/maps/api/staticmap?center='\
            f"{address1['address']['result']['formatted_address']}&zoom=18.5"\
            f'&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C'\
            f"{address1['address']['result']['geometry']['location']['lat']},"\
            f"{address1['address']['result']['geometry']['location']['lng']}"\
            f'&key={BAD_KEY}'
        result_static3 = 'https://maps.googleapis.com/maps/api/staticmap?center='\
            f"{address1['address']['result']['formatted_address']}&zoom=18.5"\
            f'&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C'\
            f"{address2['address']['result']['geometry']['location']['lat']},"\
            f"{address1['address']['result']['geometry']['location']['lng']}"\
            f'&key={MAP_KEY}'
        result_static4 = 'https://maps.googleapis.com/maps/api/staticmap?center='\
            f"{address2['address']['result']['formatted_address']}&zoom=18.5"\
            f'&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C'\
            f"{address2['address']['result']['geometry']['location']['lat']},"\
            f"{address2['address']['result']['geometry']['location']['lng']}"\
            f'&key={STATIC_KEY}'

        mockreturn = mock('result_static1')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand1 == result_static1
        mockreturn = mock('result_static2')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand2 == result_static2
        mockreturn = mock('result_static3')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand3 == result_static3
        mockreturn = mock('result_static4')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand4 == result_static4


if __name__ == "__main__":
    pass
