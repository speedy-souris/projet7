#coding:utf-8
#!/usr/bin/env python
"""
    grandpy's response display module
"""
def get_response_grandpy(key_response):
    """
        grandpy's message for each user behavior
    """
    gp_message = {
        'incomprehension':\
            "Ha, Je ne comprends pas, essaye d'être plus précis ... !",
        'mannerless':\
            "s'il te plait, reformule ta question en étant plus polis ... !",
        'disrespectful':\
            "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !",
        'response': 'Voici Ta Réponse à la question !',
        'quotas': 'reviens me voir demain !',
        'invalid': 'Répond à la question par <oui> ou par <non> ... !',
        'incivility_limit': 'cette impolitesse me FATIGUE ... !',
        'indecency_limit': 'cette grossierete me FATIGUE ... !',
        'incomprehension_limit': 'cette incomprehension me FATIGUE ... !',
        'wait2': 'As tu une nouvelle question a me demander ? ',
        'wait1': "Bonjour Mon petit, en quoi puis-je t'aider ?"
    }
    return gp_message[key_response]
