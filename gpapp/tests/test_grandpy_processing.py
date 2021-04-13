#coding:utf-8
#!/usr/bin/env python

from ..main import grandpy_response


def test_should_return_grandpy_message():
    key_message1 = grandpy_response('incomprehension')
    key_message2 = grandpy_response('mannerless')
    key_message3 = grandpy_response('disrespectful')
    key_message4 = grandpy_response('response')
    key_message5 = grandpy_response('quotas')
    key_message6 = grandpy_response('invalid')
    key_message7 = grandpy_response('incivility_limit')
    key_message8 = grandpy_response('indecency_limit')
    key_message9 = grandpy_response('incomprehension_limit')
    key_message10 = grandpy_response('wait2')
    key_message11 = grandpy_response('wait1')
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