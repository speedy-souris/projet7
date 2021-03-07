#coding:utf-8
#!/usr/bin/env python

import requests
from ..googlemapsapi import ApiGoogleMaps
from ..answersearch import KeyManagement

class TestParamsImport:
    """
        configuration of imported modules
    """
    def __init__(self):
        self.params = self.test_import_params()
        self.keys_api = self.params['keys_api_value']
        self.api_google = self.params['api_module']

    def test_api_keys(self):
        api_key = KeyManagement()
        keys_api_Google_map = {
            'map_key': api_key.get_keys['map'],
            'static_key': api_key.get_keys['staticMap'],
            'bad_key': 0
        }
        return keys_api_Google_map

    def test_import_params(self):
        params = {
            'api_module': ApiGoogleMaps(),
            'keys_api_value': self.test_api_keys()
        }
        return params

# ~ def get_api_data_static(address, localization, key_api):
    # ~ data  = {
        # ~ 'center': f"{address['address']['result']['formatted_address']}",
        # ~ 'zoom': '18.5',
        # ~ 'size': '600x300',
        # ~ 'maptype': 'roadmap',
        # ~ 'markers': f"color:red%7Clabel:A%7C{localization['lat']},\
                   # ~ {localisation['lng']}",
        # ~ 'key': f'{key_api}'
    # ~ }
    # ~ return data

# ~ def get_url_static(address, key_api):
    # ~ address_data = address['address']['result']['formatted_address']
    # ~ localization = address['address']['result']['geometry']['location']
    
    # ~ data = get_api_data_static(address_data, localization, key_api)
    
    # ~ url_api = request_data['url']
    # ~ return url_static



# google map API test on place id location
def test_geolocal_id(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference ID of the address asked
    """
    params = TestParamsImport()
    demand1 = params.api_google.get_url_placeid(
        'openClassRooms', params.keys_api['map_key']
    )
    demand2 = params.api_google.get_url_placeid(
        'openClassRooms', params.keys_api['bad_key']
    )
    demand3 = params.api_google.get_url_placeid(
    'openClassRooms', params.keys_api['static_key']
    )
    demand4 = params.api_google.get_url_placeid(
    'rueopenClassRooms', params.keys_api['map_key']
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
    
    def mock_get(requests, url_params):
        """
            Mock function on api object
        """
        class JsonResponse:
            def json(self):
                return result_place_id1
        return JsonResponse()

    mockreturn = mock_get('result_place_id1')
    monkeypatch.setattr(requests.get, mockreturn)
    assert demand1 == result_place_id1

    def mock_get(requests, url_params):
        """
            Mock function on api object
        """
        class JsonResponse:
            def json(self):
                return result_place_id2
        return JsonResponse()

    mockreturn = mock_get('result_place_id2')
    monkeypatch.setattr(requests.get, mockreturn)
    assert demand2 == result_place_id2

    def mock_get(requests, url_params):
        """
            Mock function on api object
        """
        class JsonResponse:
            def json(self):
                return result_place_id3
        return JsonResponse()
        
    mockreturn = mock_get('result_place_id3')
    monkeypatch.setattr(requests.get, mockreturn)
    assert demand3 == result_place_id3

    def mock_get(requests, url_params):
        """
            Mock function on api object
        """
        class JsonResponse:
            def json(self):
                return result_place_id3
        return JsonResponse()
        
    mockreturn = mock_get('result_place_id4')
    monkeypatch.setattr(requests.get, mockreturn)
    assert demand4 == result_place_id4

# google map API test on address location
def test_geolocal_address(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference of the requested address
    """
    params = TestParamsImport()
    place_id1 = 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
    place_id2 = 'c8'

    demand1 = params.api_google.get_url_address(
        place_id1, params.keys_api['map_key']
    )
    demand2 = params.api_google.get_url_address(
        place_id1, params.keys_api['bad_key']
    )
    demand3 = params.api_google.get_url_address(
        place_id1, params.keys_api['static_key']
    )
    demand4 = params.api_google.get_url_address(
        place_id2, params.keys_api['map_key']
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
    mockreturn = mockreturn('result_address1')
    monkeypatch.setattr(requests.get, mockreturn)
    assert demand1 == result_address1
    
    mockreturn = mockreturn('result_address2')
    monkeypatch.setattr(requests.get, mockreturn)
    assert demand2 == result_address2

    mockreturn = mockreturn('result_address3')
    monkeypatch.setattr(requests.get, mockreturn)
    assert demand3 == result_address3

    mockreturn = mockreturn('result_address4')
    monkeypatch.setattr(requests.get, mockreturn)
    assert demand4 == result_address4

    # google map API test on map static
    # ~ def test_geolocal_static(self, monkeypatch):
        # ~ """
            # ~ Google Map A.P.I test function that returns a image static
            # ~ containing the reference ID of the address asked
        # ~ """
        # ~ data = get_requests()
        # ~ address1 = {
            # ~ 'address': {
                # ~ 'result': {
                    # ~ 'formatted_address': '10QuaidelaCharente,75019Paris,France',
                    # ~ 'geometry': {
                        # ~ 'location': {'lat': 48.8975156, 'lng': 2.3833993}
                    # ~ }
                # ~ }
            # ~ }
        # ~ }
        # ~ address2 = {
            # ~ 'address': {
                # ~ 'result': {
                    # ~ 'formatted_address': 'rueopenClassRooms',
                    # ~ 'geometry': {
                        # ~ 'location': {'lat': 48.8975156, 'lng': 2.3833993}
                    # ~ }
                # ~ }
            # ~ }
        # ~ }
        # ~ demand1 = googlemapsapi.get_url_static(address1, data['static_key'])
        # ~ demand2 = googlemapsapi.get_url_static(address1, data['bad_key'])
        # ~ demand3 = googlemapsapi.get_url_static(address1, data['map_key'])
        # ~ demand4 = googlemapsapi.get_url_static(address2, data['static_key'])

        # ~ result_static1 = get_url_static(address1, data['static_key'])
        # ~ result_static2 = get_url_static(address1, data['bad_key'])
        # ~ result_static3 = get_url_static(address1, data['map_key'])
        # ~ result_static4 = get_url_static(address2, data['static_key'])

        # ~ mockreturn = get_mockreturn('result_static1')
        # ~ monkeypatch.setattr(requests.get, mockreturn)
        # ~ assert demand1 == result_static1
        # ~ mockreturn = get_mockreturn('result_static2')
        # ~ monkeypatch.setattr(requests.get, mockreturn)
        # ~ assert demand2 == result_static2
        # ~ mockreturn = get_mockreturn('result_static3')
        # ~ monkeypatch.setattr(requests.get, mockreturn)
        # ~ assert demand3 == result_static3
        # ~ mockreturn = get_mockreturn('result_static4')
        # ~ monkeypatch.setattr(requests.get, mockreturn)
        # ~ assert demand4 == result_static4


if __name__ == "__main__":
    pass
