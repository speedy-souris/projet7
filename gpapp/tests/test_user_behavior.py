#coding:utf-8
#!/usr/bin/env python

from ..main import CheckUserBehavior

class TestUserBehavior:
    def setup_method(self):
        self.polite_user_behavior = CheckUserBehavior('bonjour')
        self.inpolite_user_behavior =\
            CheckUserBehavior('ou se trouve openClassrooms')
        self.incomprehension_user_behavior = CheckUserBehavior('xxxx')
        self.rudeness_user_behavior = CheckUserBehavior('vieux')

    def test_should_return_the_parsed_user_query_value(self):
        assert self.inpolite_user_behavior.\
            user_request_parse() == 'openClassrooms'

    def test_should_return_user_civility(self):
        assert self.polite_user_behavior.user_civility() == True
        assert self.inpolite_user_behavior.user_civility() == False

    def test_should_return_user_decency(self):
        assert self.polite_user_behavior.user_decency() == True
        assert self.rudeness_user_behavior.user_decency() == False

    def test_should_return_user_comprehension(self):
        assert self.polite_user_behavior.user_comprehension() == True
        assert self.incomprehension_user_behavior.user_comprehension() == False
