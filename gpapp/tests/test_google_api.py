#coding:utf-8
#!/usr/bin/env python

import requests

from ..apis.dataapi import ApiGoogleMaps
from ..apis.answersearch import KeyManagement


class TestParamsImport(KeyManagement):
    """
        configuration of imported modules
    """
    def __init__(self):
        super().__init__()
        self.params = self.test_import_params()
        self.keys_api = self.params['keys_api_value']
        self.api_google = self.params['api_module']

    def test_api_keys(self):
        keys_api_Google_map = {
            'map_key': self.get_keys['map'],
            'static_key': self.get_keys['staticMap'],
            'bad_key': 0
        }
        return keys_api_Google_map

    def test_import_params(self):
        params = {
            'api_module': ApiGoogleMaps(),
            'keys_api_value': self.test_api_keys()
        }
        return params

IMPORT_PARAMS = TestParamsImport()
GOOGLE_KEY = IMPORT_PARAMS.keys_api
GOOGLE_MAP = IMPORT_PARAMS.api_google

def get_mockreturn(result):
    def mock_get(url, params):
        """
            Mock function on api object
        """
        class JsonResponse:
            @staticmethod
            def json():
                return result
        return JsonResponse()
    return mock_get

def test_geolocal_id(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference ID of the address asked
    """
    demand1 = GOOGLE_MAP.get_from_url_placeid_api(
        'openClassRooms', GOOGLE_KEY['map_key']
    )
    demand2 = GOOGLE_MAP.get_from_url_placeid_api(
        'openClassRooms', GOOGLE_KEY['bad_key']
    )
    demand3 = GOOGLE_MAP.get_from_url_placeid_api(
    'openClassRooms', GOOGLE_KEY['static_key']
    )
    demand4 = GOOGLE_MAP.get_from_url_placeid_api(
    'rueopenClassRooms', GOOGLE_KEY['map_key']
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
    monkeypatch.setattr(requests, 'get', mockreturn)
    assert demand1 == result_place_id1

    mockreturn = get_mockreturn('result_place_id2')
    monkeypatch.setattr(requests, 'get', mockreturn)
    assert demand2 == result_place_id2

    mockreturn = get_mockreturn('result_place_id3')
    monkeypatch.setattr(requests, 'get', mockreturn)
    assert demand3 == result_place_id3

    mockreturn = get_mockreturn('result_place_id4')
    monkeypatch.setattr(requests, 'get', mockreturn)
    assert demand4 == result_place_id4

def test_geolocal_address(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference of the requested address
    """
    place_id1 = 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
    place_id2 = 'c8'

    demand1 = GOOGLE_MAP.get_from_url_address_api(
        place_id1, GOOGLE_KEY['map_key']
    )
    demand2 = GOOGLE_MAP.get_from_url_address_api(
        place_id1, GOOGLE_KEY['bad_key']
    )
    demand3 = GOOGLE_MAP.get_from_url_address_api(
        place_id1, GOOGLE_KEY['static_key']
    )
    demand4 = GOOGLE_MAP.get_from_url_address_api(
        place_id2, GOOGLE_KEY['map_key']
    )
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
    monkeypatch.setattr(requests, 'get', mockreturn)
    assert demand1 == result_address1
    
    mockreturn = get_mockreturn('result_address2')
    monkeypatch.setattr(requests, 'get', mockreturn)
    assert demand2 == result_address2

    mockreturn = get_mockreturn('result_address3')
    monkeypatch.setattr(requests, 'get', mockreturn)
    assert demand3 == result_address3

    mockreturn = get_mockreturn('result_address4')
    monkeypatch.setattr(requests, 'get', mockreturn)
    assert demand4 == result_address4


if __name__ == "__main__":
    pass
