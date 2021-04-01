#coding:utf-8
#!/usr/bin/env python

import requests
from ..user import Question
from ..chatdata import BehaviorData


def get_from_database_chatdata():
    data_chat = BehaviorData()
    user_request = 'connais tu openClassRooms'
    data = {
        'user_request': user_request,
        'parsed': 'openClassrooms paris',
        'question': Question(user_request, data_chat),
        'data_discussion': data_chat
    }
    return data

def get_mockreturn(result):
    """
        mock template call
    """
    def mock_get(url, params):
        """
            Mock function on api object
        """
        class JsonResponse:
            """
                mock result in JSON format
            """
            @staticmethod
            def json():
                """
                    Json method
                """
                return result
        return JsonResponse()
    return mock_get

class TestUserBehaviorChat:
    """
         management of test user's question
         user behavior management
            - Politeness
            - Comprehension
    """
    def setup_method(self):
        self.data = get_from_database_chatdata()

    def test_parser(self):
        """
            Test function on the separation of the character string (question asked
            a papyRobot alias grandPy) in several words,
            removing unnecessary words in order to keep the keywords for the
            search (location history & geographic coordinates)
        """ 
        data = self.data
        demand = data['question'].parser(data['user_request'])
        # question asked to grandPy
        result_parsed = 'openClassRooms'
        assert demand == result_parsed

    def test_civility(self):
        """
            civility function test
        """
        data = self.data
        demand = data['question'].user_civility()
        assert demand == data['data_discussion'].civility
        other_demand = Question('bonjour', data['data_discussion']).user_civility()
        assert other_demand == data['data_discussion'].civility

    def test_decency(self):
        """
            decency function test
        """
        data = self.data
        demand = data['question'].user_decency()
        assert demand == data['data_discussion'].decency
        other_demand = Question('fossile', data['data_discussion']).user_decency()
        assert other_demand == data['data_discussion'].decency

    def test_comprehension(self):
        """
            comprehension function test
        """
        data = self.data
        demand = data['question'].user_comprehension()
        assert demand == data['data_discussion'].comprehension
        other_demand =\
            Question('cvccc', data['data_discussion']).user_comprehension()
        assert other_demand == data['data_discussion'].comprehension


    # ~ def test_address_conversion(self, monkeypatch):
        # ~ """
            # ~ comma deletion, convert to lowercase, convert to list
        # ~ """
        # ~ address = self.data['parsed']
        # ~ converted_result =\
            # ~ ['10','quai','de','la','charente','75019','paris','france']
        
        # ~ wiki_data = WikiMediaAddressProcessing(address)
        # ~ demand = wiki_data.get_from_list_address_convertion()

        # ~ mockreturn = get_mockreturn('converted_result')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand == converted_result

    # ~ def test_common_list(self):
        # ~ """
            # ~ determine the address
            # ~ of the common wikipedia page
            # ~ with the googleMap address
        # ~ """
        # ~ lst_wiki = [
            # ~ ['Quai', 'de', 'la', 'Gironde'],
            # ~ ['Parc', 'du', 'Pont', 'de', 'Flandre'],
            # ~ ['Square', 'du', 'Quai-de-la-Gironde'],    
            # ~ ['Avenue', 'Corentin-Cariou'],
            # ~ ['Porte', 'de', 'la', 'Villette', '(métro', 'de', 'Paris)'],
            # ~ ['Quai', 'de', 'la', 'Charente'],
            # ~ ['Porte', 'de', 'la', 'Villette'],
            # ~ ['Rue', 'Benjamin-Constant'],
            # ~ ['Quai', 'du', 'Lot'],
            # ~ ['Gare', 'du', 'pont', 'de', 'Flandre']
        # ~ ]
        # ~ lst_address = [
            # ~ '10','quai','de','la','charente','75019','paris','france'
        # ~ ]
        # ~ wiki_data = WikiMediaAddressProcessing(lst_address)
        # ~ demand = wiki_data.get_from_common_list_creation()
        # ~ common_result = 'Quai de la Charente'
        # ~ assert demand == common_result
