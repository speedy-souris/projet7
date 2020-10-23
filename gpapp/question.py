#coding:utf-8
#!/usr/bin/env python

import os

import inspect


                            #==============
                            # Script class
                            #==============
# question organization
class UserQuestion:
    """
        organization of the user's question
    """

    # constructor
    def __init__(self, params):
        """
            constructor
                organization of the user's question
        """
        self.params = params

    #=================
    # user's civility
    #=================
    def user_civility(self):
        """
            modification of attributes civility ==> parser
        """
        # list of words to find in questions
        user_answer = self.params.tmp.split()
        # search civility
        result = bool(
            [
            w for w in user_answer if w.lower() in self.params.DONNEE_CIVILITY
            ]
        )
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('user_civility'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.historical(result, 'civility'))

        self.params.civility = result
        self.params.write_civility(self.params.civility)


    #=================
    # user's decency
    #=================
    def user_decency(self):
        """
            modification of attributes decency ==> parser
        """
        # list of words to find in questions
        user_answer = self.params.tmp.split()
        # search decency
        result = bool(
            [
            w for w in user_answer if w.lower() not in self.params.INDECENCY_LIST
            ]
        )
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('user_decency'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.historical(result, 'decency'))

        self.params.decency = result
        self.params.write_decency(self.params.decency)


    #=========================
    # Grandpy incomprehension
    #=========================
    def user_comprehension(self):
        """
            modification of attributes comprehension ==> parser
        """
        # list of words to find in questions
        user_answer = self.params.tmp.split()
        # search comprehension
        result = bool(
            [
            w for w in user_answer if w.lower() in self.params.DONNEE_CIVILITY
                or w.lower() in self.params.INDECENCY_LIST
                or w.lower() in self.params.UNNECESSARY_LIST
            ]
        )
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('user_comprehension'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(self.params.debug.historical(result, 'comprehension'))
            
        self.params.comprehension = result
        self.params.write_comprehension(self.params.comprehension)


    #===============
    # question user
    #===============
    def question_user(self):
        """
            added last post from user
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('question_user'))
        label = f'Question de user ==> '
        requete_user = input(label)
        return requete_user


