#coding:utf-8
#!/usr/bin/env python

from .. import main
from ..chatdata import Chat


class TestUserJourney:
    def setup_method(self):
        self.script = main
        # ~ self.user_behavior_data = self.script.main('connais tu OpenClassrooms')
        # ~ self.data_discussion = Chat(user_question='')
        # ~ self.user_behavior = self.data_discussion.behavior_data
        # ~ self.user_behavior.get_initial_database()
    # ~ def tearDown(self):
        # ~ self.user_behavior.get_update_database()


    def test_should_return_grandpy_message_for_user_civility(self):
        user_civility_data = self.script.main('bonjour')
                
        assert user_civility_data.grandpy_response ==\
            "Bonjour Mon petit, en quoi puis-je t'aider ?" and\
            user_civility_data.grandpy_code == ''

        user_incivility_data = self.script.main('openClassrooms')
        assert user_incivility_data.grandpy_response ==\
            "s'il te plait, reformule ta question en étant plus polis ... !" and\
            user_incivility_data.grandpy_code == 'mannerless'

        user_incivility_data = self.script.main('openClassrooms')
        data_discussion = Chat(user_question='')
        data_discussion.number_incivility = 3
        print(f'incivility test = {data_discussion.number_incivility}')
        assert user_incivility_data.grandpy_response ==\
            'cette impolitesse me FATIGUE ... !' and\
            user_behavior_data.grandpy_code == 'exhausted'

