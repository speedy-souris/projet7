#coding:utf-8
#!/usr/bin/env python

import os
import inspect

from .debug import Debugging
from .chatData import BehaviorData
from .chatData import BehaviorDatabase
from .grandpyRobot import Answer
from .user import Question
from .chatData import Chat
from .answerSearch import Research



# script execution
def main(question):
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    # awaits the courtesy of the user
    debug = Debugging()
    dataDiscussion = BehaviorData()
    dataDB = BehaviorDatabase()
    grandpy = Answer()
    user = Question(question, dataDiscussion)
    discussion = Chat(user, grandpy)
    research = Research(discussion)

    dataDiscussion.reset_behavior()
    discussion.question('comprehension')
    if dataDiscussion.comprehension:
        discussion.question('decency')
        if dataDiscussion.decency and not dataDiscussion.civility:
            discussion.question('civility')
            if dataDiscussion.civility:
                dataDiscussion.reset_behavior()
                dataDiscussion.grandpy_response = discussion.answer('wait1')
                dataDiscussion.grandpy_code = ''
            else:
                dataDiscussion.display_data(44)
                dataDiscussion.grandpy_response = discussion.answer('mannerless')
                dataDiscussion.grandpy_code = 'mannerless'
                if dataDiscussion.nb_incivility >= 3:
                    dataDiscussion.nb_incility = 3
                else:
                    dataDiscussion.nb_incivility += 1
        elif not dataDiscussion.decency:
            dataDiscussion.grandpy_response = discussion.answer('disrespectful')
            dataDiscussion.grandpy_code = 'disrespectful'
            if dataDiscussion.nb_indecency >= 3:
                dataDiscussion.nb_indecency = 3
            else:
                dataDiscussion.nb_indecency += 1
        else:
            dataDiscussion.grandpy_response = discussion.answer('response')
            if dataDiscussion.nb_request >= 10:
                dataDiscussion.nb_request = 10
            else:
                dataDiscussion.nb_request += 1
            if dataDiscussion.nb_request == 5:
                dataDiscussion.grandpy_code = 'tired'
            else:
                dataDiscussion.grandpy_code = 'response'
    else:
        dataDiscussion.grandpy_response =\
            discussion.answer('incomprehension')
        dataDiscussion.grandpy_code = 'incomprehension'
        dataDiscussion.nb_incomprehension += 1

    if dataDiscussion.nb_indecency >= 3:
        dataDiscussion.grandpy_response = discussion.answer('indecency_limit')
        dataDiscussion.expiration_data()

    if dataDiscussion.nb_incomprehension >= 3:
        dataDiscussion.grandpy_response =\
            discussion.answer('incomprehension_limit')
        dataDiscussion.expiration_data()

    if dataDiscussion.nb_incivility >= 3:
        dataDiscussion.grandpy_response = discussion.answer('incivility_limit')
        dataDiscussion.expiration_data()
    if dataDiscussion.nb_request >= 10:
        dataDiscussion.grandpy_response = discussion.answer('wait1')
        dataDiscussion.expiration_data()

    if dataDiscussion.nb_request > 0 and dataDiscussion.nb_request != 5\
        and dataDiscussion.decency and dataDiscussion.nb_request < 10\
        and dataDiscussion.comprehension:
        dataDiscussion.grandpy_response = discussion.answer('response')
        dataDiscussion.grandpy_code = 'response'
        
    elif dataDiscussion.nb_request == 5:
        dataDiscussion.nb_request += 1

    display_response = research.get_map()
    dataDB.update_dataBase()

    if dataDiscussion.quotas:
        dataDB.expiry_request()

    return dataDiscussion, display_response


if __name__ == '__main__':

    # ~ var_debug = input("Tapez 'd' pour passer en debogage ... !")
    # ~ if var_debug == 'd':
        # ~ os.environ['DEBUG'] = 'True'
    # ~ os.system('clear')
    # ~ main('bonjour')
    pass

