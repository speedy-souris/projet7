#coding:utf-8
#!/usr/bin/env python

from ..user import Question
from ..chatdata import BehaviorData


USER_REQUEST = 'connais tu openClassRooms'
DATADISCUSSION = BehaviorData()
QUESTION = Question(USER_REQUEST, DATADISCUSSION)

class TestUserQuestion:
    """
         management of test user's question
         user behavior management
            - Politeness
            - Comprehension
    """
    def test_parser(self):
        """
            Test function on the separation of the character string (question asked
            a papyRobot alias grandPy) in several words,
            removing unnecessary words in order to keep the keywords for the
            search (location history & geographic coordinates)
        """
        demand = QUESTION.parser(USER_REQUEST)
        # question asked to grandPy
        result_parsed = 'openClassRooms'
        assert demand == result_parsed

    def test_civility(self):
        """
            civility function test
        """
        demand = QUESTION.user_civility()
        assert demand == DATADISCUSSION.civility
        other_demand = Question('bonjour', DATADISCUSSION).user_civility()
        assert other_demand == DATADISCUSSION.civility

    def test_decency(self):
        """
            decency function test
        """
        demand = QUESTION.user_decency()
        assert demand == DATADISCUSSION.decency
        other_demand = Question('fossile', DATADISCUSSION).user_decency()
        assert other_demand == DATADISCUSSION.decency

    def test_comprehension(self):
        """
            comprehension function test
        """
        demand = QUESTION.user_comprehension()
        assert demand == DATADISCUSSION.comprehension
        other_demand =\
            Question('cvccc', DATADISCUSSION).user_comprehension()
        assert other_demand == DATADISCUSSION.comprehension
