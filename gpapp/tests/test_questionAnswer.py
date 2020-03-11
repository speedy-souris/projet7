#coding:utf-8
#!/usr/bin/env python

import json
from io import BytesIO
import urllib.request
from .. import devSetting
from ..devSetting.dataRedis import Conversation
from ..devSetting import fDev
# ~ from .. import question_answer

                        #=====================
                        # parser and API test
                        #=====================

class TestApi:
    """
        management of test APi parameters
    """
    def test_parser(self):
        """
            Test function on the separation of the character string (question asked
            a papyRobot alias grandPy) in several words,
            removing unnecessary words in order to keep the keywords for the
            search (location history & geographic coordinates)
        """
        # question asked to grandPy
        demand = Conversation("ou est situé le restaurant la_nappe_d_or de lyon")

        assert demand.parser() == ["restaurant","la_nappe_d_or","lyon"]

    # google map API test on place id location
    def test_geolocal_id(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference ID of the address asked
        """

        resul_pid = {
            'candidates': [{
                'place_id': "ChIJTei4rhlu5kcRPivTUjAg1RU"
            }]
        }
        address_result = {
            'result': {
                'formatted_address': "16 Rue Étienne Marcel, 75002 Paris, France"
            }
        }
        def mockreturn(request):
            """
                Mock function on place_id object
            """

            return BytesIO(json.dumps(resul_pid).encode())

        monkeypatch.setattr(
            urllib.request, 'urlopen',mockreturn
        )

        assert fDev.get_place_id_list(address_result) == resul_pid

    # ~ # google map API test on address location
    def test_geolocal_address(self, monkeypatch):
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

        monkeypatch.setattr(
            urllib.request, 'urlopen',mockreturn
        )

        assert fDev.get_address("ChIJTei4rhlu5kcRPivTUjAg1RU") == resul_address

    # WikiMedia APi test on search
    def test_search_wiki(self, monkeypatch):
        """
            A.P.I wikipedia test function (wikimedia) that returns a file
            Json containing the history of the requested address
        """
        resul_history = [
            [
                """Riche d'un long passé artistique, ce secteur de Paris (France)
                dominé par la Basilique du Sacré-Cœur a toujours été le symbole
                d'un mode de vie bohème où, de Picasso à Modigliani, de nombreux
                artistes trouvèrent refuge."""
            ]
        ]

        def mockreturn(request):
            """
                Mock function on history search
            """

            return BytesIO(json.dumps(resul_history).encode())

        monkeypatch.setattr(
            urllib.request, 'urlopen',mockreturn
        )

        assert fDev.get_history("montmartre") == resul_history

# ~ class TestBehaviour:
    # ~ """

    # ~ """
                            # ~ #=======================================
                            # ~ # politeness, comprehension,
                            # ~ # comprehension and end of session test
                            # ~ #=======================================

    # ~ # Civility test
    # ~ def test_incivility(self):
        # ~ """
            # ~ civility function test
        # ~ """
        # ~ assert script.Response().POLITENESS.civility("montmartre") == False

    # ~ def test_civility(self):
        # ~ """
            # ~ civility function test
        # ~ """
        # ~ assert script.Politeness().civility("bonjour") == True

    # ~ # decency test
    # ~ def test_indecency(self):
        # ~ """
            # ~ decency function test
        # ~ """
        # ~ assert script.Behaviour.wickedness("vieux fossile") == False

    # ~ def test_decency(self):
        # ~ """
            # ~ decency function test
        # ~ """
        # ~ assert script.Behaviour.wickedness("bonjour grandpy") == True

    # ~ # comprehension test
    # ~ def test_incomprehension(self):
        # ~ """
            # ~ comprehension function test
        # ~ """
        # ~ assert script.Behaviour.comprehension("bonjopur") == False

    # ~ def test_comprehension(self):
        # ~ """
            # ~ comprehension function test
        # ~ """
        # ~ assert script.Behaviour.comprehension("bonjour grandpy") == True

    # ~ # end of counterSession test
    # ~ def test_counterSession(self):
        # ~ """
            # ~ end of session function test by request counter
        # ~ """
        # ~ assert script.Behaviour.counter_session("mont saint-michel", 10) == True

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
