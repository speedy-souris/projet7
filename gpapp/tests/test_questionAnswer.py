#coding:utf-8
#!/usr/bin/env python

import json
from io import BytesIO
import urllib.request
from ..question_answer import parser
from ..question_answer import get_place_id_list, get_address
from ..question_answer import get_history
from ..initial import config as conf

#==============================================
# parser test on the question asked to grandPy
#==============================================
def test_parser():
    """
        Test function on the separation of the character string (question asked
        a papyRobot alias grandPy) in several words,
        removing unnecessary words in order to keep the keywords for the
        search (location history & geographic coordinates)
    """
    # question asked to grandPy
    demand = conf.testing["demand"]

    assert parser(demand) == conf.testing["parsed"]

#==========================================
# google map API test on place id location
#==========================================
def test_geolocal_id(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference ID of the address asked
    """
    resul_pid = conf.testing["geoPlaceId"]

    def mockreturn(request):
        """
            Mock function on place_id object
        """
        return BytesIO(json.dumps(resul_pid).encode())

    monkeypatch.setattr(urllib.request,'urlopen',mockreturn)

    assert get_place_id_list() == resul_pid

#=========================================
# google map API test on address location
#=========================================
def test_geolocal_address(monkeypatch):
    """
        Google Map A.P.I test function that returns a file
        Json containing the reference of the requested address
    """
    resul_address = conf.testing["address"]

    def mockreturn(request):
        """
            Mock function on place_id object
        """

        return BytesIO(json.dumps(resul_address).encode())

    monkeypatch.setattr(urllib.request,'urlopen',mockreturn)

    assert get_address() == resul_address

#==============================
# WikiMedia APi test on search
#==============================
def test_search_wiki(monkeypatch):
    """
        A.P.I wikipedia test function (wikimedia) that returns a file
        Json containing the history of the requested address
    """
    resul_history = conf.testing["history"]

    def mockreturn(request):
        """
            Mock function on history search
        """

        return BytesIO(json.dumps(resul_history).encode())

    monkeypatch.setattr(urllib.request,'urlopen',mockreturn)

    assert get_history() == resul_history
