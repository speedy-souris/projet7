#coding:utf-8
#!/usr/bin/env python

from ..chatdata import Chat

class TestLocalDataValue:
    def setup_method(self):
        self.initialized_value = Chat(None)

    def test_initialization_dedault_database_value_by_database(self):
        self.initialized_value.behavior_data.get_initial_database()
        result_database_quotas_value =\
            self.initialized_value.behavior_data.read_user_request_quotas
        result_database_incomprehension_value =\
            self.initialized_value.behavior_data.\
            read_counter_of_number_of_user_incomprehension
        result_database_civility_value =\
            self.initialized_value.behavior_data.read_user_civility
        result_database_decency_value =\
            self.initialized_value.behavior_data.read_user_decency
        result_database_comprehension =\
            self.initialized_value.behavior_data.read_user_comprehension
        
        assert result_database_quotas_value == False
        assert result_database_incomprehension_value == False
        assert result_database_civility_value == False
        assert result_database_decency_value == False
        assert result_database_comprehension == False

    def test_initialization_dedault_database_counting_by_database(self):
        self.initialized_value.behavior_data.get_initial_database()
        result_database_request_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_request
        result_database_incivility_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_incivility
        result_database_indecency_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_indecency
        result_database_incomprehension_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_incomprehension

        assert result_database_request_value == 0
        assert result_database_incivility_value == 0
        assert result_database_indecency_value == 0
        assert result_database_incomprehension_value == 0

    def test_initialization_dedault_database_value_by_local_data(self):
        self.initialized_value.behavior_data.get_initial_attribute()
        result_database_quotas_value =\
            self.initialized_value.behavior_data.read_user_request_quotas
        result_database_incomprehension_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_incomprehension
        result_database_civility_value =\
            self.initialized_value.behavior_data.read_user_civility
        result_database_decency_value = self.initialized_value.behavior_data.read_user_decency
        result_database_comprehension =\
            self.initialized_value.behavior_data.read_user_comprehension
        
        assert result_database_quotas_value == False
        assert result_database_incomprehension_value == False
        assert result_database_civility_value == False
        assert result_database_decency_value == False
        assert result_database_comprehension == False

    def test_initialization_dedault_database_counting_by_local_data(self):
        self.initialized_value.behavior_data.get_initial_attribute()
        result_database_request_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_request
        result_database_incivility_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_incivility
        result_database_indecency_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_indecency
        result_database_incomprehension_value =\
            self.initialized_value.behavior_data.read_counter_of_number_of_user_incomprehension

        assert result_database_request_value == 0
        assert result_database_incivility_value == 0
        assert result_database_indecency_value == 0
        assert result_database_incomprehension_value == 0

