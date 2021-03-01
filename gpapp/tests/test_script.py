#coding:utf-8
#!/usr/bin/env python

from ..user import Question

class TestUserQuestion:
    """
         management of test user's question
    """
    # user question parser test
    def test_parser(self):
        """
            Test function on the separation of the character string (question asked
            a papyRobot alias grandPy) in several words,
            removing unnecessary words in order to keep the keywords for the
            search (location history & geographic coordinates)
        """
        user_request = 'connais tu openClassRooms'
        question = Question(user_request, None)
        demand = question.parser(user_request)
        # question asked to grandPy
        result_parsed = 'openClassRooms'
        assert demand == result_parsed

# ~ class TestBehaviour:
    # ~ """
        # ~ user behavior management
            # ~ - Politeness
            # ~ - Comprehension
    # ~ """

    # ~ # Civility test
    # ~ def test_civility(self):
        # ~ """
            # ~ civility function test
        # ~ """
        # ~ # only one value on redis for civility : do not mix conversation object
        # ~ demand = script.DataParameter("montmartre")
        # ~ script.DataParameter("montmartre").civility()
        # ~ assert False == demand.read_civility
        # ~ other_demand = script.DataParameter("bonjour")
        # ~ script.DataParameter("bonjour").civility()
        # ~ assert True == other_demand.read_civility

    # ~ # decency test
    # ~ def test_decency(self):
        # ~ """
            # ~ decency function test
        # ~ """
        # ~ # only one value on redis for decency : do not mix conversation object
        # ~ demand = script.DataParameter("montmartre")
        # ~ script.DataParameter("montmartre").decency()
        # ~ assert True == demand.read_decency
        # ~ other_demand = script.DataParameter("fossile")
        # ~ script.DataParameter("fossile").decency()
        # ~ assert False == other_demand.read_decency

    # ~ # Convertion of boolean Test
    # ~ def test_bool_to_string(self):
        # ~ """
            # ~ convert a boolean to string
        # ~ """
        # ~ assert script.bool_convers(False) == "0"
        # ~ assert script.bool_convers(True) == "1"

    # ~ def test_string_to_boolean(self):
        # ~ """
            # ~ convert a string to boolean
        # ~ """
        # ~ assert script.str_convers(b"0") == False
        # ~ assert script.str_convers(b"1") == True
        # ~ assert script.str_convers(b"") == False

    # ~ def test_comprehension(self):
        # ~ """
            # ~ comprehension function test
        # ~ """
        # ~ pass
        # ~ assert script.Behaviour.comprehension("bonjour grandpy") == True

    # ~ # end of counterSession test
    # ~ def test_counterSession(self):
        # ~ """
            # ~ end of session function test by request counter
        # ~ """
        # ~ assert script.Behaviour.counter_session("mont saint-michel", 10) == True
