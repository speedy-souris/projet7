#coding:utf-8
#!/usr/bin/env python

from ..main import CheckUserBehavior

class TestUserRequestCounting:
    def initialization_of_count_data(self):
        self.default_count_data = CheckUserBehavior(user_question=None)
        self.default_count_data.get_processing_of_user_behavior_data.\
            request_quotas = False
        self.default_count_data.get_processing_of_user_behavior_data.\
            number_request = 0
        self.default_count_data.get_processing_of_user_behavior_data.\
            number_incivility = 0
        self.default_count_data.get_processing_of_user_behavior_data.\
            number_indecency = 0
        self.default_count_data.get_processing_of_user_behavior_data.\
            number_incomprehension = 0

    def setup_method(self):
        self.initialization_of_count_data()
    def teardown_method(self):
        self.initialization_of_count_data()
        
    def test_should_return_request_limit_if_all_user_behavior_true(self):
        while self.default_count_data.get_processing_of_user_behavior_data.\
            number_request < 11:
            self.default_count_data.get_processing_of_user_behavior_data.\
                number_request += 1

        assert self.default_count_data.user_request_limit() == True

    def test_should_return_request_limit_if_nb_incivility3(self):
        while self.default_count_data.get_processing_of_user_behavior_data.\
            number_incivility < 4:
            self.default_count_data.get_processing_of_user_behavior_data.\
                number_incivility += 1

        assert self.default_count_data.user_incivility_limit() == True

    def test_should_return_request_limit_if_nb_indecency3(self):
        while self.default_count_data.get_processing_of_user_behavior_data.\
            number_indecency < 4:
            self.default_count_data.get_processing_of_user_behavior_data.\
                number_indecency += 1

        assert self.default_count_data.user_indecency_limit() == True

    def test_should_return_request_limit_if_nb_incomprehension3(self):
        while self.default_count_data.get_processing_of_user_behavior_data.\
            number_incomprehension < 4:
            self.default_count_data.get_processing_of_user_behavior_data.\
                number_incomprehension += 1

        assert self.default_count_data.user_incomprehension_limit() == True
