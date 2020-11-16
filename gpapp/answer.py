#coding:utf-8
#!/usr/bin/env python

import os
import inspect



                           #==============
                           # Script class
                           #==============
# Grandpy response
class GpAnswer:
    """
        organization of the grandpy's answer
    """
    def __init__(self, params):
        """
            constructor
               organization of the grandpy's answer
        """
        self.params = params

    #==================
    # response grandpy
    #==================
    def answer_returned(self):
        """
            response returned by grandpy for the courteous user
        """
        txt_returned = f'Voici Ta Réponse à la question {self.params.tmp} !'
        response = 'La Réponse est ... !'
        print(f'\nRéponse de {self.params.grandpy} ==> {txt_returned} :')
        self.params.add_message(txt_returned, self.params.grandpy)
        self.params.tmp_response = response
        return response


    #========================================
    # reconnection after 24 hours of waiting
    #========================================
    def reconnection(self):
        """
            stop questions and answers for 24 hours
        """
        txt_response = 'reviens me voir demain !'
        response = f'Réponse de {self.params.grandpy} ==> {txt_response}'
        self.params.tmp_response = txt_response
        print(f'\n{response}')
        self.params.add_message(txt_response, self.params.grandpy)
        print('\n----------------------------------------------------------------')
        print('-------- HISTORIQUE DE CONVERSATION ----------------------------')
        print('----------------------------------------------------------------')
        self.params.chat_viewer()
        print('----------------------------------------------------------------\n')
        self.params.display_status()
        self.params.init_message()
        self.params.quotas = True
        self.params.expiry_counter()


    #=================
    # attent question
    #=================
    def waiting_question(self):
        """
            waiting for user question
        """
        label = 'Hey bien, tu peux me poser ta question maintenant ... ! '
        response = f'Réponse de {self.params.grandpy} ==> {label}'
        self.params.tmp_response = label
        print(f'\n{response}')
        return label

    #=====================
    # attent new question
    #=====================
    def waiting_new_question(self):
        """
            waiting for user new question
        """
        label = 'As tu une nouvelle question a me demander ? '
        response = f'Réponse de {self.params.grandpy} ==> {label}'
        self.params.tmp_response = label
        print(f'\n{response}')
        return label

    #=====================
    # stress of indecency
    #=====================
    def stress_indecency(self):
        """
            stress of Grandpy
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('stress_indecency'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(f'Réponse de {self.params.grandpy}')
            
        txt_response = 'cette grossierete me FATIGUE ... !'
        response = f'Réponse de {self.params.grandpy} ==> {txt_response}'
        self.params.tmp_response = txt_response
        print(f'\n{response}')
        return txt_response


    #====================
    # stress of civility
    #====================
    def stress_incivility(self):
        """
            stress of Grandpy
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('stress_incivility'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(f'Réponse de {self.params.grandpy}')

        txt_response = 'cette impolitesse me FATIGUE ... !'
        response = f'Réponse de {self.params.grandpy} ==> {txt_response}'
        self.params.tmp_response = txt_response
        print(f'\n{response}')
        return txt_response


    #===========================
    # stress of incomprehension
    #===========================
    def stress_incomprehension(self):
        """
            stress of Grandpy
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('stress_incomprehension'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(f'Réponse de {self.params.grandpy}')

        txt_response = f'cette incomprehension me FATIGUE ... !'
        response = f'Réponse de {self.params.grandpy} ==> {txt_response}'
        self.params.tmp_response = txt_response
        print(f'\n{response}')
        return txt_response

    #=============
    # rude answer
    #=============
    def rude_user(self):
        """
            rude user
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('rude_user'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(f'Réponse de {self.params.grandpy}')

        txt_response = 'Si tu es grossier, je ne peux rien pour toi ... : '
        response = f'Réponse de {self.params.grandpy} ==> {txt_response}'
        self.params.tmp_response = txt_response
        print(f'\n{response}')
        return txt_response


    #===================
    # user unpoliteness
    #===================
    def unpoliteness_user(self):
        """
            user unpoliteness in the question for grandpy
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('unpoliteness_user'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(f'Réponse de {self.params.grandpy}')

        txt_response = 'Si tu es impoli, je ne peux rien pour toi ... : '
        response = f'Réponse de {self.params.grandpy} ==> {txt_response}'
        self.params.tmp_response = txt_response
        print(f'\n{response}')
        return txt_response


    #====================
    # incorrect question
    #====================
    def question_incorrect(self):
        """
                unknown words in the question
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.params.debug.name('question_incorrect'))
            print(self.params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(f'Réponse de {self.params.grandpy}')
            
        txt_response = "Je ne comprends pas, essaye d'être plus précis ... !"
        response = f'\nRéponse de {self.params.grandpy} ==> {txt_response}'
        self.params.tmp_response = txt_response
        print(f'{response}')
        return txt_response


