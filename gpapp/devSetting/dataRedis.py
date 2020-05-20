#coding:utf-8
#!/usr/bin/env python

import redis
from .dataInitial import InitData

# Redis server organization
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
                    #==============
                    # Server Redis
                    #==============
    INITDATA = InitData()

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
        self.question = question

        # ~ self.writing("quotas_api", CONVERSION.bool_convers(False))
        # ~ self.writing("civility", CONVERSION.bool_convers(False))
        # ~ self.writing("decency", CONVERSION.bool_convers(True))
        # ~ self.writing("comprehension", CONVERSION.bool_convers(True))
        # ~ self.writing("nb_request", 0)
        self.initial_status()

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

    #==================================
    # Initialization status parameters
    #==================================
    def initial_status(self):
        """
            creation and initialization of parameters for REDIS
        """
        self.write_quotas(False)
        self.write_civility(False)
        self.write_decency(True)
        self.write_comprehension(True)
        self.write_counter("0")

    #============
    # Quotas_api
    #============
    def write_quotas(self, quotas):
        """
            saving of quotas configuration
        """
        self.quotas = quotas
        self.writing("quotas_api", bool_convers(self.quotas))

    @property
    def read_quotas(self):
        """
            reading of quotas configuration
        """
        return str_convers(self.reading("quotas_api"))

    #==========
    # Civility
    #==========
    def write_civility(self, civility):
        """
            saving of civility configuration
        """
        # ~ self.civility = civility
        self.writing("civility", bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration
        """
        return str_convers(self.reading("civility"))

    #=========
    # Decency
    #=========
    def write_decency(self, decency):
        """
            saving of decency configuration
        """
        self.writing("decency", bool_convers(decency))

    @property
    def read_decency(self):
        """
            reading of decency configuration
        """
        return str_convers(self.reading("decency"))

    #===============
    # comprehension
    #===============
    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration
        """
        self.comprehension = comprehension
        self.writing(
            "comprehension",
            bool_convers(self.comprehension)
        )

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration
        """
        return str_convers(Conversation.reading("comprehension"))

    #=================
    # Counter Request
    #=================
    @property
    def increment_counter(self):
        """
            Counter increment
        """
        self.nb_request = self.incrementing("nb_request")

    @property
    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter)
        """
        self.expiry("nb_request", 86400)

    @property
    def read_counter(self):
        """
            reading of counter configuration
        """
        return self.reading("nb_request")

    def write_counter(self, value):
        """
            modification of the value
            of the request counter in Redis
        """
        self.writing("nb_request", value)
        # ~ try:
            # ~ self.writing("nb_request", value)
        # ~ except TypeError:
            # ~ self.writing("nb_request", 0)
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

    #==========
    # civility
    #==========
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
        self.write_civility(result1)

    #=========
    # decency
    #=========
    def decency(self):
        """
            modification of attributes decency
        """
        # list of words to find in questions
        list_question = self.question.split()
        # search decency
        result2 = bool(
            [
            w for w in list_question if w.lower() not in InitData.INDECENCY_LIST
            ]
        )

        self.write_decency(result2)

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

        self.write_comprehension(result3)

                    #==================================
                    # converting data values for Redis
                    #==================================
# boolean ==> string
def bool_convers(value):
    """
        conversion from boolean to string
    """
    if value :
        return "1"
    else:
        return "0"

 # string ==> boolean
def str_convers(value):
    """
        conversion from string to boolean
    """
    value = value.decode("utf8")
    if value == "0":
        return False
    elif value == "":
        return False
    else:
        return True


if __name__ == "__main__":
    pass

