#!/usr/bin/env python

import urllib.request

import json
from io import BytesIO

from gpapp.question_answer import parser
from gpapp.question_answer import get_place_id, get_address

# parser test on the question asked to grandPy
def test_parser():
    """
    Test function on the separation of the character string (question asked
     a papyRobot alias grandPy) in several words,
     removing unnecessary words in order to keep the keywords for the
     search (location history & geographic coordinates)
    """
    # question asked to grandPy
    demand = "ou est situé le restaurant la_nappe_d_or de lyon"

    assert parser(demand) == ["restaurant","la_nappe_d_or","lyon"]

# google map API test on place id location
def test_geolocal_id(monkeypatch):
    """
    Google Map A.P.I test function that returns a file
     Json containing the reference ID of the address asked
    """

    resul_pid = {
                    'candidates': [{
                        'place_id': "ChIJTei4rhlu5kcRPivTUjAg1RU"
                    }]
                }

    def mockreturn(request):
        """
        Mock function on place_id object
        """

        return BytesIO(json.dumps(resul_pid).encode())

    monkeypatch.setattr(urllib.request, 'urlopen',
        mockreturn)

    assert get_place_id() == resul_pid


# ~ # google map API test on address location
def test_geolocal_address(monkeypatch):
    """
    Google Map A.P.I test function that returns a file
     Json containing the reference of the requested address
    """
    resul_address = {
                        'result': {
                            'formatted_address': "16 Rue Étienne Marcel, 75002 Paris, France"
                        }
                    }

    def mockreturn(request):
        """
        Mock function on place_id object
        """

        return BytesIO(json.dumps(resul_address).encode())

    monkeypatch.setattr(urllib.request, 'urlopen',
        mockreturn)

    assert get_address() == resul_address
