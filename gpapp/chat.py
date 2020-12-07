#coding:utf-8
#!/usr/bin/env python

import os
import inspect

# chat organization
class Chat:
    """
        object management class
    """
    # Constructor 
    def __init__(self, user, grandpy):
        """
            constructor
                - user object
                - grandpy objet
                - question
        """
        self.user = user
        self.grandpy = grandpy
#                  ~~~~~~~~~~~~~~~~~~
    def civility_check(self):
        """
            call for civility check
        """
        self.user.user_civility()

    def decency_check(self):
        """
            call for decency check
        """
        self.user.user_decency()

    def comprehension_check(self):
        """
            call for comprehension check
        """
        self.user.user_comprehension()


    # grandpy's reply
    def expected_response(self):
        """
            call for grandpy's answer
        """
        return self.grandpy.answer_returned()

    # absence of grandpy
    def reconnection_delay(self):
        """
            call for the 24:00 stop
        """
        self.grandpy.reconnection()

    # wait user courtesy 
    def waiting_request(self):
        """
            grandpy wait ==> response asked to the user
        """
        return self.grandpy.waiting_question()

    # wait user new question
    def waiting_new_request(self):
        """
            grandpy wait ==>  new response asked to the user
        """
        return self.grandpy.waiting_new_question()

    # over the user indecency limit 
    def indecency_limit(self):
        """
            call for grandpy's reaction ==> too much user indecency
        """
        return self.grandpy.stress_indecency()

    # over the user incivility limit 
    def incivility_limit(self):
        """
            call for grandpy's reaction ==> too much user incivility
        """
        return self.grandpy.stress_incivility()

    # over the user incomprehension limit 
    def incorrect_limit(self):
        """
            call for grandpy's reaction ==> too much user incomprehension
        """
        return self.grandpy.stress_incomprehension()

    # user rude request
    def rude_request(self):
        """
            call for rude user
        """
        return self.grandpy.rude_user()

    # user unpoliteness 
    def unpoliteness_request(self):
        """
            call for unpoliteness user
        """
        return self.grandpy.unpoliteness_user()

    # user error
    def incorrect_request(self):
        """
            call for user incomprehension
        """
        return self.grandpy.question_incorrect()

