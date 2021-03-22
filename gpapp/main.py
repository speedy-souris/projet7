#coding:utf-8
#!/usr/bin/env python

import chatdata
import grandpyrobot
import user
import answersearch


# ~ def checkout_comprehension(discussion):
    # ~ """
        # ~ check the understanding of the question
    # ~ """
    # ~ data_discussion.get_reset_behavior()
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
    _chatdata = chatdata
    data_discussion = _chatdata.BehaviorData()
    grandpy = grandpyrobot
    _user = user.Question(question, data_discussion)
    discussion = _chatdata.Chat(_user, grandpy)
    data_db = _chatdata.BehaviorDatabase()
    research = answersearch.get_from_map_status(discussion, question)

    discussion.get_question('comprehension')
    if data_discussion.comprehension:
        discussion.get_question('decency')
        if data_discussion.decency and not data_discussion.civility:
            discussion.get_question('civility')
            if data_discussion.civility:
                data_discussion.get_reset_behavior()
                data_discussion.grandpy_response = discussion.get_answer('wait1')
                data_discussion.grandpy_code = ''
            else:
                data_discussion.get_display_data(44)
                data_discussion.grandpy_response = discussion.get_answer('mannerless')
                data_discussion.grandpy_code = 'mannerless'
                if data_discussion.nb_incivility >= 3:
                    data_discussion.nb_incility = 3
                else:
                    data_discussion.nb_incivility += 1
        elif not data_discussion.decency:
            data_discussion.grandpy_response = discussion.get_answer('disrespectful')
            data_discussion.grandpy_code = 'disrespectful'
            if data_discussion.nb_indecency >= 3:
                data_discussion.nb_indecency = 3
            else:
                data_discussion.nb_indecency += 1
        else:
            data_discussion.grandpy_response = discussion.get_answer('response')
            if data_discussion.nb_request >= 10:
                data_discussion.nb_request = 10
            else:
                data_discussion.nb_request += 1
            if data_discussion.nb_request == 5:
                data_discussion.grandpy_code = 'tired'
            else:
                data_discussion.grandpy_code = 'response'
    else:
        data_discussion.grandpy_response =\
            discussion.get_answer('incomprehension')
        data_discussion.grandpy_code = 'incomprehension'
        data_discussion.nb_incomprehension += 1

    if data_discussion.nb_indecency >= 3:
        data_discussion.grandpy_response = discussion.get_answer('indecency_limit')
        data_discussion.expiration_data()

    if data_discussion.nb_incomprehension >= 3:
        data_discussion.grandpy_response =\
            discussion.get_answer('incomprehension_limit')
        data_discussion.expiration_data()

    if data_discussion.nb_incivility >= 3:
        data_discussion.grandpy_response = discussion.get_answer('incivility_limit')
        data_discussion.expiration_data()
    if data_discussion.nb_request >= 10:
        data_discussion.grandpy_response = discussion.get_answer('wait1')
        data_discussion.expiration_data()

    if data_discussion.nb_request > 0 and data_discussion.nb_request != 5\
        and data_discussion.decency and data_discussion.nb_request < 10\
        and data_discussion.comprehension:
        data_discussion.grandpy_response = discussion.get_answer('response')
        data_discussion.grandpy_code = 'response'

    elif data_discussion.nb_request == 5:
        data_discussion.nb_request += 1

    display_response = research.get_from_map_status()
    data_db.get_update_dataBase()

    if data_discussion.quotas:
        data_db.expiry_request()

    return data_discussion, display_response


if __name__ == '__main__':
    pass
