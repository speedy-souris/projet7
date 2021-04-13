#coding:utf-8
#!/usr/bin/env python

from ..main import CheckUserBehavior

class TestDatabaseValue:
    def setup_method(self):
        self.default_database_value = CheckUserBehavior(user_question='')
        self.initialized_value = \
            self.default_database_value.get_processing_of_user_behavior_data

    def test_initialization_dedault_behavior_value(self):
        self.initialized_value.get_initial_database()
        result_user_civility = self.initialized_value.read_user_civility
        result_user_decency = self.initialized_value.read_user_decency
        result_user_comprehension = self.initialized_value.read_user_comprehension

        assert result_user_civility == False
        assert result_user_decency == False
        assert result_user_comprehension == False

    def test_initialization_dedault_counter_value(self):
        self.initialized_value.get_initial_database()
        result_number_request = self.initialized_value.\
            read_counter_of_number_of_user_request
        result_number_incivility = self.initialized_value.\
            read_counter_of_number_of_user_incivility
        result_number_indecency = self.initialized_value.\
            read_counter_of_number_of_user_indecency
        result_number_incomprehension = self.initialized_value.\
            read_counter_of_number_of_user_incomprehension

        assert result_number_request == 0
        assert result_number_incivility == 0
        assert result_number_indecency == 0
        assert result_number_incomprehension == 0
