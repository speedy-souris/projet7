#coding:utf-8
#!/usr/bin/env python

import os
import inspect

# chat organization
class Chat:
    """
        object management class
    """
    # Constructor 
    def __init__(self, user, grandpy):
        """
            constructor
                - user object
                - grandpy objet
        """
        self.user = user
        self.grandpy = grandpy
        
#-------------------- user behavior ------------------------------------

    def question(self, check):
        return self.user.message(check)

#------------------- grandpy robot behavior ----------------------------

    def answer(self, stage):
        return self.grandpy.message(stage)
