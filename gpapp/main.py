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

def grandpy_message(stage=None):
    if stage == 'incomprehension':
        message =\
            "Ha, repose ta question, je n'ai pas bien compris ce que tu veux dire ... !"

    elif stage == 'rudeness':
        message =\
            "s'il te plait, reformule ta question en étant plus polis ... ! "

    elif stage == 'disrespectful':
        message =\
            "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !"

    elif stage == 'invalid':
        message = 'Répond à la user par <oui> ou par <non> ... !'

    else:
        message = "Bonjour Mon petit, en quoi puis-je t'aider ?"

    return message 

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
    grandpy = Answer(question, research)
    discussion = Chat(user, grandpy)

    dataDiscussion.reset_behavior()
    discussion.comprehension_check()
    if dataDiscussion.comprehension:
        discussion.decency_check()
        if dataDiscussion.decency and not dataDiscussion.civility:
            discussion.civility_check()
            if dataDiscussion.civility:
                dataDiscussion.init_value()
                dataDiscussion.grandpy_response = grandpy_message()
            else:
                dataDiscussion.grandpy_response = grandpy_message('rudeness')
                dataDiscussion.nb_incivility += 1
        elif not dataDiscussion.decency:
            dataDiscussion.grandpy_response = grandpy_message('disrespectful')
            dataDiscussion.nb_indecency += 1
        else:
            dataDiscussion.grandpy_response = discussion.expected_response()
            dataDiscussion.nb_request += 1
    else:
        dataDiscussion.grandpy_response = grandpy_message('incomprehension')
        dataDiscussion.nb_incomprehension += 1

    if dataDiscussion.nb_indecency >= 3:
        dataDiscussion.quotas = True
        dataDiscussion.grandpy_response = discussion.indecency_limit()

    if dataDiscussion.nb_incomprehension >= 3:
        dataDiscussion.quotas = True
        dataDiscussion.grandpy_response = discussion.incorrect_limit()

    if dataDiscussion.nb_incivility >= 3:
        dataDiscussion.quotas = True
        dataDiscussion.grandpy_response = discussion.incivility_limit()

    if dataDiscussion.nb_request > 0\
        and dataDiscussion.decency\
        and dataDiscussion.comprehension:
        dataDiscussion.grandpy_response = discussion.expected_response()

    dataDiscussion.update_data()
    return dataDiscussion


if __name__ == "__main__":

    # ~ var_debug = input("Tapez 'd' pour passer en debogage ... !")
    # ~ if var_debug == 'd':
        # ~ os.environ['DEBUG'] = "True"
    # ~ os.system('clear')
    # ~ main('bonjour')
    pass

