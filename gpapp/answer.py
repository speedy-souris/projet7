#coding:utf-8
#!/usr/bin/env python

import inspect
from chat import Chat


                           #==============
                           # Script class
                           #==============
# Grandpy response
class GpAnswer(Chat):
    """
        organization of the grandpy's answer
            Chat ==> mother class
    """
    def __init__(self):
        """
            constructor
               organization of the grandpy's answer
        """
        super().__init__()


    #==================
    # response grandpy
    #==================
    def answer_returned(self):
        """
            response returned by grandpy for the courteous user
        """
        response = "Voici Ta Réponse !"
        print(f"{response} : {self.tmp}")
        self.add_message(response, self.grandpy)
        self.nb_request += 1


    #========================================
    # reconnection after 24 hours of waiting
    #========================================
    def reconnection(self):
        """
            stop questions and answers for 24 hours
        """
        response = f"Réponse de {self.grandpy} ==> reviens me voir demain !"
        print(f"\n{response}")
        self.add_message(response, self.grandpy)
        print("\n--------------------------------------------")
        print("-------- HISTORIQUE DE CONVERSATION --------")
        print("--------------------------------------------")
        self.chat_viewer()
        print("--------------------------------------------\n")
        self.init_message()
        # ~ self.expiry_counter()


    #=================
    # attent question
    #=================
    def waiting_question(self):
        """
            waiting for user question
        """
        response = "Que veux tu savoir ... ?"
        print(self.name("waiting_question"))
        print(f"Reponse de {self.grandpy} ==> {answer}")
        self.add_message(answer, self.grandpy)


    #=====================
    # stress of indecency
    #=====================
    def stress_indecency(self):
        """
            stress of Grandpy
        """
        response = "cette grossierete me FATIGUE ... !"
        print(response)
        self.add_message(response, self.grandpy)
        print(f"{inspect.currentframe().f_lineno + 2}", end=".")
        print(f" Appel de {self.reconnection.__name__}")
        self.reconnection()


    #====================
    # stress of civility
    #====================
    def stress_incivility(self):
        """
            stress of Grandpy
        """
        response = "cette impolitesse me FATIGUE ... !"
        print(response)
        self.add_message(response, self.grandpy)
        print()
        print(f"{inspect.currentframe().f_lineno + 2}", end=".")
        print(f" Appel de {self.reconnection.__name__}")
        self.reconnection()


    #===========================
    # stress of incomprehension
    #===========================
    def stress_incomprehension(self):
        """
            stress of Grandpy
        """
        response = f"Réponse de {self.grandpy} ==> "\
            f"cette incomprehension me FATIGUE ... !"
        print(f"\n{response}")
        print(self.name("stress_incomprehension"))
        print(self.nb_line(inspect.currentframe().f_lineno+2), end=" ==> ")
        print(self.call("add_message", "QuestionParameter"))
        self.add_message(response, self.grandpy)
        print(self.name("stress_incomprehension"))
        print(self.nb_line(inspect.currentframe().f_lineno+2), end=" ==> ")
        print(self.call(self.reconnection.__name__, type(self).__name__))
        self.reconnection()



    #=============
    # rude answer
    #=============
    def rude_user(self):
        """
            rude user
        """
        question = "Si tu es grossier, je ne peux rien pour toi ... : \n"
        self.add_message(question, self.grandpy)


    #===================
    # user unpoliteness
    #===================
    def unpoliteness_user(self):
        """
            user unpoliteness in the question for grandpy
        """
        question = "Si tu es impoli, je ne peux rien pour toi ... : \n"
        self.add_message(question, self.grandpy)


    #====================
    # incorrect question
    #====================
    def question_incorrect(self):
        """
                unknown words in the question
        """
        response = f"Réponse de {self.grandpy} ==> "\
            +"Je ne comprends pas, essaye d'être plus précis ... !"
        print(f"\n{response}")
        print(self.name("question_incorrect"))
        print(self.nb_line(inspect.currentframe().f_lineno+2), end=" ==> ")
        print(self.call("add_message", "QuestionParameter"))
        self.add_message(response, self.grandpy)
