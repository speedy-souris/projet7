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
    # ~ _data_db.get_reset_behavior()
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
    _data_db  = BehaviorData()
    _access_database = AccessBehaviorDataBase()
    _user = user.Question(question, _data_db)
    discussion = Chat(_user, grandpyrobot)
    research = answersearch.get_from_map_status(discussion, question)

    discussion.get_question('comprehension')
    if _data_db.comprehension:
        discussion.get_question('decency')
        if _data_db.decency and not _data_db.civility:
            discussion.get_question('civility')
            if _data_db.civility:
                _data_db.get_reset_behavior()
                _data_db.grandpy_response = discussion.get_answer('wait1')
                _data_db.grandpy_code = ''
            else:
                _data_db.get_display_data(44)
                _data_db.grandpy_response = discussion.get_answer('mannerless')
                _data_db.grandpy_code = 'mannerless'
                if _data_db.nb_incivility >= 3:
                    _data_db.nb_incility = 3
                else:
                    _data_db.nb_incivility += 1
        elif not _data_db.decency:
            _data_db.grandpy_response = discussion.get_answer('disrespectful')
            _data_db.grandpy_code = 'disrespectful'
            if _data_db.nb_indecency >= 3:
                _data_db.nb_indecency = 3
            else:
                _data_db.nb_indecency += 1
        else:
            _data_db.grandpy_response = discussion.get_answer('response')
            if _data_db.nb_request >= 10:
                _data_db.nb_request = 10
            else:
                _data_db.nb_request += 1
            if _data_db.nb_request == 5:
                _data_db.grandpy_code = 'tired'
            else:
                _data_db.grandpy_code = 'response'
    else:
        _data_db.grandpy_response =\
            discussion.get_answer('incomprehension')
        _data_db.grandpy_code = 'incomprehension'
        _data_db.nb_incomprehension += 1

    if _data_db.nb_indecency >= 3:
        _data_db.grandpy_response = discussion.get_answer('indecency_limit')
        _data_db.get_expiration_data()

    if _data_db.nb_incomprehension >= 3:
        _data_db.grandpy_response =\
            discussion.get_answer('incomprehension_limit')
        _data_db.get_expiration_data()

    if _data_db.nb_incivility >= 3:
        _data_db.grandpy_response = discussion.get_answer('incivility_limit')
        _data_db.get_expiration_data()
    if _data_db.nb_request >= 10:
        _data_db.grandpy_response = discussion.get_answer('wait1')
        _data_db.get_expiration_data()

    if _data_db.nb_request > 0 and _data_db.nb_request != 5\
        and _data_db.decency and _data_db.nb_request < 10\
        and _data_db.comprehension:
        _data_db.grandpy_response = discussion.get_answer('response')
        _data_db.grandpy_code = 'response'

    elif _data_db.nb_request == 5:
        _data_db.nb_request += 1

    display_response = research
    _access_database.get_update_database()

    if _data_db.quotas:
        _data_db.expiry_request()

    return _data_db, display_response


if __name__ == '__main__':
    pass
