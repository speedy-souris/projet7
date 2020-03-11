#coding:utf-8
#!/usr/bin/env python

import redis
from .dataInitial import InitData
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
        self.quotas = 0
        self.civility = 0
        self.decency = 1
        self.comprehension = 1
        self.nb_request = 0
        self.question = question

        Conversation.writing("quotas_api", self.quotas)
        Conversation.writing("civility", self.civility)
        Conversation.writing("decency", self.decency)
        Conversation.writing("comprehension", self.comprehension)
        Conversation.writing("nb_request", self.nb_request)

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
            w for w in list_question if w.lower() not in Conversation.INITDATA.constants[
                "list_unnecessary"
            ]
        ]

        return result



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
        Script.writing("quotas_api", self.quotas)

    @property
    def read_quotas(self):
        """
            reading of quotas configuration
        """
        return Script.reading("quotas_api")

#==========
# Civility
#==========
    def write_civility(self, civility):
        """
            saving of civility configuration
        """
        self.civility = civility
        Script.writing("civility", self.civility)

    @property
    def read_civility(self):
        """
            reading of civility configuration
        """
        return Script.reading("civility")

#=========
# Decency
#=========
    def write_decency(self, decency):
        """
            saving of decency configuration
        """
        self.decency = decency
        Script.writing("decency", self.decency)

    @property
    def read_decency(self):
        """
            reading of decency configuration
        """
        return Script.reading("decency")

#===============
# comprehension
#===============
    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration
        """
        self.comprehension = comprehension
        Script.writing("comprehension", self.comprehension)

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration
        """
        return Script.reading("comprehension")

#=================
# Counter Request
#=================
    @property
    def increment_counter(self):
        """
            Counter increment
        """
        self.nb_request = Script.incrementing("nb_request")

    @property
    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter)
        """
        Script.expiry("nb_request", 86400)

    @property
    def read_counter(self):
        """
            reading of counter configuration
        """
        return Script.reading("nb_request")

    def write_counter(self, data, value):
        """
            modification of the value
            of the request counter in Redis
        """
        try:
            Script.writing(data, value)
        except TypeError:
            Script.writing("nb_request", 0)


if __name__ == "__main__":
    pass
