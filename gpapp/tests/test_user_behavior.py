#coding:utf-8
#!/usr/bin/env python

from ..chatdata import Chat

class TestUserBehavior:
    def setup_method(self):
        self.polite_user_behavior = Chat('bonjour')
        self.inpolite_user_behavior = Chat('ou se trouve openClassrooms')
        self.incomprehension_user_behavior = Chat('xxxx')
        self.rudeness_user_behavior = Chat('vieux')

    def test_should_return_the_parsed_user_query_value(self):
        parsed_content_return = self.inpolite_user_behavior.\
            obtain_processing_of_user_behavior_data('parser')

        assert parsed_content_return == 'openClassrooms'

    def test_should_return_user_civility(self):
        return_civility_true = self.polite_user_behavior.\
            obtain_processing_of_user_behavior_data('civility')
        return_civility_false = self.inpolite_user_behavior.\
            obtain_processing_of_user_behavior_data('civility')

        assert return_civility_true == True
        assert return_civility_false == False

    def test_should_return_user_decency(self):
        return_decency_true = self.polite_user_behavior.\
            obtain_processing_of_user_behavior_data('decency')
        return_decency_false = self.rudeness_user_behavior.\
            obtain_processing_of_user_behavior_data('decency')

        assert return_decency_true == True
        assert return_decency_false == False

    def test_should_return_user_comprehension(self):
        return_comprehension_true = self.polite_user_behavior.\
            obtain_processing_of_user_behavior_data('comprehension')
        return_comprehension_false = self.incomprehension_user_behavior.\
            obtain_processing_of_user_behavior_data('comprehension')

        assert return_comprehension_true == True
        assert return_comprehension_false == False
