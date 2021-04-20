#coding:utf-8
#!/usr/bin/env python

from ..chatdata import Chat


def test_should_return_grandpy_message():
    grandpy_message_data = Chat(user_question='')
    key_message1 =\
        grandpy_message_data.get_grandpy_answer_processing('incomprehension')
    key_message2 =\
        grandpy_message_data.get_grandpy_answer_processing('mannerless')
    key_message3 =\
        grandpy_message_data.get_grandpy_answer_processing('disrespectful')
    key_message4 =\
        grandpy_message_data.get_grandpy_answer_processing('response')
    key_message5 =\
        grandpy_message_data.get_grandpy_answer_processing('quotas')
    key_message6 =\
        grandpy_message_data.get_grandpy_answer_processing('invalid')
    key_message7 =\
        grandpy_message_data.get_grandpy_answer_processing('incivility_limit')
    key_message8 = \
        grandpy_message_data.get_grandpy_answer_processing('indecency_limit')
    key_message9 = \
        grandpy_message_data.\
        get_grandpy_answer_processing('incomprehension_limit')
    key_message10 = \
        grandpy_message_data.get_grandpy_answer_processing('wait2')
    key_message11 =\
        grandpy_message_data.get_grandpy_answer_processing('wait1')
    result_message1 =\
        "Ha, Je ne comprends pas, essaye d'être plus précis ... !"
    result_message2 =\
        "s'il te plait, reformule ta question en étant plus polis ... !"
    result_message3 =\
        "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !"
    result_message4 = 'Voici Ta Réponse à la question !'
    result_message5 = 'reviens me voir demain !'
    result_message6 = 'Répond à la question par <oui> ou par <non> ... !'
    result_message7 = 'cette impolitesse me FATIGUE ... !'
    result_message8 = 'cette grossierete me FATIGUE ... !'
    result_message9 = 'cette incomprehension me FATIGUE ... !'
    result_message10 = 'As tu une nouvelle question a me demander ? '
    result_message11 = "Bonjour Mon petit, en quoi puis-je t'aider ?"

    assert key_message1 == result_message1
    assert key_message2 == result_message2
    assert key_message3 == result_message3
    assert key_message4 == result_message4
    assert key_message5 == result_message5
    assert key_message6 == result_message6
    assert key_message7 == result_message7
    assert key_message8 == result_message8
    assert key_message9 == result_message9
    assert key_message10 == result_message10
    assert key_message10 == result_message10
