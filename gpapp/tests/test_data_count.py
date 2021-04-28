#coding:utf-8
#!/usr/bin/env python

from ..main import main
from ..chatdata import Chat

class TestUserRequestCounting:
    def initialization_of_count_data(self):
        self.default_count_data = Chat(None)
        self.default_count_data.behavior_data.get_initial_attribute()

    def setup_method(self):
        self.initialization_of_count_data()
        self.user_civility_data = main('bonjour')
        self.civility_count_data = main('OpenClassrooms')
        # ~ self.indecency_count_data = Chat('vieux')
        # ~ self.incomprehension_count_data = Chat('xxxx')
    def teardown_method(self):
        self.initialization_of_count_data()

    def test_should_return_request_limit_if_all_user_behavior_true_0(self):
        assert self.user_civility_data.\
            get_grandpy_answer_processing('wait1') ==\
                "Bonjour Mon petit, en quoi puis-je t'aider ?" and\
                self.user_civility_data.behavior_data.grandpy_code == ''

    def test_should_return_request_value_if_user_behavior_true_4(self):
        while self.civility_count_data.behavior_data.number_request < 2:
            self.civility_count_data.behavior_data.number_request += 1
        assert self.civility_count_data.\
            get_grandpy_answer_processing('response') ==\
                'Voici Ta Réponse à la question !'

    def test_should_return_request_limit_if_all_user_behavior_true(self):
        while self.civility_count_data.behavior_data.number_request < 11:
            self.civility_count_data.behavior_data.number_request += 1
        self.civility_count_data.behavior_data.user_behavior_limited()
        assert  self.civility_count_data.behavior_data.request_quotas == True

    def test_should_return_request_limit_if_number_incivility_3(self):
        while self.civility_count_data.behavior_data.number_incivility < 3:
            self.civility_count_data.behavior_data.number_incivility += 1
        self.civility_count_data.behavior_data.user_behavior_limited()
        assert  self.civility_count_data.\
            behavior_data.request_quotas == True and \
            self.civility_count_data.\
            get_grandpy_answer_processing('incivility_limit') ==\
            'cette impolitesse me FATIGUE ... !' and \
            self.civility_count_data.behavior_data.grandpy_code == 'exhausted'

    # ~ def test_should_return_request_limit_if_number_indecency_3(self):
        # ~ while self.indecency_count_data.behavior_data.number_indecency < 3:
            # ~ self.indecency_count_data.behavior_data.number_indecency += 1
        # ~ self.indecency_count_data.behavior_data.user_behavior_data_limit() 
        # ~ assert self.indecency_count_data.\
            # ~ behavior_data.request_quotas == True and \
            # ~ self.indecency_count_data.\
            # ~ get_grandpy_answer_processing('indecency_limit') ==\
            # ~ 'cette grossierete me FATIGUE ... !' and \
            # ~ self.civility_count_data.behavior_data.grandpy_code == 'exhausted'


    # ~ def \
        # ~ test_should_return_request_limit_if_number_incomprehension_3(self):
        # ~ while self.incomprehension_count_data.behavior_data.number_incomprehension < 3:
            # ~ self.incomprehension_count_data.behavior_data.number_incomprehension += 1
        # ~ self.incomprehension_count_data.behavior_data.user_behavior_data_limit()
        # ~ assert self.incomprehension_count_data.behavior_data.request_quotas == True
