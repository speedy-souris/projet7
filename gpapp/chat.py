#coding:utf-8
#!/usr/bin/env python

import inspect


                           #==============
                           # Script class
                           #==============
# Redis server organization
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
                - user
                - grandpy
        """
        self.user = user
        self.grandpy = grandpy
        self.params = params

    #===============
    # user property
    #===============
    def user_request(self):
        """
            call waiting for user request
        """
        print(self.params.debug.name('user_request'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('question_user', 'UserQuestion'))
        return self.user.question_user()

    def civility_check(self):
        """
            call for civility check
        """
        print(self.params.debug.name('civility_check'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('user_civility', 'UserQuestion'))
        self.user.user_civility()

    def decency_check(self):
        """
            call for decency check
        """
        print(self.params.debug.name('decency_check'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('user_decency', 'UserQuestion'))
        self.user.user_decency()

    def comprehension_check(self):
        """
            call for comprehension check
        """
        print(self.params.debug.name('comprehension_check'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('user_comprehension', 'UserQuestion'))
        self.user.user_comprehension()

    #==================
    # grandpy property
    #==================
    def grandpy_reply(self):
        """
            call for grandpy's answer
        """
        self.grandpy.answer_returned

    def reconnection_delay(self):
        """
            call for the 24:00 stop
        """
        print(self.params.debug.name('reconnection_delay'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('reconnection', 'GpAnswer'))
        self.grandpy.reconnection()

    def waiting_request(self):
        """
            call to wait for grandpy ==> response asked to the user
        """
        self.grandpy.waiting_question()

    def indecency_limit(self):
        """
            call for grandpy's reaction ==> too much user indecency
        """
        print(self.params.debug.name('indecency_limit'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('stress_indecency', 'GpAnswer'))
        return self.grandpy.stress_indecency()

    def incivility_limit(self):
        """
            call for grandpy's reaction ==> too much user incivility
        """
        print(self.params.debug.name('incivility_limit'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('stress_incivility', 'GpAnswer'))
        return self.grandpy.stress_incivility()

    def incorrect_limit(self):
        """
            call for grandpy's reaction ==> too much user incomprehension
        """
        print(self.params.debug.name('incorrect_limit'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('stress_incomprehension', 'GpAnswer'))
        return self.grandpy.stress_incomprehension()

    def rude_request(self):
        """
            call for rude user
        """
        print(self.params.debug.name('rude_request'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('rude_user', 'GpAnswer'))
        return self.grandpy.rude_user()

    def unpoliteness_request(self):
        """
            call for unpoliteness user
        """
        print(self.params.debug.name('unpoliteness_request'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('unpoliteness_user', 'GpAnswer'))
        return self.grandpy.unpoliteness_user()

    def incorrect_request(self):
        """
            call for user incomprehension
        """
        print(self.params.debug.name('incorrect_request'))
        print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(self.params.debug.call('question_incorrect', 'GpAnswer'))
        return self.grandpy.question_incorrect()
