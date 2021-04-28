#coding:utf-8
#!/usr/bin/env python

from ..chatdata import Chat

class TestLocalDataValue:
    def setup_method(self):
        self.initialized_value = Chat(None)

    def test_initialization_dedault_behavior_value_by_database(self):
        self.initialized_value.behavior_data.get_initial_database()
        result_quotas = self.initialized_value.behavior_data.request_quotas
        result_user_civility =\
            self.initialized_value.behavior_data.user_civility
        result_user_decency =\
            self.initialized_value.behavior_data.user_decency
        result_user_comprehension =\
            self.initialized_value.behavior_data.user_comprehension

        assert result_quotas == False
        assert result_user_civility == False
        assert result_user_decency == False
        assert result_user_comprehension == False

    def test_initialization_dedault_counter_value_by_database(self):
        self.initialized_value.behavior_data.get_initial_database()
        result_number_request =\
            self.initialized_value.behavior_data.number_request
        result_number_incivility =\
            self.initialized_value.behavior_data.number_incivility
        result_number_indecency = \
            self.initialized_value.behavior_data.number_indecency
        result_number_incomprehension =\
            self.initialized_value.behavior_data.number_incomprehension

        assert result_number_request == 0
        assert result_number_incivility == 0
        assert result_number_indecency == 0
        assert result_number_incomprehension == 0

    def test_initialization_dedault_behavior_value_by_local_data(self):
        self.initialized_value.behavior_data.get_initial_attribute()
        result_quotas = self.initialized_value.behavior_data.request_quotas
        result_user_civility =\
            self.initialized_value.behavior_data.user_civility
        result_user_decency =\
            self.initialized_value.behavior_data.user_decency
        result_user_comprehension =\
            self.initialized_value.behavior_data.user_comprehension

        assert result_quotas == False
        assert result_user_civility == False
        assert result_user_decency == False
        assert result_user_comprehension == False

    def test_initialization_dedault_counter_value_by_local_data(self):
        self.initialized_value.behavior_data.get_initial_attribute()
        result_number_request =\
            self.initialized_value.behavior_data.number_request
        result_number_incivility =\
            self.initialized_value.behavior_data.number_incivility
        result_number_indecency =\
            self.initialized_value.behavior_data.number_indecency
        result_number_incomprehension =\
            self.initialized_value.behavior_data.number_incomprehension

        assert result_number_request == 0
        assert result_number_incivility == 0
        assert result_number_indecency == 0
        assert result_number_incomprehension == 0

