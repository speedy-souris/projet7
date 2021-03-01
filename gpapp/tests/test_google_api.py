#coding:utf-8
#!/usr/bin/env python

from .. import googlemapsapi
from ..answersearch import KeyManagement
import urllib.request
from io import BytesIO
import json

# Google API test
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
        api_key = KeyManagement()
        map_key = api_key.keys['map']
        demand = googlemapsapi.get_place_id_list('openClassRooms', map_key)
        result_place_id = {
            'candidates': [{
                'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
            }],
            'status' : 'OK'
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_place_id).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand == result_place_id

    # google map API test on place id location with a bab key
    def test_geolocal_bad_key(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference ID of the address asked
            with a bad key
        """
        api_key = KeyManagement()
        map_key = 0
        demand = googlemapsapi.get_place_id_list('openClassRooms', map_key)
        result_place_id = {
            'candidates' : [],
            'error_message' : 'The provided API key is invalid.',
            'status' : 'REQUEST_DENIED'
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_place_id).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand == result_place_id

    # google map API test on place id location with a key not allowed
    def test_geolocal_not_authorized(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference ID of the address asked
            with a key not allowed
        """
        api_key = KeyManagement()
        map_key = api_key.keys['staticMap']
        demand = googlemapsapi.get_place_id_list('openClassRooms', map_key)
        result_place_id = {
            'candidates' : [],
            'error_message' : 'This API key is not authorized to use this service or API.',
            'status' : 'REQUEST_DENIED'
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_place_id).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand == result_place_id

    # google map API test on place id location
    def test_geolocal_bab_request(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference ID of the bad address asked
        """
        api_key = KeyManagement()
        map_key = api_key.keys['map']
        demand = googlemapsapi.get_place_id_list('rueopenClassRooms', map_key)
        result_place_id = {
            'candidates': [],
            'status' : 'ZERO_RESULTS'
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_place_id).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand == result_place_id

    # google map API test on address location
    def test_geolocal_address(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference of the requested address
        """
        api_key = KeyManagement()
        map_key = api_key.keys['map']
        place_id = 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
        demand = googlemapsapi.get_address(place_id, map_key)
        result_address = {
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
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_address).encode())

        monkeypatch.setattr(urllib.request, 'urlopen',mockreturn)
        assert demand == result_address

    # google map API test on address location with bab key
    def test_geolocal_bad_address(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference of the requested address
            with bab key
        """
        api_key = KeyManagement()
        map_key = 0
        place_id = 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
        demand = googlemapsapi.get_address(place_id, map_key)
        result_address = {
            'error_message' : 'The provided API key is invalid.',
           'html_attributions' : [],
           'status' : 'REQUEST_DENIED'
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_address).encode())

        monkeypatch.setattr(urllib.request, 'urlopen',mockreturn)
        assert demand == result_address

    # google map API test on address location with key not allowed
    def test_geolocal_address_not_authorized(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference of the requested address
            with key not allowed
        """
        api_key = KeyManagement()
        map_key = api_key.keys['staticMap']
        place_id = 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
        demand = googlemapsapi.get_address(place_id, map_key)
        result_address = {
            'error_message' : 'This API key is not authorized to use this service or API.',
           'html_attributions' : [],
           'status' : 'REQUEST_DENIED'
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_address).encode())

        monkeypatch.setattr(urllib.request, 'urlopen',mockreturn)
        assert demand == result_address

    # google map API test on address location with bab place_id
    def test_geolocal_invalid(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference of the requested address
            with bab place_id
        """
        api_key = KeyManagement()
        map_key = api_key.keys['map']
        place_id = 'c8'
        demand = googlemapsapi.get_address(place_id, map_key)
        result_address = {
            'html_attributions': [],
            'status': 'INVALID_REQUEST'
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_address).encode())

        monkeypatch.setattr(urllib.request, 'urlopen',mockreturn)
        assert demand == result_address

    # google map API test on map static
    def test_geolocal_static(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a image static
            containing the reference ID of the address asked
        """
        api_key = KeyManagement()
        map_key = api_key.keys['map']
        address = 
        demand = googlemapsapi.get_static(address, map_key)
        result_static = {
            'address':{
                'result': {
                    'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                    'geometry': {
                        'location': {'lat': 48.8975156, 'lng': 2.3833993}
                    }
                }
            }
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """
            return BytesIO(json.dumps(result_static).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand == result_static

if __name__ == "__main__":
    pass
