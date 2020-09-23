#coding:utf-8
#!/usr/bin/env python

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
    # waiting for user question
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('user_request', type(persona).__name__))
    return_user = persona.user_request()
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('add_message', type(params).__name__))
    params.add_message(return_user, params.user)
    # determines the comprehension value in the user question
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('comprehension_check', type(persona).__name__))
    persona.comprehension_check()
    # determines the civility value in the user question
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('civility_check', type(persona).__name__))
    persona.civility_check()
    # determines the decency value in the user question
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('decency_check', type(persona).__name__))
    persona.decency_check()

def reconnect_parameter(params, response, persona):
    """
        reconnection parameter after 24h00
    """
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('add_message', type(params).__name__))
    params.add_message(response, params.grandpy)
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('reconnection_delay', type(persona).__name__))
    persona.reconnection_delay()

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
    # grandpy presentation archiving
    txt_home = "Bonjour Mon petit, en quoi puis-je t'aider ?"
    home = f'Accueil de {params.grandpy} ==> {txt_home}'
    print(f'\n{home}')
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.call('add_message', type(params).__name__))
    params.add_message(txt_home, params.grandpy)
    # behavior analysis
    presentation_user(params, persona)
    # return line after testing
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.return_line())
    # analyze the value of understanding
    while (
        params.nb_incomprehension < 3 and params.nb_incivility < 3
        and params.nb_indecency < 3 and not params.civility
    ):
        # decency
        if not params.decency:
            params.nb_indecency += 1
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(params.debug.call('rude_request', type(persona).__name__))
            question = persona.rude_request()
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(params.debug.call('add_message', type(params).__name__))
            params.add_message(question, params.grandpy)
            # behavior analysis
            presentation_user(params, persona)
        # comprehension
        elif not params.comprehension:
            params.nb_incomprehension += 1
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(params.debug.call('incorrect_request', type(persona).__name__))
            response = persona.incorrect_request()
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(params.debug.call('add_message', type(params).__name__))
            params.add_message(response, params.grandpy)
            # behavior analysis
            presentation_user(params, persona)
        else:
            params.nb_incivility += 1
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(params.debug.call('unpoliteness_request', type(persona).__name__))
            response = persona. unpoliteness_request()
            print(params.debug.name('main'))
            print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            print(params.debug.call('add_message', type(params).__name__))
            params.add_message(response, params.grandpy)
            # behavior analysis
            presentation_user(params, persona)
    # return line after analisis
    print(params.debug.name('main'))
    print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
    print(params.debug.return_line())
    # conditions after the first analysis
    if params.nb_incomprehension > 3:
        print(params.debug.name('main'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('incorrect_limit', type(persona).__name__))
        response = persona.incorrect_limit()
        reconnect_parameter(params, response, persona)
    elif params.nb_incivility > 3:
        print(params.debug.name('main'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('incivility_limit', type(persona).__name__))
        response = persona.incivility_limit()
        reconnect_parameter(params, response, persona)
    elif params.nb_indecency > 3:
        print(params.debug.name('main'))
        print(params.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        print(params.debug.call('indecency_limit', type(persona).__name__))
        response = persona.indecency_limit()
        persona.reconnection_delay()
    else:
        params.reset_status()





if __name__ == "__main__":
    main()
