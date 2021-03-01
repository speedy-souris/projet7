#coding:utf-8
#!/usr/bin/env python

class Answer:
    """
        organization of the grandpy's answer
    """
    def answer_returned(self):
        """
            response returned by grandpy for the courteous user
        """
        txt_returned = 'Voici Ta Réponse à la question !'
        return txt_returned

    def reconnection(self):
        """
            stop questions and answers for 24 hours
        """
        txt_response = 'reviens me voir demain !'
        return txt_response

    def waiting_question(self):
        """
            waiting for user question
        """
        txt_response = "Bonjour Mon petit, en quoi puis-je t'aider ?"
        return txt_response

    def waiting_new_question(self):
        """
            waiting for user new question
        """
        txt_response = 'As tu une nouvelle question a me demander ? '
        return txt_response

    def stress_indecency(self):
        """
            stress of Grandpy
        """
        txt_response = 'cette grossierete me FATIGUE ... !'
        return txt_response

    def stress_incivility(self):
        """
            stress of Grandpy
        """
        txt_response = 'cette impolitesse me FATIGUE ... !'
        return txt_response

    def stress_incomprehension(self):
        """
            stress of Grandpy
        """
        txt_response = 'cette incomprehension me FATIGUE ... !'
        return txt_response

    def rude_user(self):
        """
            rude user
        """
        txt_response =\
            "Hola, sois plus RESPECTUEUX ENVERS TES AINES 'MON PETIT' ... !"
        return txt_response

    def unpoliteness_user(self):
        """
            user unpoliteness in the question for grandpy
        """
        txt_response =\
            "s'il te plait, reformule ta question en étant plus polis ... !"
        return txt_response

    def question_incorrect(self):
        """
                unknown words in the question
        """
        txt_response = "Ha, Je ne comprends pas, essaye d'être plus précis ... !"
        return txt_response

    def question_invalid(self):
        """
                invalid words in the question
        """
        txt_response = 'Répond à la question par <oui> ou par <non> ... !'
        return txt_response
        
#---------------------- Message of Grandpy -----------------------------        

    def message(self, stage):
        gp_message = {
            'incomprehension': self.question_incorrect,
            'mannerless': self.unpoliteness_user,
            'disrespectful': self.rude_user,
            'response': self.answer_returned,
            'quotas': self.reconnection,
            'invalid': self.question_invalid,
            'incivility_limit': self.stress_incivility,
            'indecency_limit': self.stress_indecency,
            'incomprehension_limit': self.stress_incomprehension,
            'wait2': self.waiting_new_question,
            'wait1': self.waiting_question
        }
        return gp_message[stage]()
    
    


