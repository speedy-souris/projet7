#coding:utf-8
#!/usr/bin/env python

from ..user import Question
from ..chatdata import BehaviorData


def script_data():
    dataDiscussion = BehaviorData()
    user_request = 'connais tu openClassRooms'
    data = {
        'user_request': user_request,
        'question': Question(user_request, dataDiscussion),
        'dataDiscussion': dataDiscussion
    }
    return data

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
        data = script_data()
        demand = data['question'].parser(data['user_request'])
        # question asked to grandPy
        result_parsed = 'openClassRooms'
        assert demand == result_parsed

    def test_civility(self):
        """
            civility function test
        """
        data = script_data()
        demand = data['question'].user_civility()
        assert demand == data['dataDiscussion'].civility
        other_demand = Question('bonjour', data['dataDiscussion']).user_civility()
        assert other_demand == data['dataDiscussion'].civility

    def test_decency(self):
        """
            decency function test
        """
        data = script_data()
        demand = data['question'].user_decency()
        assert demand == data['dataDiscussion'].decency
        other_demand = Question('fossile', data['dataDiscussion']).user_decency()
        assert other_demand == data['dataDiscussion'].decency

    def test_comprehension(self):
        """
            comprehension function test
        """
        data = script_data()
        demand = data['question'].user_comprehension()
        assert demand == data['dataDiscussion'].comprehension
        other_demand =\
            Question('cvccc', data['dataDiscussion']).user_comprehension()
        assert other_demand == data['dataDiscussion'].comprehension
