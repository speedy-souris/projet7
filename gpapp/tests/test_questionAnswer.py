#coding:utf-8
#!/usr/bin/env python

import json
from io import BytesIO
import urllib.request
from ..devSetting import dataTesting as params
from .. import question_answer as script

                        #=====================
                        # parser and API test
                        #=====================
class TestApi:
    """
        management of test APi parameters
    """
    DATA = params.ParamsTest().testing
    # parser test on the question asked to grandPy
    @classmethod
    def test_parser(cls):
        """
            Test function on the separation of the character string (question asked
            a papyRobot alias grandPy) in several words,
            removing unnecessary words in order to keep the keywords for the
            search (location history & geographic coordinates)
        """
        # question asked to grandPy
        demand = cls.TestApi.DATA["demand"]

        assert script.ApiParams.parser(demand) == cls.TestApi.DATA["parsed"]

    # google map API test on place id location
    @classmethod
    def test_geolocal_id(cls, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference ID of the address asked
        """

        resul_pid = cls.TestApi.DATA["geoPlaceId"]

        def mockreturn(request):
            """
                Mock function on place_id object
            """

            return BytesIO(json.dumps(resul_pid).encode())

        monkeypatch.setattr(
            urllib.request, 'urlopen',mockreturn
        )

        assert script.ApiParams.get_place_id_list() == resul_pid

    # google map API test on address location
    @classmethod
    def test_geolocal_address(cls, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference of the requested address
        """
        resul_address = cls.TestApi.DATA["address"]

        def mockreturn(request):
            """
                Mock function on place_id object
            """

            return BytesIO(json.dumps(resul_address).encode())

        monkeypatch.setattr(
            urllib.request, 'urlopen',mockreturn
        )

        assert script.ApiParams.get_address() == resul_address

    # WikiMedia APi test on search
    @classmethod
    def test_search_wiki(cls, monkeypatch):
        """
            A.P.I wikipedia test function (wikimedia) that returns a file
            Json containing the history of the requested address
        """
        resul_history = cls.TestApi.DATA["history"]

        def mockreturn(request):
            """
                Mock function on history search
            """

            return BytesIO(json.dumps(resul_history).encode())

        monkeypatch.setattr(
            urllib.request, 'urlopen',mockreturn
        )

        assert script.ApiParams.get_history() == resul_history

class TestBehaviour:
    """

    """
                            #=======================================
                            # politeness, comprehension,
                            # comprehension and end of session test
                            #=======================================

    # Civility test
    def test_incivility(self):
        """
            civility function test
        """
        assert script.Response().POLITENESS.civility("montmartre") == False

    def test_civility(self):
        """
            civility function test
        """
        assert script.Politeness().civility("bonjour") == True

    # decency test
    def test_indecency(self):
        """
            decency function test
        """
        assert script.Behaviour.wickedness("vieux fossile") == False

    def test_decency(self):
        """
            decency function test
        """
        assert script.Behaviour.wickedness("bonjour grandpy") == True

    # comprehension test
    def test_incomprehension(self):
        """
            comprehension function test
        """
        assert script.Behaviour.comprehension("bonjopur") == False

    def test_comprehension(self):
        """
            comprehension function test
        """
        assert script.Behaviour.comprehension("bonjour grandpy") == True

    # end of counterSession test
    def test_counterSession(self):
        """
            end of session function test by request counter
        """
        assert script.Behaviour.counter_session("mont saint-michel", 10) == True

# civility and decency test
# if civility == True
#     assert decency == True / assert decency == False
# if civility == False
# assert decency == True / assert decency == False
#    ------------------------------------
# civility and comprehension test
# if civility == True
#     assert comprehension == True / assert comprehension == False
# if civility == False
# assert comprehension == True / assert comprehension == False

if __name__ == "__main__":
    pass
