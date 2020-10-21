#coding:utf-8
#!/usr/bin/env python

import inspect


# debug class
class Debugging:
    """
        class for debugging script, method, function
            - red    ==> parameter module
            - green  ==> main module
            - purple ==> question module
            - orange ==> chat module
    """
    # constructor
    def __init__(self):
        """
           debug class constructor
        """
        self.red = '\033[31m'  # debug color for the parameter module
        self.green = '\033[32m'  # debug color for the main module
        self.orange = '\033[33m'  # debug color for the chat module
        self.blue = '\033[34m'  # debug color for the answer module
        self.purple = '\033[35m'  # debug color for question module
        self.reset = '\033[0m'  # debug end color for modules
        self.dbg_color = ''  # debug color assignment

    # function name
    def name(self, func_name):
        """
            determines the debugging color of the name
        """
        if func_name == 'main' or func_name == 'check_presentation_user'\
            or func_name == 'reconnect_parameter':
            self.dbg_color = self.green
        elif func_name == 'add_message':
            self.dbg_color = self.red
        elif func_name == 'waiting_question' or func_name == 'question_incorrect'\
            or func_name == 'stress_incomprehension' or func_name == 'stress_indecency'\
            or func_name == 'stress_incivility':
            self.dbg_color = self.blue
        elif func_name == 'user_comprehension' or func_name == 'user_decency'\
            or func_name == 'user_civility' or func_name == 'response_user':
            self.dbg_color = self.purple
        elif func_name == 'user_request' or func_name == 'civility_check'\
            or func_name == 'decency_check' or func_name == 'comprehension_check'\
            or func_name == 'grandpy_reply' or func_name == 'reconnection_delay'\
            or func_name == 'waiting_request' or func_name == 'indecency_limit'\
            or func_name == 'incivility_limit' or func_name == 'incorrect_request'\
            or func_name == 'rude_request' or func_name == 'unpoliteness'\
            or func_name == 'incorrect_request':
            self.dbg_color = self.orange

        return f'\n{self.dbg_color}fonction {func_name}{self.reset}'


    # function call
    def call(self, func_name, class_name):
        """
            determines the debug color of the function call
        """
        if class_name == 'UserQuestion':
            self.dbg_color = self.purple
        elif class_name == 'QuestionParameter':
            self.dbg_color = self.red
        elif class_name == 'GpAnswer':
            self.dbg_color = self.blue
        elif class_name == 'Chat':
            self.dbg_color = self.orange

        return f'Appel de {self.dbg_color}{func_name}{self.reset}'\
            +f' dans {self.dbg_color}{class_name}{self.reset}'


    # function add
    def historical(self, result, func_name):
        """
            determines the debug color of the function call
        """
        if func_name == 'user_civility'\
            or func_name == 'user_decency'\
            or func_name == 'user_comprehension':
            self.dbg_color =  self.purple
        elif func_name == 'comprehension'\
            or func_name == 'civility' or func_name == 'decency'\
            or func_name == 'nb_incomprehension' or func_name == 'nb_request'\
            or func_name == 'nb_indecency' or func_name == 'nb_incivility'\
            or func_name == 'add_message':
            self.dbg_color = self.red
        elif func_name == 'stress_incivility' or func_name == 'stress_indecency'\
            or func_name == 'stress_incomprehension':
            self.dbg_color = self.blue

        return f'Ajout de {self.dbg_color}{result}{self.reset}'\
            +f' dans {self.dbg_color}{func_name}{self.reset}'
    # line numbre in function
    def nb_line(self, line):
        """
            determine the next line number in the function
        """
        if line != 0:
            dbg_color = self.green
        return f'{self.dbg_color}ligne {line}{self.reset}'


    # after function
    def return_line(self):
        """
            new line after function
        """
        return 'Retour'



