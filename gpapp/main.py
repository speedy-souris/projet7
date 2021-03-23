#coding:utf-8
#!/usr/bin/env python
"""
    main management menu
"""
from .chatdata import BehaviorData, Chat, AccessBehaviorDataBase
from . import grandpyrobot
from . import user
from . import answersearch


# ~ def checkout_comprehension(discussion):
    # ~ """
        # ~ check the understanding of the question
    # ~ """
    # ~ data_db.get_reset_behavior()
    # ~ comprehension = discussion.get_question('comprehension')
    # ~ return comprenhension

# ~ def checkout_dencency(discussion):
    # ~ """
        # ~ check the decency of the question
    # ~ """
    # ~ decency = discussion.get_question('decency')
    # ~ return decency

# ~ def checkout_civility(discussion):
    # ~ """
        # ~ check the civility of the question
    # ~ """
    # ~ decency = discussion.get_question('decency')
    # ~ return decency

# script execution
def main(question):
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    # awaits the courtesy of the user
    _behavior_data = BehaviorData()
    _access_database = AccessBehaviorDataBase()
    grandpy = grandpyrobot
    _user = user.Question(question, _behavior_data)
    _chat = Chat(_user, grandpy)
    discussion =_chat
    data_db = _behavior_data
    _map_status = answersearch.get_from_map_status(discussion, question)
    research = _map_status

    discussion.get_question('comprehension')
    if data_db.comprehension:
        discussion.get_question('decency')
        if data_db.decency and not data_db.civility:
            discussion.get_question('civility')
            if data_db.civility:
                data_db.get_reset_behavior()
                data_db.grandpy_response = discussion.get_answer('wait1')
                data_db.grandpy_code = ''
            else:
                data_db.get_display_data(44)
                data_db.grandpy_response = discussion.get_answer('mannerless')
                data_db.grandpy_code = 'mannerless'
                if data_db.nb_incivility >= 3:
                    data_db.nb_incility = 3
                else:
                    data_db.nb_incivility += 1
        elif not data_db.decency:
            data_db.grandpy_response = discussion.get_answer('disrespectful')
            data_db.grandpy_code = 'disrespectful'
            if data_db.nb_indecency >= 3:
                data_db.nb_indecency = 3
            else:
                data_db.nb_indecency += 1
        else:
            data_db.grandpy_response = discussion.get_answer('response')
            if data_db.nb_request >= 10:
                data_db.nb_request = 10
            else:
                data_db.nb_request += 1
            if data_db.nb_request == 5:
                data_db.grandpy_code = 'tired'
            else:
                data_db.grandpy_code = 'response'
    else:
        data_db.grandpy_response =\
            discussion.get_answer('incomprehension')
        data_db.grandpy_code = 'incomprehension'
        data_db.nb_incomprehension += 1

    if data_db.nb_indecency >= 3:
        data_db.grandpy_response = discussion.get_answer('indecency_limit')
        data_db.get_expiration_data()

    if data_db.nb_incomprehension >= 3:
        data_db.grandpy_response =\
            discussion.get_answer('incomprehension_limit')
        data_db.get_expiration_data()

    if data_db.nb_incivility >= 3:
        data_db.grandpy_response = discussion.get_answer('incivility_limit')
        data_db.get_expiration_data()
    if data_db.nb_request >= 10:
        data_db.grandpy_response = discussion.get_answer('wait1')
        data_db.get_expiration_data()

    if data_db.nb_request > 0 and data_db.nb_request != 5\
        and data_db.decency and data_db.nb_request < 10\
        and data_db.comprehension:
        data_db.grandpy_response = discussion.get_answer('response')
        data_db.grandpy_code = 'response'

    elif data_db.nb_request == 5:
        data_db.nb_request += 1

    display_response = research
    _access_database.get_update_database()

    if data_db.quotas:
        data_db.expiry_request()

    return data_db, display_response


if __name__ == '__main__':
    pass
