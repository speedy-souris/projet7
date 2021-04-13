#coding:utf-8
#!/usr/bin/env python
"""
    main management menu
"""
from .chatdata import Chat
from . import grandpyrobot  
# ~ from . import answersearch


class CheckUserBehavior(Chat):
    """
        check the state of the user's behavior in their questions
    """
    def __init__(self, user_question):
        super().__init__(user_question)
        self.user_behavior_processing = self.return_user_behavior_data
        self.user_behavior_value = self.get_processing_of_user_behavior_data

    def user_civility(self):
        if self.user_behavior_processing.return_user_civility_value():
            self.user_behavior_value.user_civility = True
        else:
            self.user_behavior_value.user_civility = False
            self.user_behavior_value.number_incivility += 1
        return self.user_behavior_value.user_civility

    def user_decency(self):
        if self.user_behavior_processing.return_user_decency_value():
            self.user_behavior_value.user_decency = True
        else:
            self.user_behavior_value.user_decency = False
            self.user_behavior_value.number_indecency += 1
        return self.user_behavior_value.user_decency

    def user_comprehension(self):
        if self.user_behavior_processing.return_user_comprehension_value():
            self.user_behavior_value.user_comprehension = True
        else:
            self.user_behavior_value.user_comprehension = False
            self.user_behavior_value.number_incomprehension += 1
        return self.user_behavior_value.user_comprehension

    def user_request_limit(self):
        if self.user_behavior_value.number_request >= 10:
            self.user_behavior_value.request_quotas = True
        return self.user_behavior_value.request_quotas

    def user_incivility_limit(self):
        if self.user_behavior_value.number_incivility >= 3:
            self.user_behavior_value.request_quotas = True
        return self.user_behavior_value.request_quotas

    def user_indecency_limit(self):
        if self.user_behavior_value.number_indecency >= 3:
            self.user_behavior_value.request_quotas = True
        return self.user_behavior_value.request_quotas

    def user_incomprehension_limit(self):
        if self.user_behavior_value.number_incomprehension >= 3:
            self.user_behavior_value.request_quotas = True
        return self.user_behavior_value.request_quotas

    def user_request_parse(self):
        return self.user_behavior_processing.parser()

def grandpy_response(answer_key):
    grandpy_response_processing = grandpyrobot
    response_grandpy =\
        grandpy_response_processing.get_response_grandpy(answer_key)
    return response_grandpy 

# script execution
def main(user_question):
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    # awaits the courtesy of the user
    # ~ _data_db  = BehaviorData()
    # ~ _access_database = AccessBehaviorDataBase()
    # ~ _user = user.Question(question, _data_db)
    # ~ discussion = Chat(_user, grandpyrobot)
    # ~ research = answersearch.get_from_map_status(discussion, question)

    # ~ discussion.get_question('comprehension')
    # ~ if _data_db.comprehension:
        # ~ discussion.get_question('decency')
        # ~ if _data_db.decency and not _data_db.civility:
            # ~ discussion.get_question('civility')
            # ~ if _data_db.civility:
                # ~ _data_db.get_reset_behavior()
                # ~ _data_db.grandpy_response = discussion.get_answer('wait1')
                # ~ _data_db.grandpy_code = ''
            # ~ else:
                # ~ _data_db.get_display_data(44)
                # ~ _data_db.grandpy_response = discussion.get_answer('mannerless')
                # ~ _data_db.grandpy_code = 'mannerless'
                # ~ if _data_db.nb_incivility >= 3:
                    # ~ _data_db.nb_incility = 3
                # ~ else:
                    # ~ _data_db.nb_incivility += 1
        # ~ elif not _data_db.decency:
            # ~ _data_db.grandpy_response = discussion.get_answer('disrespectful')
            # ~ _data_db.grandpy_code = 'disrespectful'
            # ~ if _data_db.nb_indecency >= 3:
                # ~ _data_db.nb_indecency = 3
            # ~ else:
                # ~ _data_db.nb_indecency += 1
        # ~ else:
            # ~ _data_db.grandpy_response = discussion.get_answer('response')
            # ~ if _data_db.nb_request >= 10:
                # ~ _data_db.nb_request = 10
            # ~ else:
                # ~ _data_db.nb_request += 1
            # ~ if _data_db.nb_request == 5:
                # ~ _data_db.grandpy_code = 'tired'
            # ~ else:
                # ~ _data_db.grandpy_code = 'response'
    # ~ else:
        # ~ _data_db.grandpy_response =\
            # ~ discussion.get_answer('incomprehension')
        # ~ _data_db.grandpy_code = 'incomprehension'
        # ~ _data_db.nb_incomprehension += 1

    # ~ if _data_db.nb_indecency >= 3:
        # ~ _data_db.grandpy_response = discussion.get_answer('indecency_limit')
        # ~ _data_db.get_expiration_data()

    # ~ if _data_db.nb_incomprehension >= 3:
        # ~ _data_db.grandpy_response =\
            # ~ discussion.get_answer('incomprehension_limit')
        # ~ _data_db.get_expiration_data()

    # ~ if _data_db.nb_incivility >= 3:
        # ~ _data_db.grandpy_response = discussion.get_answer('incivility_limit')
        # ~ _data_db.get_expiration_data()
    # ~ if _data_db.nb_request >= 10:
        # ~ _data_db.grandpy_response = discussion.get_answer('wait1')
        # ~ _data_db.get_expiration_data()

    # ~ if _data_db.nb_request > 0 and _data_db.nb_request != 5\
        # ~ and _data_db.decency and _data_db.nb_request < 10\
        # ~ and _data_db.comprehension:
        # ~ _data_db.grandpy_response = discussion.get_answer('response')
        # ~ _data_db.grandpy_code = 'response'

    # ~ elif _data_db.nb_request == 5:
        # ~ _data_db.nb_request += 1

    # ~ display_response = research
    # ~ _access_database.get_update_database()

    # ~ if _data_db.quotas:
        # ~ _data_db.expiry_request()

    # ~ return _data_db, display_response


if __name__ == '__main__':
    pass
