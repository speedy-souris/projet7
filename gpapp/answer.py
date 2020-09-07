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
        response = "reviens me voir demain !"
        print(response)
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
        question = "Que veux tu savoir ... ?\n"
        self.add_message(question, self.grandpy)
        print()
        print(f"{inspect.currentframe().f_lineno + 2}",end=".")
        print(f" Appel de {self.response_user.__name__}")
        self.response_user(question)


    #=====================
    # stress of indecency
    #=====================
    def stress_indecency(self):
        """
            stress of Grandpy
        """
        response = "cette grossierete me FATIGUE ..."
        print(response)
        self.add_message(response, self.grandpy)
        print()
        print(f"{inspect.currentframe().f_lineno + 2}", end=".")
        print(f" Appel de {self.reconnection.__name__}")
        self.reconnection()


    #=====================
    # stress of civility
    #=====================
    def stress_incility(self):
        """
            stress of Grandpy
        """
        response = "cette imopolitesse me FATIGUE ..."
        print(response)
        self.add_message(response, self.grandpy)
        print()
        print(f"{inspect.currentframe().f_lineno + 2}", end=".")
        print(f" Appel de {self.reconnection.__name__}")
        self.reconnection()


    #=============
    # rude answer
    #=============
    def rude_user(self, func):
        def rude(self):
            """
                rude user
            """
            question = "Si tu es grossier, je ne peux rien pour toi ... : \n"
            self.add_message(question, self.grandpy)
            print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
            print(f" Appel de {func.response_user.__name__}\n")
            func.response_user(question)
        return rude


    #===================
    # user unpoliteness
    #===================
    def unpoliteness_user(self, func):
        def unpoliteness(self):
            """
                user unpoliteness in the question for grandpy
            """
            question = "Si tu es impoli, je ne peux rien pour toi ... : \n"
            self.add_message(question, self.grandpy)
            print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
            print(f" Appel de {func.response_user.__name__}\n")
            func.response_user(question)
        return unpoliteness


