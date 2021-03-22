#coding:utf-8
#!/usr/bin/env python

from ..user import Question
from ..chatdata import BehaviorData
from ..answersearch import Research
from ..wikimediaapi import ApiWikiMedia


def get_script_data():
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
        data = get_script_data()
        demand = data['question'].parser(data['user_request'])
        # question asked to grandPy
        result_parsed = 'openClassRooms'
        assert demand == result_parsed

    def test_civility(self):
        """
            civility function test
        """
        data = get_script_data()
        demand = data['question'].user_civility()
        assert demand == data['dataDiscussion'].civility
        other_demand = Question('bonjour', data['dataDiscussion']).user_civility()
        assert other_demand == data['dataDiscussion'].civility

    def test_decency(self):
        """
            decency function test
        """
        data = get_script_data()
        demand = data['question'].user_decency()
        assert demand == data['dataDiscussion'].decency
        other_demand = Question('fossile', data['dataDiscussion']).user_decency()
        assert other_demand == data['dataDiscussion'].decency

    def test_comprehension(self):
        """
            comprehension function test
        """
        data = get_script_data()
        demand = data['question'].user_comprehension()
        assert demand == data['dataDiscussion'].comprehension
        other_demand =\
            Question('cvccc', data['dataDiscussion']).user_comprehension()
        assert other_demand == data['dataDiscussion'].comprehension

class TestResearch:
    """
        management of test API research
    """
    RESEARCH = Research(user=None)
    def test_address_conversion(self):
        """
            comma deletion, convert to lowercase, convert to list
        """
        research = self.RESEARCH
        address = '10 Quai de la charente, 75019 Paris, France'
        converted_result = [
            '10','quai','de','la','charente','75019','paris','france'
        ]
        demand = research.get_from_address_conversion(address)
        assert demand == converted_result

    def test_common_list(self):
        """
            determine the address
            of the common wikipedia page
            with the googleMap address
        """
        research = self.RESEARCH
        lst_wiki = [
            ['Quai', 'de', 'la', 'Gironde'],
            ['Parc', 'du', 'Pont', 'de', 'Flandre'],
            ['Square', 'du', 'Quai-de-la-Gironde'],    
            ['Avenue', 'Corentin-Cariou'],
            ['Porte', 'de', 'la', 'Villette', '(métro', 'de', 'Paris)'],
            ['Quai', 'de', 'la', 'Charente'],
            ['Porte', 'de', 'la', 'Villette'],
            ['Rue', 'Benjamin-Constant'],
            ['Quai', 'du', 'Lot'],
            ['Gare', 'du', 'pont', 'de', 'Flandre']
        ]
        lst_address = [
            '10','quai','de','la','charente','75019','paris','france'
        ]
        demand = research.get_from_common_list_creation(lst_wiki, lst_address)
        common_result = 'Quai de la Charente'
        assert demand == common_result
