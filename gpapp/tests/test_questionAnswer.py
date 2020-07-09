#coding:utf-8
#!/usr/bin/env python

import json
from io import BytesIO
import urllib.request
from .. import question_answer as script

                        #=====================
                        # parser and API test
                        #=====================

class TestApi:
    """
        management of test APi parameters
    """
    # user question parser test
    def test_parser(self):
        """
            Test function on the separation of the character string (question asked
            a papyRobot alias grandPy) in several words,
            removing unnecessary words in order to keep the keywords for the
            search (location history & geographic coordinates)
        """
        # question asked to grandPy
        demand = script.DataParameter(
            "ou est situé le restaurant la_nappe_d_or de lyon"
        )

        assert demand.parser() == ["restaurant","la_nappe_d_or","lyon"]

    # google map API test on place id location
    def test_geolocal_id(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference ID of the address asked
        """
        demand = script.DataParameter("bonjour")
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
        assert demand.get_place_id_list(address_result) == resul_pid

    # ~ # google map API test on address location
    def test_geolocal_address(self, monkeypatch):
        """
            Google Map A.P.I test function that returns a file
            Json containing the reference of the requested address
        """
        demand = script.DataParameter("bonjour")
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

        assert demand.get_address(
            "ChIJTei4rhlu5kcRPivTUjAg1RU"
        ) == resul_address

    # WikiMedia APi test on search
    def test_search_wiki(self, monkeypatch):
        """
            A.P.I wikipedia test function (wikimedia) that returns a file
            Json containing the history of the requested address
        """
        demand = script.DataParameter("bonjour")
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

        assert demand.get_history("montmartre") == resul_history

class TestBehaviour:
    """
        user behavior management
            - Politeness
            - Comprehension
    """

    # Civility test
    def test_civility(self):
        """
            civility function test
        """
        # only one value on redis for civility : do not mix conversation object
        demand = script.DataParameter("montmartre")
        script.DataParameter("montmartre").civility()
        assert False == demand.read_civility
        other_demand = script.DataParameter("bonjour")
        script.DataParameter("bonjour").civility()
        assert True == other_demand.read_civility

    # decency test
    def test_decency(self):
        """
            decency function test
        """
        # only one value on redis for decency : do not mix conversation object
        demand = script.DataParameter("montmartre")
        script.DataParameter("montmartre").decency()
        assert True == demand.read_decency
        other_demand = script.DataParameter("fossile")
        script.DataParameter("fossile").decency()
        assert False == other_demand.read_decency

    # Convertion of boolean Test
    def test_bool_to_string(self):
        """
            convert a boolean to string
        """
        assert script.bool_convers(False) == "0"
        assert script.bool_convers(True) == "1"

    def test_string_to_boolean(self):
        """
            convert a string to boolean
        """
        assert script.str_convers(b"0") == False
        assert script.str_convers(b"1") == True
        assert script.str_convers(b"") == False

    def test_comprehension(self):
        """
            comprehension function test
        """
        pass
        # ~ assert script.Behaviour.comprehension("bonjour grandpy") == True

    # ~ # end of counterSession test
    # ~ def test_counterSession(self):
        # ~ """
            # ~ end of session function test by request counter
        # ~ """
        # ~ assert script.Behaviour.counter_session("mont saint-michel", 10) == True



if __name__ == "__main__":
    pass
