#coding:utf-8
#!/usr/bin/env python
"""
    googleMap API test module
"""
import requests

from ..googlemapsapi import GoogleMapsAddressProcessing

# ~ def api_params():
    # ~ google_api = GoogleMapsAddressProcessing('openClassrooms')
    # ~ params = {
        # ~ 'map_key': google_api.api_config.get_keys['map'],
        # ~ 'static_key': google_api.api_config.get_keys['staticMap'],
        # ~ 'bab_key': 0,
        # ~ 'url_api1': google_api.api_data.url_api1,
        # ~ 'url_api2': google_api.api_data.url_api2
    # ~ }
    # ~ return params

# ~ def get_mockreturn(result):
    # ~ """
        # ~ mock template call
    # ~ """
    # ~ def mock_get(url, params):
        # ~ """
            # ~ Mock function on api object
        # ~ """
        # ~ class JsonResponse:
            # ~ """
                # ~ mock result in JSON format
            # ~ """
            # ~ @staticmethod
            # ~ def json():
                # ~ """
                    # ~ Json method
                # ~ """
                # ~ return result
        # ~ return JsonResponse()
    # ~ return mock_get

# ~ class TestApiGoogleMap:
    # ~ """
        # ~ configuration of imported modules
    # ~ """
    # ~ def setup_method(self):
        # ~ self.params = api_params()
        # ~ self.api_google = self.params.google_api

    # ~ def test_geolocal_id(monkeypatch):
        # ~ """
            # ~ Google Map A.P.I test function that returns a file
            # ~ Json containing the reference ID of the address asked
        # ~ """
        # ~ address = 'openClassrooms'
        # ~ result_placeid = {
            # ~ "candidates" : [
              # ~ {
                 # ~ "place_id" : "ChIJIZX8lhRu5kcRGwYk8Ce3Vc8"
              # ~ }
           # ~ ],
           # ~ "status" : "OK"
        # ~ }
        # ~ demand =\
            # ~ self.google_api.get_from_url_placeid_api(
                # ~ address, self.params['map_key']
        # ~ )
        # ~ demand1 = self.google_api.get_from_url_placeid_api(
            # ~ address, self.params['map_key']
        # ~ )
        # ~ demand2 = self.google_api.get_from_url_placeid_api(
            # ~ address, self.params['bad_key']
        # ~ )
        # ~ demand3 = self.google_api.get_from_url_placeid_api(
            # ~ address, self.params['static_key']
        # ~ )
        # ~ demand4 = self.google_api.get_from_url_placeid_api(
        # ~ 'rueopenClassRooms', self.params['map_key']
        # ~ )
        # ~ result_place_id1 = {
            # ~ 'candidates': [{
                # ~ 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
            # ~ }],
            # ~ 'status' : 'OK'
        # ~ }
        # ~ result_place_id2 = {
            # ~ 'candidates' : [],
            # ~ 'error_message' : 'The provided API key is invalid.',
            # ~ 'status' : 'REQUEST_DENIED'
        # ~ }
        # ~ result_place_id3 = {
            # ~ 'candidates' : [],
            # ~ 'error_message' : 'This API key is not authorized to use this service or API.',
            # ~ 'status' : 'REQUEST_DENIED'
        # ~ }
        # ~ result_place_id4 = {
            # ~ 'candidates': [],
            # ~ 'status' : 'ZERO_RESULTS'
        # ~ }
        # ~ mockreturn = get_mockreturn('result_place_id1')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand1 == result_place_id1
    
        # ~ mockreturn = get_mockreturn('result_place_id2')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand2 == result_place_id2
    
        # ~ mockreturn = get_mockreturn('result_place_id3')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand3 == result_place_id3
    
        # ~ mockreturn = get_mockreturn('result_place_id4')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand4 == result_place_id4
    
    # ~ def test_geolocal_address(monkeypatch):
        # ~ """
            # ~ Google Map A.P.I test function that returns a file
            # ~ Json containing the reference of the requested address
        # ~ """
        # ~ place_id1 = 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8'
        # ~ place_id2 = 'c8'
    
        # ~ demand1 = self.get_from_url_address_api(
            # ~ place_id1, self.test_key_params['map_key']
        # ~ )
        # ~ demand2 = self.get_from_url_address_api(
            # ~ place_id1, self.test_key_params['bad_key']
        # ~ )
        # ~ demand3 = self.get_from_url_address_api(
            # ~ place_id1, self.test_key_params['static_key']
        # ~ )
        # ~ demand4 = self.get_from_url_address_api(
            # ~ place_id2, self.test_key_params['map_key']
        # ~ )
        # ~ result_address1 = {
            # ~ 'html_attributions': [],
            # ~ 'result': {
                # ~ 'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                # ~ 'geometry': {
                    # ~ 'location': {'lat': 48.8975156, 'lng': 2.3833993},
                    # ~ 'viewport': {
                        # ~ 'northeast': {'lat': 48.89886618029151, 'lng': 2.384755530291502},
                        # ~ 'southwest': {'lat': 48.89616821970851, 'lng': 2.382057569708498}
                    # ~ }
                # ~ }
            # ~ },
            # ~ 'status': 'OK'
        # ~ }
        # ~ result_address2 = {
            # ~ 'error_message' : 'The provided API key is invalid.',
           # ~ 'html_attributions' : [],
           # ~ 'status' : 'REQUEST_DENIED'
        # ~ }
        # ~ result_address3 = {
            # ~ 'error_message' : 'This API key is not authorized to use this service or API.',
           # ~ 'html_attributions' : [],
           # ~ 'status' : 'REQUEST_DENIED'
        # ~ }
        # ~ result_address4 = {
            # ~ 'html_attributions': [],
            # ~ 'status': 'INVALID_REQUEST'
        # ~ }
        # ~ mockreturn = get_mockreturn('result_address1')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand1 == result_address1
    
        # ~ mockreturn = get_mockreturn('result_address2')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand2 == result_address2
    
        # ~ mockreturn = get_mockreturn('result_address3')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand3 == result_address3
    
        # ~ mockreturn = get_mockreturn('result_address4')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand4 == result_address4


# ~ if __name__ == "__main__":
    # ~ pass
