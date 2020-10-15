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
def presentation_user(params, persona):
    """
        user presentation analysis
    """
    # initialization of user behavior data values
    params.comprehension = False
    params.civility = False
    params.decency = False
    # waiting for user question
    print(params.debug.name('presentation_user'))
    print(
        f'{params.debug.nb_line(inspect.currentframe().f_lineno)} ATTENTE QUESTION'
    )
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('user_request', type(persona).__name__))
    return_user = persona.user_request()
    print(params.debug.name('presentation_user'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('add_message', type(params).__name__))
    params.add_message(return_user, params.user)
    # determines the comprehension value in the user question
    print(params.debug.name('presentation_user'))
    print(
        f'{params.debug.nb_line(inspect.currentframe().f_lineno)} CHECK COMPORTEMENT'
    )
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('comprehension_check', type(persona).__name__))
    persona.comprehension_check()
    # determines the civility value in the user question
    print(params.debug.name('presentation_user'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('civility_check', type(persona).__name__))
    persona.civility_check()
    # determines the decency value in the user question
    print(params.debug.name('presentation_user'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('decency_check', type(persona).__name__))
    persona.decency_check()
    if not params.civility or not params.comprehension or not params.decency:
        params.counter_request += 1

def reconnect_parameter(params, response, persona):
    """
        reconnection parameter after 24h00
    """
    print(params.debug.name('reconnect_parameter'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('add_message', type(params).__name__))
    params.add_message(response, params.grandpy)
    print(params.debug.name('reconnect_parameter'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('reconnection_delay', type(persona).__name__))
    persona.reconnection_delay()

def grandpy_message(stage=None):
    if stage == 'incomprehension':
        message = \
            "Ha, repose ta question, je n'ai pas bien compris ce que tu veux dire ... !"
    elif stage == 'rudeness':
        message = "s'il te plait, reformule ta question en étant plus polis ... ! "
    elif stage == 'disrespectful':
        message = "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !"
    elif stage == 'correct':
        message = 'Hey bien, tu peux me poser ta question maintenant ... ! '
    else:
        message = "Bonjour Mon petit, en quoi puis-je t'aider ?"
    return message 
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
        print(params.debug.name('main'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('add_message', type(params).__name__))
        params.add_message(message, params.grandpy)
        # behavior analysis
        print(params.debug.name('main'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('presentation_user', 'presetation_user'))
        presentation_user(params, persona)
        # return line after testing
        print(params.debug.name('main'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(f'{params.debug.return_line()} vers TEST DE CIVILITY')
        # analyze the value of understand
        if not params.decency:
            params.nb_indecency += 1
            message = grandpy.rude_user()
            params.add_message(message, params.grandpy)
            message = grandpy_message('disrespectful')

        elif not params.comprehension:
            params.nb_incomprehension += 1
            message = grandpy.question_incorrect()
            params.add_message(message, params.grandpy)
            message = grandpy_message('incomprehension')

        elif not params.civility:
            params.nb_incivility += 1
            message = grandpy.unpoliteness_user()
            params.add_message(message, params.grandpy)
            message = grandpy_message('rudeness')

        else:
            break

        print(f'\nRéponse de {params.grandpy} ==> {message}')
        if params.nb_incivility >= 3:
            message = grandpy.stress_incivility()
            params.add_message(message, params.grandpy)
        elif params.nb_indecency >= 3:
            message = grandpy.stress_indecency()
            params.add_message(message, params.grandpy)
        elif params.nb_incomprehension >= 3:
            message = grandpy.stress_incomprehension()
            params.add_message(message, params.grandpy)

    if params.civility:
        params.reset_status()
        params.civility = True
        print(params.debug.name('main'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(f'{params.debug.return_line()} aprés TEST DE CIVILITY')

    grandpy.reconnection()


if __name__ == "__main__":
    main()


