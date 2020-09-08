#coding:utf-8
#!/usr/bin/env python

import inspect
from debug import Debugging as Dbg

                           #==============
                           # Script class
                           #==============
# user question parameter
class QuestionParameter(Dbg):
    """
        user question parameter for Chat
            - messages--|            content of the question asked to grandpy
                        |-- list ==> by the user containing the keywords
                        |            for the Google Map API / Grandpy's response
            - chatters--|----------- speaker for the question / answer (Grandpy / user)
            - tmp ---------      ==> temporary variable for for the question parser
            - grandpy -----      ==> grandpa robot
            - user --------      ==> user asking questions
            - civility
            - decency
            - comprehension

    """
    def __init__(self):
        """
            contructor of parameter
                - messages
                - tmp
                - grandpy
                - user
                - civility
                - decency
                - comprehension
        """
        super().__init__()
        self.messages = []
        self.chatters = []
        self.tmp = ""  # temporary variable for civility / decency wordlist
        self.grandpy = "Grandpy" # user for message
        self.user = "User"  # user for message
        self.civility = False
        self.decency = False
        self.comprehension = False


    #=============
    # add message
    #=============
    def add_message(self, message, chatter):
        """
            Add new message with chatter
        """
        print(self.name("add_message"))
        print(self.nb_line(inspect.currentframe().f_lineno+1), end=" ==> ")
        print(self.historical(f"[{message}]","add_message"))
        print(self.nb_line(inspect.currentframe().f_lineno+1), end=" ==> ")
        print(self.historical(f"[{chatter}]","add_message"))
        self.messages.append(message)
        self.chatters.append(chatter)
        if chatter == "User":
            self.tmp = message


    #========================
    # message initialization
    #========================
    def init_message(self):
        """
            resetting the message list
        """
        self.messages[:] = []
        self.chatters[:] = []


    #====================
    # Read list messages
    #====================
    def chat_viewer(self):
        """
            Read full list of messages
        """
        for (counter, (chatter, message)) in enumerate(
            zip(self.chatters, self.messages)):
            print(f"{counter + 1}.{[chatter]} = {message}")
