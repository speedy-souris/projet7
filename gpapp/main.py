#coding:utf-8
#!/usr/bin/env python

import os

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
    params.reset_behavior()
    # waiting for user question
    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_presentation_user'))
        print(
           f'{params.debug.nb_line(inspect.currentframe().f_lineno)} ATTENTE QUESTION'
        )
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('user_request', type(persona).__name__))
    return_user = persona.user_request()

    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_presentation_user'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('add_message', type(params).__name__))
    params.add_message(return_user, params.user)
    
    # determines the comprehension value in the user question
    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_presentation_user'))
        print(
            f'{params.debug.nb_line(inspect.currentframe().f_lineno)} CHECK COMPORTEMENT'
        )
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('comprehension_check', type(persona).__name__))
    persona.comprehension_check()

    # determines the civility value in the user question
    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_presentation_user'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('civility_check', type(persona).__name__))
    persona.civility_check()

    # determines the decency value in the user question
    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_presentation_user'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('decency_check', type(persona).__name__))
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
    params.reset_behavior()
    # waiting for user question
    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_question_user'))
        print(
            f'{params.debug.nb_line(inspect.currentframe().f_lineno)} ATTENTE QUESTION'
        )
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('user_request', type(persona).__name__))
    return_user = persona.user_request()

    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_question_user'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('add_message', type(params).__name__))
    params.add_message(return_user, params.user)

    # determines the comprehension value in the user question
    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_question_user'))
        print(
            f'{params.debug.nb_line(inspect.currentframe().f_lineno)} CHECK COMPORTEMENT'
        )
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('comprehension_check', type(persona).__name__))
    persona.comprehension_check()

    # determines the decency value in the user question
    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('check_question_user'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('decency_check', type(persona).__name__))
    persona.decency_check()

    return return_user


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
        if os.environ.get('DEBUG') == 'True':
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(params.debug.call('add_message', type(params).__name__))
        params.add_message(message, params.grandpy)

        # behavior analysis
        if os.environ.get('DEBUG') == 'True':
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(params.debug.call('check_presentation_user', 'check_presentation_user'))
        check_presentation_user(params, persona)

        # return line after testing
        if os.environ.get('DEBUG') == 'True':
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(f'{params.debug.return_line()} vers TEST DE CIVILITY')
        # analyze the value of indecency
        if not params.decency:
            params.nb_indecency += 1
            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('rude_request', type(persona).__name__))
            message = persona.rude_request()

            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('add_message', type(params).__name__))
            params.add_message(message, params.grandpy)
            if params.nb_indecency < 3:
                message = grandpy_message('disrespectful')

        # analyze the value of understand
        elif not params.comprehension:
            params.nb_incomprehension += 1
            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('incorrect_request', type(persona).__name__))
            message = persona.incorrect_request()

            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('add_message', type(params).__name__))
            params.add_message(message, params.grandpy)
            if params.nb_incomprehension < 3:
                message = grandpy_message('incomprehension')

        # analyze the value of incivility
        elif not params.civility:
            params.nb_incivility += 1
            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('unpoliteness_request', type(persona).__name__))
            message = persona.unpoliteness_request()
            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('add_message', type(params).__name__))
            params.add_message(message, params.grandpy)
            if params.nb_incivility < 3:
                message = grandpy_message('rudeness')

        else:
            break

        # incivility limit exceeded
        if params.nb_indecency < 3\
            and params.nb_incivility < 3\
            and params.nb_incomprehension < 3:

            print(f'\nRéponse de {params.grandpy} ==> {message}')
        if params.nb_incivility >= 3:
            message = persona.incivility_limit()

            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('add_message', type(params).__name__))
            params.add_message(message, params.grandpy)

        # indecency limit exceeded
        elif params.nb_indecency >= 3:
            message = persona.indecency_limit()

            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('add_message', type(params).__name__))
            params.add_message(message, params.grandpy)

        # incomprehesion limit exceeded
        elif params.nb_incomprehension >= 3:
            message = persona.incorrect_limit()

            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('add_message', type(params).__name__))
            params.add_message(message, params.grandpy)

    if os.environ.get('DEBUG') == 'True':
        print(params.debug.name('main'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(f'{params.debug.return_line()} aprés TEST DE CIVILITY')
    # grandpy response archiving
    if params.civility:
        params.reset_status()
        if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('waiting_request', type(persona).__name__))
        message = persona.waiting_request()
        while params.nb_indecency < 3\
            and params.nb_incomprehension < 3\
            and params.nb_request < 10:
            # grandpy response archiving
            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('add_message', type(params).__name__))
            params.add_message(message, params.grandpy)

            # behavior analysis
            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(params.debug.call('check_question_user', 'check_question_user'))
            message = check_question_user(params, persona)

            # return line after testing
            if os.environ.get('DEBUG') == 'True':
                print(params.debug.name('main'))
                print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                print(f'{params.debug.return_line()} vers TEST DE DECENCY')

            # analyze the value of indecency
            if not params.decency:
                params.nb_indecency += 1
                if os.environ.get('DEBUG') == 'True':
                    print(params.debug.name('main'))
                    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    print(params.debug.call('rude_request', type(persona).__name__))
                message = persona.rude_request()

                if os.environ.get('DEBUG') == 'True':
                    print(params.debug.name('main'))
                    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    print(params.debug.call('add_message', type(params).__name__))
                params.add_message(message, params.grandpy)

                if params.nb_indecency < 3:
                    message = grandpy_message('disrespectful')
                    print(f'Réponse de {params.grandpy} ==> {message}')

            # analyze the value of understand
            elif not params.comprehension:
                params.nb_incomprehension += 1
                if os.environ.get('DEBUG') == 'True':
                    print(params.debug.name('main'))
                    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    print(params.debug.call('incorrect_request', type(persona).__name__))

                message = persona.incorrect_request()
                if os.environ.get('DEBUG') == 'True':
                    print(params.debug.name('main'))
                    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    print(params.debug.call('add_message', type(params).__name__))
                params.add_message(message, params.grandpy)
                if params.nb_incomprehension < 3:
                    message = grandpy_message('incomprehension')
                    print(f'Réponse de {params.grandpy} ==> {message}')

            else:
                message = persona.expected_response()
                print(f'\nRéponse de {params.grandpy} ==> {message}')
                if os.environ.get('DEBUG') == 'True':
                    print(params.debug.name('main'))
                    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    print(params.debug.call('add_message', type(params).__name__))
                params.add_message(message, params.grandpy)
                params.nb_request += 1
                if os.environ.get('DEBUG') == 'True':
                    print(params.debug.name('main'))
                    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    print(params.debug.call('waiting_new_request', type(persona).__name__))
                message = persona.waiting_new_request()

                if os.environ.get('DEBUG') == 'True':
                    print(params.debug.name('main'))
                    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    print(params.debug.call('add_message', type(params).__name__))
                params.add_message(message, params.grandpy)

                if os.environ.get('DEBUG') == 'True':
                    print(params.debug.name('main'))
                    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    print(params.debug.call('check_question_user', 'check_question_user'))
                message = check_question_user(params, persona)

                if message == 'non':
                    break
                elif message == 'oui':
                    if os.environ.get('DEBUG') == 'True':
                        print(params.debug.name('main'))
                        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                        print(params.debug.call('waiting_request', type(persona).__name__))
                    message = persona.waiting_request()

                else:
                    while message == '' and params.nb_incomprehension < 3:
                        params.nb_incomprehension += 1
                        message = grandpy_message('invalid')
                        print(f'\nRéponse de {params.grandpy} ==> {message}')
                        params.add_message(message, params.grandpy)
                        message = check_question_user(params, persona)
                        params.add_message(message, params.grandpy)
                    if params.nb_incomprehension >= 3:
                        message = persona.incorrect_limit()
                        params.add_message(message, params.grandpy)
                    elif message == 'non':
                        break
                    elif message == 'oui':
                        message = persona.waiting_request()
                        #print(f'\nRéponse de {params.grandpy} ==> {message}')
                        #params.add_message(message, params.grandpy)
                        continue

    persona.reconnection_delay()

if __name__ == "__main__":

    var_debug = input("Tapez 'd' pour passer en debogage ... !")
    if var_debug == 'd':
        os.environ['DEBUG'] = "True"
    os.system('clear')
    main()


