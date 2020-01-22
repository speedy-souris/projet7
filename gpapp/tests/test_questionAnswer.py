#coding:utf-8
#!/usr/bin/env python

import json
from io import BytesIO

import urllib.request

from ..question_answer import parser
from ..question_answer import get_place_id_list, get_address
from ..question_answer import get_history

class TestingConf:
    """
        management of API parameters by default for tests
    """
    DEMAND = "ou est situé le restaurant la_nappe_d_or de lyon"
    PARSED = ["restaurant","la_nappe_d_or","lyon"]
    GEOPLACEID = {
        'candidates': [{
            'place_id': "ChIJTei4rhlu5kcRPivTUjAg1RU"
        }]
    }
    ADDRESS = {
        'result': {
            'formatted_address': "16 Rue Étienne Marcel, 75002 Paris, France"
        }
    }
    HISTORY = [
        [
            """Riche d'un long passé artistique, ce secteur de Paris (France)
            dominé par la Basilique du Sacré-Cœur a toujours été le symbole
            d'un mode de vie bohème où, de Picasso à Modigliani, de nombreux
            artistes trouvèrent refuge."""
        ]
    ]

    @classmethod
    def test_data(cls):
        data = {
            "demand": cls.DEMAND,
            "parsed": cls.PARSED,
            "geoPlaceId": cls.GEOPLACEID,
            "address": cls.ADDRESS,
            "history": cls.HISTORY
        }
        return data

class ParamsTest:
    """
        API default settings for testing
    """
    TESTINGCONFIG = TestingConf()

    @classmethod
    def testing(cls):
        test = {
            "demand": cls.TESTINGCONFIG.test_data()["demand"],
            "parsed": cls.TESTINGCONFIG.test_data()["parsed"],
            "geoPlaceId": cls.TESTINGCONFIG.test_data()["geoPlaceId"],
            "address": cls.TESTINGCONFIG.test_data()["address"],
            "history": cls.TESTINGCONFIG.test_data()["history"]
        }
        return test

# parser test on the question asked to grandPy
def test_parser():
    """
        Test function on the separation of the character string (question asked
        a papyRobot alias grandPy) in several words,
        removing unnecessary words in order to keep the keywords for the
        search (location history & geographic coordinates)
    """
    # question asked to grandPy
    demand = ParamsTest.testing()["demand"]

    assert parser(demand) == ParamsTest.testing()["parsed"]

# google map API test on place id location
def test_geolocal_id(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference ID of the address asked
    """

    resul_pid = ParamsTest.testing()["geoPlaceId"]

    def mockreturn(request):
        """
            Mock function on place_id object
        """

        return BytesIO(json.dumps(resul_pid).encode())

    monkeypatch.setattr(
        urllib.request, 'urlopen',mockreturn
    )

    assert get_place_id_list() == resul_pid

# google map API test on address location
def test_geolocal_address(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference of the requested address
    """
    resul_address = ParamsTest.testing()["address"]

    def mockreturn(request):
        """
            Mock function on place_id object
        """

        return BytesIO(json.dumps(resul_address).encode())

    monkeypatch.setattr(
        urllib.request, 'urlopen',mockreturn
    )

    assert get_address() == resul_address

# WikiMedia APi test on search
def test_search_wiki(monkeypatch):
    """
        A.P.I wikipedia test function (wikimedia) that returns a file
        Json containing the history of the requested address
    """
    resul_history = ParamsTest.testing()["history"]

    def mockreturn(request):
        """
            Mock function on history search
        """

        return BytesIO(json.dumps(resul_history).encode())

    monkeypatch.setattr(
        urllib.request, 'urlopen',mockreturn
    )

    assert get_history() == resul_history
