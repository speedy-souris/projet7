#coding:utf-8
#!/usr/bin/env python

import inspect


# response organization
class Answer:
    """
        organization of the grandpy's answer
    """
    def __init__(self, dataDiscussion, response):
        """
            constructor
               organization of the grandpy's answer
        """
        self.dataDiscussion = dataDiscussion
        self.response = response
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # response grandpy
    def answer_returned(self):
        """
            response returned by grandpy for the courteous user
        """
        txt_returned = f'Voici Ta Réponse à la question {self.question} !'
        self.dataDiscussion.write_response =\
            response.get_place_id_list(response)
        return response

    # return from grandpy after 24h00
    def reconnection(self):
        """
            stop questions and answers for 24 hours
        """
        txt_response = 'reviens me voir demain !'
        # ~ response = f'Réponse de {self.history.grandpy} ==> {txt_response}'
        # ~ self.dataDiscussion.grandpy_response = txt_response
        # ~ print(f'\n{response}')
        # ~ self.history.add_message(txt_response, self.history.grandpy)
        # ~ print('\n----------------------------------------------------------------')
        # ~ print('-------- HISTORIQUE DE CONVERSATION ----------------------------')
        # ~ print('----------------------------------------------------------------')
        # ~ self.history.chat_viewer()
        # ~ print('----------------------------------------------------------------\n')
        # ~ self.dataDiscussion.display_status()
        # ~ self.history.init_message()
        # ~ self.dataDiscussion.quotas = True
        # ~ self.dataDiscussion.expiry_counter()

    # attent question
    def waiting_question(self):
        """
            waiting for user question
        """
        txt_response = 'Hey bien, tu peux me poser ta question maintenant ... ! '
        return txt_response

    # attent new question
    def waiting_new_question(self):
        """
            waiting for user new question
        """
        txt_response = 'As tu une nouvelle question a me demander ? '
        return txt_response

    # stress of indecency
    def stress_indecency(self):
        """
            stress of Grandpy
        """
        txt_response = 'cette grossierete me FATIGUE ... !'
        return txt_response

    # stress of civility
    def stress_incivility(self):
        """
            stress of Grandpy
        """
        txt_response = 'cette impolitesse me FATIGUE ... !'
        return txt_response

    # stress of incomprehension
    def stress_incomprehension(self):
        """
            stress of Grandpy
        """
        txt_response = f'cette incomprehension me FATIGUE ... !'
        return txt_response

    # rude answer
    def rude_user(self):
        """
            rude user
        """
        txt_response = 'Si tu es grossier, je ne peux rien pour toi ... : '
        return txt_response

    # user unpoliteness
    def unpoliteness_user(self):
        """
            user unpoliteness in the question for grandpy
        """
        txt_response = 'Si tu es impoli, je ne peux rien pour toi ... : '
        return txt_response

    # incorrect question
    def question_incorrect(self):
        """
                unknown words in the question
        """
        txt_response = "Je ne comprends pas, essaye d'être plus précis ... !"
        return txt_response


