#coding:utf-8
#!/usr/bin/env python

import os
import inspect


                           #==============
                           # Script class
                           #==============
# user question parameter
class History:
    """
        the content of the user question for the analyzer script
            - messages--|            content of the question asked to grandpy
                        |-- list ==> by the user containing the keywords
                        |            for the Google Map API / Grandpy's response
            - chatters--|----------- speaker for the question / answer (Grandpy / user)
            - user_question      ==> temporary variable for for the question parser
            - grandpy            ==> grandpa robot
            - user               ==> user asking questions
            - data_redis         ==> object for the connection to the redis database
    """
    # constructor
    def __init__(self, debug=None):
        """
            contructor of parameter
                - messages, user_question, grandpy, user
                - civility, decency, comprehension, quotas
                - nb_incivility, nb_indecency, nb_incomprehension, nb_request
        """
        self.debug = debug
        self.messages = []
        self.chatters = []
        self.user_question = user_question
        self.grandpy = 'Grandpy' # robot for chat message
        self.user = 'User'  # user for chat message

    # create an archive
    def add_message(self, message, chatter):
        """
            Add new message with chatter
        """
        if os.environ.get('DEBUG') == 'True':
            print(self.debug.name('add_message'))
            print(
                f'{self.debug.nb_line(inspect.currentframe().f_lineno)} CREATION ARCHIVE'
            )
            print(self.debug.nb_line(inspect.currentframe().f_lineno+1), end=' ==> ')
            print(self.debug.historical(f'{message}','add_message'))
            print(self.debug.nb_line(inspect.currentframe().f_lineno+1), end=' ==> ')
            print(self.debug.historical(f'{chatter}','add_message'))

        self.messages.append(message)
        self.chatters.append(chatter)
        if chatter == 'User':
            self.user_question = message


    # initialization of the archive
    def init_message(self):
        """
            reseting the message list
        """
        self.messages[:] = []
        self.chatters[:] = []


    # Read the archive
    def chat_viewer(self):
        """
            Read full list of messages
        """
        print()
        for (counter, (chatter, message)) in enumerate(
            zip(self.chatters, self.messages)):
            print(f'{counter + 1}.{[chatter]} = {message}')
        print()

if __name__ == "__main__":
    pass
