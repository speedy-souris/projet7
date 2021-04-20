#coding:utf-8
#!/usr/bin/env python

from ..chatdata import UserBehaviorLimit

class TestUserRequestCounting:
    def initialization_of_count_data(self):
        self.default_count_data = UserBehaviorLimit('')
        self.default_count_data.request_quotas = False
        self.default_count_data.number_request = 0
        self.default_count_data.number_incivility = 0
        self.default_count_data.number_indecency = 0
        self.default_count_data.number_incomprehension = 0

    def setup_method(self):
        self.initialization_of_count_data()
        self.user_civility_data = UserBehaviorLimit('bonjour')
        self.civility_count_data = UserBehaviorLimit('OpenClassrooms')
        self.indecency_count_data = UserBehaviorLimit('vieux')
        self.incomprehension_count_data = UserBehaviorLimit('xxxx')
    def teardown_method(self):
        self.initialization_of_count_data()

    def test_should_return_user_civility(self):
        self.user_civility_data.user_request_civility()
        assert self.user_civility_data.user_civility == True

    def test_should_return_request_limit_if_all_user_behavior_true(self):
        while self.civility_count_data.number_request < 11:
            self.civility_count_data.number_request += 1
        self.civility_count_data.user_request_limit()
        assert  self.civility_count_data.request_quotas == True

    def test_should_return_request_limit_if_number_incivility_to_3(self):
        while self.civility_count_data.number_incivility < 3:
            self.civility_count_data.number_incivility += 1
        self.civility_count_data.user_incivility_limit()
        assert  self.civility_count_data.request_quotas == True

    def test_should_return_request_limit_if_number_indecency_to_3(self):
        while self.indecency_count_data.number_indecency < 3:
            self.indecency_count_data.number_indecency += 1
        self.indecency_count_data.user_indecency_limit() 
        assert self.indecency_count_data.request_quotas == True

    def \
        test_should_return_request_limit_if_number_incomprehension_to_3(self):
        while self.incomprehension_count_data.number_incomprehension < 3:
            self.incomprehension_count_data.number_incomprehension += 1

        assert self.incomprehension_count_data.user_incomprehension_limit() == True
