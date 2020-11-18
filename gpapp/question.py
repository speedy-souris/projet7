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
        self.data_redis = self.params.data_redis

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

        self.data_redis.civility = result


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

        self.data_redis.decency = result


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
            
        self.data_redis.comprehension = result


    #========
    # parser
    #========
    def parser(self):
        """
            function that cuts the string of characters (question asked to GrandPy)
            into a word list then delete all unnecessary words to keep only
            the keywords for the search
        """

        # list of words to remove in questions
        list_question = self.params.tmp.split()
        result = [
            w for w in list_question if w.lower() not in self.params.UNNECESSARY_LIST
        ]

        return result

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


