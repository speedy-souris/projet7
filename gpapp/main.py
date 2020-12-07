#coding:utf-8
#!/usr/bin/env python

import os
import inspect

from .chat import Chat
from .chatData import Data
from .user import Question
from .grandpyRobot import Answer
from .answerSearch import Research
from .debug import Debugging

def check_presentation_user(discussion, dataDiscussion):
    """
        user presentation analysis
    """
    dataDiscussion.reset_behavior()
    discussion.comprehension_check()
    discussion.civility_check()
    discussion.decency_check()

def grandpy_message(stage=None):
    if stage == 'incomprehension':
        message =\
            "Ha, repose ta user, je n'ai pas bien compris ce que tu veux dire ... !"
    elif stage == 'rudeness':
        message =\
            "s'il te plait, reformule ta user en étant plus polis ... ! "
    elif stage == 'disrespectful':
        message =\
            "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !"
    elif stage == 'invalid':
        message = 'Répond à la user par <oui> ou par <non> ... !'
    else:
        message = "Bonjour Mon petit, en quoi puis-je t'aider ?"

    return message 

def check_question_user(discussion):
    """
        user question analysis
    """
    dataDiscussion.reset_behavior()
    discussion.comprehension_check()
    discussion.decency_check()

    return return_user


# script execution
def main(question):
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    # awaits the courtesy of the user
    debug = Debugging()
    dataDiscussion = Data()
    user = Question(question, dataDiscussion)
    research = Research(user, dataDiscussion)
    grandpy = Answer(dataDiscussion, research)
    discussion = Chat(user, grandpy)

    if dataDiscussion.nb_incivility < 3\
        and dataDiscussion.nb_incomprehension < 3\
        and dataDiscussion.nb_indecency <3:
        # behavior analysis
        check_presentation_user(discussion, dataDiscussion)
        # analyze the value of indecency
        print(f'comprehension ==> {dataDiscussion.comprehension}')
        print(f'civility ==> {dataDiscussion.civility}')
        print(f'decency ==> {dataDiscussion.decency}')
        if dataDiscussion.civility:
            dataDiscussion.grandpy_response = discussion.waiting_request()
        elif not dataDiscussion.civility and dataDiscussion.decency:
            dataDiscussion.grandpy_response = discussion.unpoliteness_request()
        elif not dataDiscussion.decency:
            dataDiscussion.grandpy_response = discussion.rude_request()
        else:
            dataDiscussion.grandpy_response = discussion.incorrect_request()

    dataDiscussion.update_data()
    return dataDiscussion


    
    # ~ while history.nb_incivility < 3\
        # ~ and history.nb_indecency < 3\
        # ~ and history.nb_incomprehension < 3:
        # ~ # grandpy response archiving
        # ~ if os.environ.get('DEBUG') == 'True':
            # ~ print(history.debug.name('main'))
            # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            # ~ print(history.debug.call('add_message', type(history).__name__))
        # ~ history.add_message(message, history.grandpy)

        # ~ # behavior analysis
        # ~ if os.environ.get('DEBUG') == 'True':
            # ~ print(history.debug.name('main'))
            # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            # ~ print(history.debug.call('check_presentation_user', 'check_presentation_user'))
        # ~ check_presentation_user(history, discussion)

        # ~ # return line after testing
        # ~ if os.environ.get('DEBUG') == 'True':
            # ~ print(history.debug.name('main'))
            # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
            # ~ print(f'{history.debug.return_line()} vers TEST DE CIVILITY')
        # ~ # analyze the value of indecency
        # ~ if not history.decency:
            # ~ history.nb_indecency += 1
            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('rude_request', type(discussion).__name__))
            # ~ message = discussion.rude_request()

            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('add_message', type(history).__name__))
            # ~ history.add_message(message, history.grandpy)
            # ~ if history.nb_indecency < 3:
                # ~ message = grandpy_message('disrespectful')

        # ~ # analyze the value of understand
        # ~ elif not history.comprehension:
            # ~ history.nb_incomprehension += 1
            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('incorrect_request', type(discussion).__name__))
            # ~ message = discussion.incorrect_request()

            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('add_message', type(history).__name__))
            # ~ history.add_message(message, history.grandpy)
            # ~ if history.nb_incomprehension < 3:
                # ~ message = grandpy_message('incomprehension')

        # ~ # analyze the value of incivility
        # ~ elif not history.civility:
            # ~ history.nb_incivility += 1
            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('unpoliteness_request', type(discussion).__name__))
            # ~ message = discussion.unpoliteness_request()
            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('add_message', type(history).__name__))
            # ~ history.add_message(message, history.grandpy)
            # ~ if history.nb_incivility < 3:
                # ~ message = grandpy_message('rudeness')

        # ~ else:
            # ~ break

        # ~ # incivility limit exceeded
        # ~ if history.nb_indecency < 3\
            # ~ and history.nb_incivility < 3\
            # ~ and history.nb_incomprehension < 3:

            # ~ print(f'\nRéponse de {history.grandpy} ==> {message}')
        # ~ if history.nb_incivility >= 3:
            # ~ message = discussion.incivility_limit()

            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('add_message', type(history).__name__))
            # ~ history.add_message(message, history.grandpy)

        # ~ # indecency limit exceeded
        # ~ elif history.nb_indecency >= 3:
            # ~ message = discussion.indecency_limit()

            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('add_message', type(history).__name__))
            # ~ history.add_message(message, history.grandpy)

        # ~ # incomprehesion limit exceeded
        # ~ elif history.nb_incomprehension >= 3:
            # ~ message = discussion.incorrect_limit()

            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('add_message', type(history).__name__))
            # ~ history.add_message(message, history.grandpy)

    # ~ if os.environ.get('DEBUG') == 'True':
        # ~ print(history.debug.name('main'))
        # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
        # ~ print(f'{history.debug.return_line()} aprés TEST DE CIVILITY')
    # ~ # grandpy response archiving
    # ~ if history.civility:
        # ~ history.reset_status()
        # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('waiting_request', type(discussion).__name__))
        # ~ message = discussion.waiting_request()
        # ~ while history.nb_indecency < 3\
            # ~ and history.nb_incomprehension < 3\
            # ~ and history.nb_request < 10:
            # ~ # grandpy response archiving
            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('add_message', type(history).__name__))
            # ~ history.add_message(message, history.grandpy)

            # ~ # behavior analysis
            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(history.debug.call('check_question_user', 'check_question_user'))
            # ~ message = check_question_user(history, discussion)

            # ~ # return line after testing
            # ~ if os.environ.get('DEBUG') == 'True':
                # ~ print(history.debug.name('main'))
                # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                # ~ print(f'{history.debug.return_line()} vers TEST DE DECENCY')

            # ~ # analyze the value of indecency
            # ~ if not history.decency:
                # ~ history.nb_indecency += 1
                # ~ if os.environ.get('DEBUG') == 'True':
                    # ~ print(history.debug.name('main'))
                    # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    # ~ print(history.debug.call('rude_request', type(discussion).__name__))
                # ~ message = discussion.rude_request()

                # ~ if os.environ.get('DEBUG') == 'True':
                    # ~ print(history.debug.name('main'))
                    # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    # ~ print(history.debug.call('add_message', type(history).__name__))
                # ~ history.add_message(message, history.grandpy)

                # ~ if history.nb_indecency < 3:
                    # ~ message = grandpy_message('disrespectful')
                    # ~ print(f'Réponse de {history.grandpy} ==> {message}')

            # ~ # analyze the value of understand
            # ~ elif not history.comprehension:
                # ~ history.nb_incomprehension += 1
                # ~ if os.environ.get('DEBUG') == 'True':
                    # ~ print(history.debug.name('main'))
                    # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    # ~ print(history.debug.call('incorrect_request', type(discussion).__name__))

                # ~ message = discussion.incorrect_request()
                # ~ if os.environ.get('DEBUG') == 'True':
                    # ~ print(history.debug.name('main'))
                    # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    # ~ print(history.debug.call('add_message', type(history).__name__))
                # ~ history.add_message(message, history.grandpy)
                # ~ if history.nb_incomprehension < 3:
                    # ~ message = grandpy_message('incomprehension')
                    # ~ print(f'Réponse de {history.grandpy} ==> {message}')

            # ~ else:
                # ~ message = discussion.expected_response()
                # ~ print(f'\nRéponse de {history.grandpy} ==> {message}')
                # ~ if os.environ.get('DEBUG') == 'True':
                    # ~ print(history.debug.name('main'))
                    # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    # ~ print(history.debug.call('add_message', type(history).__name__))
                # ~ history.add_message(message, history.grandpy)
                # ~ history.nb_request += 1
                # ~ if os.environ.get('DEBUG') == 'True':
                    # ~ print(history.debug.name('main'))
                    # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    # ~ print(history.debug.call('waiting_new_request', type(discussion).__name__))
                # ~ message = discussion.waiting_new_request()

                # ~ if os.environ.get('DEBUG') == 'True':
                    # ~ print(history.debug.name('main'))
                    # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    # ~ print(history.debug.call('add_message', type(history).__name__))
                # ~ history.add_message(message, history.grandpy)

                # ~ if os.environ.get('DEBUG') == 'True':
                    # ~ print(history.debug.name('main'))
                    # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                    # ~ print(history.debug.call('check_question_user', 'check_question_user'))
                # ~ message = check_question_user(history, discussion)

                # ~ if message == 'non':
                    # ~ break
                # ~ elif message == 'oui':
                    # ~ if os.environ.get('DEBUG') == 'True':
                        # ~ print(history.debug.name('main'))
                        # ~ print(history.debug.nb_line(inspect.currentframe().f_lineno+2), end=' ==> ')
                        # ~ print(history.debug.call('waiting_request', type(discussion).__name__))
                    # ~ message = discussion.waiting_request()

                # ~ else:
                    # ~ while message == '' and history.nb_incomprehension < 3:
                        # ~ history.nb_incomprehension += 1
                        # ~ message = grandpy_message('invalid')
                        # ~ print(f'\nRéponse de {history.grandpy} ==> {message}')
                        # ~ history.add_message(message, history.grandpy)
                        # ~ message = check_question_user(history, discussion)
                        # ~ history.add_message(message, history.grandpy)
                    # ~ if history.nb_incomprehension >= 3:
                        # ~ message = discussion.incorrect_limit()
                        # ~ history.add_message(message, history.grandpy)
                    # ~ elif message == 'non':
                        # ~ break
                    # ~ elif message == 'oui':
                        # ~ message = discussion.waiting_request()
                        # ~ continue

    # ~ discussion.reconnection_delay()

if __name__ == "__main__":

    # ~ var_debug = input("Tapez 'd' pour passer en debogage ... !")
    # ~ if var_debug == 'd':
        # ~ os.environ['DEBUG'] = "True"
    # ~ os.system('clear')
    # ~ main('bonjour')
    pass


