#coding:utf-8
#!/usr/bin/env python

import os

import inspect


                           #==============
                           # Script class
                           #==============
# chat organization
class Chat:
    """
        object management class
    """
    #===========================
    # Constructor of Chat class
    #===========================
    def __init__(self, user, grandpy, params):
        """
            constructor
                - user object
                - grandpy objet
                - parameter object
        """
        self.user = user
        self.grandpy = grandpy
        self.params = params

    #===============
    # user property
    #===============
    # wait user question
    def user_request(self):
        """
            call waiting for user request
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('user_request'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('question_user', 'UserQuestion'))

        return self.user.question_user()

    # civility test
    def civility_check(self):
        """
            call for civility check
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('civility_check'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('user_civility', 'UserQuestion'))
            
        self.user.user_civility()

    # decency test
    def decency_check(self):
        """
            call for decency check
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('decency_check'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('user_decency', 'UserQuestion'))
        
        self.user.user_decency()

    # comprehension test
    def comprehension_check(self):
        """
            call for comprehension check
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('comprehension_check'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('user_comprehension', 'UserQuestion'))

        self.user.user_comprehension()

    #==================
    # grandpy property
    #==================
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
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('reconnection_delay'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('reconnection', 'GpAnswer'))

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
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('indecency_limit'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('stress_indecency', 'GpAnswer'))

        return self.grandpy.stress_indecency()

    # over the user incivility limit 
    def incivility_limit(self):
        """
            call for grandpy's reaction ==> too much user incivility
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('incivility_limit'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('stress_incivility', 'GpAnswer'))

        return self.grandpy.stress_incivility()

    # over the user incomprehension limit 
    def incorrect_limit(self):
        """
            call for grandpy's reaction ==> too much user incomprehension
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('incorrect_limit'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('stress_incomprehension', 'GpAnswer'))

        return self.grandpy.stress_incomprehension()

    # user rude request
    def rude_request(self):
        """
            call for rude user
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('rude_request'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('rude_user', 'GpAnswer'))

        return self.grandpy.rude_user()

    # user unpoliteness 
    def unpoliteness_request(self):
        """
            call for unpoliteness user
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('unpoliteness_request'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('unpoliteness_user', 'GpAnswer'))

        return self.grandpy.unpoliteness_user()

    # user error
    def incorrect_request(self):
        """
            call for user incomprehension
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('incorrect_request'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.call('question_incorrect', 'GpAnswer'))

        return self.grandpy.question_incorrect()

