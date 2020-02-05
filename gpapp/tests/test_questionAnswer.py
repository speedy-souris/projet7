#coding:utf-8
#!/usr/bin/env python

import json
from io import BytesIO
import urllib.request
from ..classSetting.dataTesting import ParamsTest as params
from .. import question_answer as script

                        #=====================
                        # parser and API test
                        #=====================

# parser test on the question asked to grandPy
def test_parser():
    """
        Test function on the separation of the character string (question asked
        a papyRobot alias grandPy) in several words,
        removing unnecessary words in order to keep the keywords for the
        search (location history & geographic coordinates)
    """
    # question asked to grandPy
    demand = params.testing()["demand"]

    assert script.parser(demand) == params.testing()["parsed"]

# google map API test on place id location
def test_geolocal_id(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference ID of the address asked
    """

    resul_pid = params.testing()["geoPlaceId"]

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
    resul_address = params.testing()["address"]

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
    resul_history = params.testing()["history"]

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
        decency function test
    """
    assert script.wickedness("vieux fossile") == False

# comprehension test
def test_comprehension():
    """
        comprehension function test
    """
    assert script.comprehension("bonjopur") == False

# end of counterSession test
def test_counterSession():
    """
        end of session function test by request counter
    """
    assert script.counter_session("mont saint-michel", 10) == True

# end of apiSession test
def test_apiSession():
    """
        end of session function test by API parameters
    """
    assert script.api_session("arene arles", apiParams=True) == True




