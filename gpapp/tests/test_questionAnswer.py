#coding:utf-8
#!/usr/bin/env python

import json
from io import BytesIO
import urllib.request
from .. import question_answer as script

                        #=====================
                        # parser and API test
                        #=====================
class TestingConf:
    """
        management of API parameters
    """
    def __init__(self):
        self.data = {}

class ParamsTest:
    """
        API default settings for testing
    """
    TESTING = TestingConf()

    @classmethod
    def test_testing(cls):
        """
            Initialization of API parameters by default for tests
        """
        cls.TESTING.data["demand"] =\
            "ou est situé le restaurant la_nappe_d_or de lyon"
        cls.TESTING.data["parsed"] = [
            "restaurant","la_nappe_d_or","lyon"
        ]
        cls.TESTING.data["geoPlaceId"] = {
            'candidates': [{
                'place_id': "ChIJTei4rhlu5kcRPivTUjAg1RU"
            }]
        }
        cls.TESTING.data["address"] = {
            'result': {
                'formatted_address': "16 Rue Étienne Marcel, 75002 Paris, France"
            }
        }
        cls.TESTING.data["history"] = [
            [
                """Riche d'un long passé artistique, ce secteur de Paris (France)
                dominé par la Basilique du Sacré-Cœur a toujours été le symbole
                d'un mode de vie bohème où, de Picasso à Modigliani, de nombreux
                artistes trouvèrent refuge."""
            ]
        ]

        return cls.TESTING.data

# parser test on the question asked to grandPy
def test_parser():
    """
        Test function on the separation of the character string (question asked
        a papyRobot alias grandPy) in several words,
        removing unnecessary words in order to keep the keywords for the
        search (location history & geographic coordinates)
    """
    # question asked to grandPy
    demand = ParamsTest.test_testing()["demand"]

    assert script.parser(demand) == ParamsTest.test_testing()["parsed"]

# google map API test on place id location
def test_geolocal_id(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference ID of the address asked
    """

    resul_pid = ParamsTest.test_testing()["geoPlaceId"]

    def mockreturn(request):
        """
            Mock function on place_id object
        """

        return BytesIO(json.dumps(resul_pid).encode())

    monkeypatch.setattr(
        urllib.request, 'urlopen',mockreturn
    )

    assert script.get_place_id_list() == resul_pid

# google map API test on address location
def test_geolocal_address(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference of the requested address
    """
    resul_address = ParamsTest.test_testing()["address"]

    def mockreturn(request):
        """
            Mock function on place_id object
        """

        return BytesIO(json.dumps(resul_address).encode())

    monkeypatch.setattr(
        urllib.request, 'urlopen',mockreturn
    )

    assert script.get_address() == resul_address

# WikiMedia APi test on search
def test_search_wiki(monkeypatch):
    """
        A.P.I wikipedia test function (wikimedia) that returns a file
        Json containing the history of the requested address
    """
    resul_history = ParamsTest.test_testing()["history"]

    def mockreturn(request):
        """
            Mock function on history search
        """

        return BytesIO(json.dumps(resul_history).encode())

    monkeypatch.setattr(
        urllib.request, 'urlopen',mockreturn
    )

    assert script.get_history() == resul_history

                        #=======================================
                        # politeness, comprehension,
                        # comprehension and end of session test
                        #=======================================

# Civility test
def test_civility():
    """
        civility function test
    """
    assert script.civility("montmartre") == False

# decency test
def test_decency():
    """
        dencency function test
    """
    assert script.wickedness("vieux fossile") == False

# comprehension test
def test_comprehension():
    """
        comprehension function test
    """
    assert script.comprehension("bonjopur") == False





