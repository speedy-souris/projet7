#coding:utf-8
#!/usr/bin/env python

from os import system

import inspect

from chat import Chat
from question import UserQuestion
from answer import GpAnswer
from parameter import QuestionParameter
from debug import Debugging

#===================
# utility functions
#===================
def check_presentation_user(params, persona):
    """
        user presentation analysis
    """
    # initialization of user behavior data values
    params.comprehension = False
    params.civility = False
    params.decency = False
    # waiting for user question
    #s1
    #print(params.debug.name('check_presentation_user'))
    #print(
     #   f'{params.debug.nb_line(inspect.currentframe().f_lineno)} ATTENTE QUESTION'
    #)
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('user_request', type(persona).__name__))
    #e1
    return_user = persona.user_request()
    #s2
    #print(params.debug.name('presentation_user'))
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('add_message', type(params).__name__))
    #e2
    params.add_message(return_user, params.user)
    # determines the comprehension value in the user question
    #s3
    #print(params.debug.name('presentation_user'))
    #print(
    #    f'{params.debug.nb_line(inspect.currentframe().f_lineno)} CHECK COMPORTEMENT'
    #)
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('comprehension_check', type(persona).__name__))
    #e4
    persona.comprehension_check()
    # determines the civility value in the user question
    #s5
    #print(params.debug.name('presentation_user'))
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('civility_check', type(persona).__name__))
    #e5
    persona.civility_check()
    # determines the decency value in the user question
    #s6
    #print(params.debug.name('presentation_user'))
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('decency_check', type(persona).__name__))
    #e6
    persona.decency_check()


def grandpy_message(stage=None):
    if stage == 'incomprehension':
        message = \
            "Ha, repose ta question, je n'ai pas bien compris ce que tu veux dire ... !"
    elif stage == 'rudeness':
        message = "s'il te plait, reformule ta question en étant plus polis ... ! "
    elif stage == 'disrespectful':
        message = "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !"
    elif stage == 'invalid':
        message = 'Répond à la question par <oui> ou par <non> ... !'
    else:
        message = "Bonjour Mon petit, en quoi puis-je t'aider ?"
    return message 

def check_question_user(params, persona):
    """
        user question analysis
    """
    # initialization of user behavior data values
    params.comprehension = False
    params.decency = False
    # waiting for user question
    #print(params.debug.name('presentation_user'))
    #print(
    #    f'{params.debug.nb_line(inspect.currentframe().f_lineno)} ATTENTE QUESTION'
    #)
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('user_request', type(persona).__name__))
    return_user = persona.user_request()
    #print(params.debug.name('check_presentation_user'))
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('add_message', type(params).__name__))
    params.add_message(return_user, params.user)
    # determines the comprehension value in the user question
    #print(params.debug.name('check_presentation_user'))
    #print(
    #    f'{params.debug.nb_line(inspect.currentframe().f_lineno)} CHECK COMPORTEMENT'
    #)
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('comprehension_check', type(persona).__name__))
    persona.comprehension_check()
    # determines the decency value in the user question
    #print(params.debug.name('check_presentation_user'))
    #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    #print(params.debug.call('decency_check', type(persona).__name__))
    persona.decency_check()


#=======================
# main script execution
#=======================
def main():
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    #---------------------------------
    # awaits the courtesy of the user
    #---------------------------------
    debug = Debugging()
    params = QuestionParameter(debug)
    user = UserQuestion(params)
    grandpy = GpAnswer(params)
    persona = Chat(user, grandpy, params)
    params.reset_status()
    # grandpy presentation archiving
    message = grandpy_message()
    print(f'Accueil de {params.grandpy} ==> {message}')
    while params.nb_incivility < 3\
        and params.nb_indecency < 3\
        and params.nb_incomprehension < 3:
        # grandpy response archiving
        #print(params.debug.name('main'))
        #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        #print(params.debug.call('add_message', type(params).__name__))
        params.add_message(message, params.grandpy)
        # behavior analysis
        #print(params.debug.name('main'))
        #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        #print(params.debug.call('check_presentation_user', 'check_presentation_user'))
        check_presentation_user(params, persona)
        # return line after testing
        #print(params.debug.name('main'))
        #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        #print(f'{params.debug.return_line()} vers TEST DE CIVILITY')
        # analyze the value of understand
        if not params.decency:
            params.nb_indecency += 1
            message = persona.rude_request()
            params.add_message(message, params.grandpy)
            message = grandpy_message('disrespectful')

        elif not params.comprehension:
            params.nb_incomprehension += 1
            message = persona.incorrect_request()
            params.add_message(message, params.grandpy)
            message = grandpy_message('incomprehension')

        elif not params.civility:
            params.nb_incivility += 1
            message = persona.unpoliteness_request()
            params.add_message(message, params.grandpy)
            message = grandpy_message('rudeness')

        else:
            break

        print(f'\nRéponse de {params.grandpy} ==> {message}')
        if params.nb_incivility >= 3:
            message = persona.incivility_limit()
            params.add_message(message, params.grandpy)
        elif params.nb_indecency >= 3:
            message = persona.indecency_limit()
            params.add_message(message, params.grandpy)
        elif params.nb_incomprehension >= 3:
            message = persona.incomprehension_limit()
            params.add_message(message, params.grandpy)

    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(f'{params.debug.return_line()} aprés TEST DE CIVILITY\n')
    # grandpy response archiving
    if params.civility:
        params.reset_status()
        params.civility = True
        message = persona.waiting_request()
        while params.nb_indecency < 3\
            and params.nb_incomprehension < 3\
            and params.nb_request < 10:
            # grandpy response archiving
            #print(params.debug.name('main'))
            #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            #print(params.debug.call('add_message', type(params).__name__))
            params.add_message(message, params.grandpy)
            # behavior analysis
            #print(params.debug.name('main'))
            #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            #print(params.debug.call('check_question_user', 'check_question_user'))
            check_question_user(params, persona)
            # return line after testing
            #print(params.debug.name('main'))
            #print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            #print(f'{params.debug.return_line()} vers TEST DE DECENCY')
            # analyze the value of understand
            if not params.decency:
                params.nb_indecency += 1
                message = persona.rude_request()
                params.add_message(message, params.grandpy)
                message = grandpy_message('disrespectful')

            elif not params.comprehension:
                params.nb_incomprehension += 1
                message = persona.incorrect_request()
                params.add_message(message, params.grandpy)
                message = grandpy_message('incomprehension')

            else:
                message = persona.expected_response()
                params.add_message(message, params.grandpy)
                params.nb_request += 1
                message = persona.waiting_new_request()
                params.add_message(message, params.grandpy)
                check_question_user(params, persona)
                if message == 'non':
                    break
                elif message == 'oui':
                    message = persona.waiting_request()
                else:
                    message = grandpy_message('invalid')
                    params.nb_incomprehension += 1

    persona.reconnection_delay()

if __name__ == "__main__":
    main()


