#coding:utf-8
#!/usr/bin/env python

from ..main import CheckUserBehavior

class TestDataConverter:
    def setup_method(self):
        self.default_converter_data_parameter =\
            CheckUserBehavior(user_question=None)

    def test_converter_string_to_booleen(self):
        value_true = self.default_converter_data_parameter.\
            get_processing_of_user_behavior_data.string_to_boolean_conversion('True')
        value_false = self.default_converter_data_parameter.\
            get_processing_of_user_behavior_data.\
            string_to_boolean_conversion('False')

        assert value_true == True
        assert value_false == False

    def test_converter_booleen_to_string(self):
        value_true = self.default_converter_data_parameter.\
            get_processing_of_user_behavior_data.boolean_to_string_conversion(True)
        value_false = self.default_converter_data_parameter.\
            get_processing_of_user_behavior_data.\
            boolean_to_string_conversion(False)

        assert value_true == 'True'
        assert value_false == 'False'

    def test_converter_string_to_int(self):
        value_string = self.default_converter_data_parameter.\
            get_processing_of_user_behavior_data.string_to_int_conversion('0')

        assert value_string == 0
