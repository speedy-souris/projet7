#coding:utf-8
#!/usr/bin/env python

import redis
from .dataInitial import InitData
from . import fDev as func
# ~ from ..tests import test_questionAnswer
#==============
# Server Redis
#==============
class Conversation:
    """
        Initialization of Redis connection parameters
            - CONNECT
        Management class for initializing configuration data
            - quotas
            - civility
            - decency
            - comprehension
            - nb_request
    """
    INITDATA = InitData()
    # ~ PARAMS = test_questionAnswer.TestAPi().PARAMS

    if not INITDATA.status_env["status_prod"]:
        CONNECT = redis.Redis(
            host="localhost",
            port=6379,
            db=0
        )
    else:
        CONNECT = redis.Redis(
            host="grandpy-papy-robot.herokuapp.com/",
            port=6379,
            db=1
        )

    def __init__(self, question):
        """
            constructor
            for initializing the API variables in Redis
        """
        # ~ self.quotas = False
        # ~ self.civility = False
        # ~ self.decency = True
        # ~ self.comprehension = True
        # ~ self.nb_request = 0
        self.question = question

        Conversation.writing("quotas_api", func.bool_convers(False))
        Conversation.writing("civility", func.bool_convers(False))
        Conversation.writing("decency", func.bool_convers(True))
        Conversation.writing("comprehension", func.bool_convers(True))
        Conversation.writing("nb_request", 0)

    @classmethod
    def writing(cls, data, value):
        """
            writing data to Redis
        """
        cls.CONNECT.set(data, value)

    @classmethod
    def incrementing(cls, data):
        """
            incrementing the request counter in Redis
        """
        cls.CONNECT.incr(data)

    @classmethod
    def expiry(cls, data, value):
        """
            expiration
            of the counter variable in Redis
            (after 24 hours)
        """
        cls.CONNECT.expire(data, value)

    @classmethod
    def reading(cls, data):
        """
            reading data in Redis
        """
        return cls.CONNECT.get(data)

                        #=================
                        # Initialization
                        # Data of setting
                        #=================
    #============
    # Quotas_api
    #============
    def write_quotas(self, quotas):
        """
            saving of quotas configuration
        """
        self.quotas = quotas
        Conversation.writing("quotas_api", func.bool_convers(self.quotas))

    @property
    def read_quotas(self):
        """
            reading of quotas configuration
        """
        return func.int_convers(Conversation.reading("quotas_api"))

    #==========
    # Civility
    #==========
    def write_civility(self, civility):
        """
            saving of civility configuration
        """
        # ~ self.civility = civility
        Conversation.writing("civility", func.bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration
        """
        return func.int_convers(Conversation.reading("civility"))

    #=========
    # Decency
    #=========
    def write_decency(self, decency):
        """
            saving of decency configuration
        """
        self.decency = decency
        Conversation.writing("decency", func.bool_convers(self.decency))

    @property
    def read_decency(self):
        """
            reading of decency configuration
        """
        return func.int_convers(Conversation.reading("decency"))

    #===============
    # comprehension
    #===============
    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration
        """
        self.comprehension = comprehension
        Conversation.writing("comprehension", func.bool_convers(self.comprehension))

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration
        """
        return func.int_convers(Conversation.reading("comprehension"))

    #=================
    # Counter Request
    #=================
    @property
    def increment_counter(self):
        """
            Counter increment
        """
        self.nb_request = Conversation.incrementing("nb_request")

    @property
    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter)
        """
        Conversation.expiry("nb_request", 86400)

    @property
    def read_counter(self):
        """
            reading of counter configuration
        """
        return Conversation.reading("nb_request")

    def write_counter(self, data, value):
        """
            modification of the value
            of the request counter in Redis
        """
        try:
            Conversation.writing(data, value)
        except TypeError:
            Conversation.writing("nb_request", 0)
    #========
    # parser
    #========
    def parser(self):
        """
            function that cuts the string of characters (question asked to GrandPy)
            into a word list then delete all unnecessary words to keep only
            the keywords for the search
        """

        # list of words to remove in questions
        list_question = self.question.split()
        result = [
            w for w in list_question if w.lower() not in InitData.UNNECESSARY_LIST
        ]

        return result

    #============
    # attendance
    # word_list
    #============
    # ~ def attendance(self):
        # ~ """
            # ~ presence of list item
        # ~ """
        # ~ # list of words to find in questions
        # ~ list_question = self.question.split()
        # ~ # search civility
        # ~ result1 = bool(
            # ~ [
            # ~ w for w in list_question if w.lower() in InitData.CIVILITY_LIST
            # ~ ]
        # ~ )
        # ~ # search decency
        # ~ result2 = bool(
            # ~ [
            # ~ w for w in list_question if w.lower() in InitData.INDECENCY_LIST
            # ~ ]
        # ~ )
        # ~ # search comprehension
        # ~ result3 = bool(
            # ~ [
            # ~ w for w in list_question if w.lower()\
                # ~ in InitData.CIVILITY_LIST and w.lower() in InitData.INDECENCY_LIST
            # ~ ]
        # ~ )

        # ~ return (result1, result2, result3)

    def civility(self):
        """
            modification of attributes civility
        """
        # list of words to find in questions
        list_question = self.question.split()
        # search civility
        result1 = bool(
            [
            w for w in list_question if w.lower() in InitData.CIVILITY_LIST
            ]
        )
        print(self.question)
        print(result1)
        self.write_civility(
            func.bool_convers(result1)
        )

    def decency(self):
        """
            modification of attributes decency
        """
        # list of words to find in questions
        list_question = self.question.split()
        # search decency
        result2 = bool(
            [
            w for w in list_question if w.lower() in InitData.INDECENCY_LIST
            ]
        )

        self.write_decency(
            func.bool_convers(result2)
        )

    def comprehension(self):
        """
            modification of attributes decency
        """
        # list of words to find in questions
        list_question = self.question.split()
        # search comprehension
        result3 = bool(
            [
            w for w in list_question if w.lower()\
                in InitData.CIVILITY_LIST and w.lower() in InitData.INDECENCY_LIST
            ]
        )

        self.write_comprehension(
            func.bool_convers(result3)
        )

if __name__ == "__main__":
    pass
