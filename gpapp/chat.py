#coding:utf-8
#!/usr/bin/env python

import redis
from parameter import QuestionParameter as Params


                           #========================
                           # class setting function
                           #========================

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


                           #==============
                           # Script class
                           #==============
# Redis server organization
class Chat(Params):
    """
        Params ==> mother class (QuestionParameter)
        API Private Key and Constants Management :
            local (development) / external (production)
                status_env()
                    - key_data["map"]         ==> KEY_API_MAP / HEROKU_KEY_API_MAP
                    - key_data["staticMap"]   ==> KEY_API_STATIC_MAP / HEROKU_KEY_API_STATIC_MAP
                    - key_data["status_prod"] ==> True / False

        Management for initializing configuration database Redis
            - redis_connect() ==> connection initialization for the Redis database
            - writing()       ==> writing of data value for the Redis database
            - incrementing()  ==> incrementing the data value for the Redis database
            - expiry()        ==> data value expiration times for the Redis database
            - reading         ==> read data value for the Redis database
    """
    #===========================
    # Constructor of Chat class
    #===========================
    def __init__(self):
        """
            constructor for initializing the API default variables in Redis
                - quotas           ==> initialisation of quotas attribut
                - nb_indecency     ==> number of user indecency
                - nb_request       ==> number of user requests
                - redis_connect()  ==> initialization of the connection method
                                       to the Redis database
                - initial_status() ==> initialization of data values
                                       from the Redis database
        """
        super().__init__()
        self.quotas = False
        self.nb_incivility = 0
        self.nb_indecency = 0
        self.nb_incomprehension = 0
        self.nb_request = 0
        self.redis_connect()
        self.initial_status()


    #==============
    # Server Redis
    #==============
    def redis_connect(self):
        """
            connection to the Redis database
        """
        self.connect = redis.Redis(
            host="localhost",
            port=6379,
            db=0
        )


    # writing
    def writing(self, data, value):
        """
            writing data to Redis database
        """
        self.connect.set(data, value)


    # increment
    def incrementing(self, data):
        """
            incrementing the request counter in Redis database
        """
        self.connect.incr(data)


    # expiration time
    def expiry(self, data, value):
        """
            expiration
            of the counter variable in Redis database
            (after 24 hours)
        """
        self.connect.expire(data, value)


    # reading
    def reading(self, data):
        """
            reading data in Redis database
        """
        return self.connect.get(data)


    #==================================
    # Initialization status parameters
    #==================================
    def initial_status(self):
        """
            creation and initialization by default of data values
            for the Redis database

                - write_ civility()   ==> default initialization of civility values
                                          for the Redis database
                - write_quotas()      ==> default initialization of quotas values
                                          for the Redis database
                - write_decency()   ==> default initialization of decency values
                                          for the Redis database
                - write_counter()     ==> default initialization of counter values
                                          for the Redis database

        """
        self.write_civility(False)
        self.write_quotas(False)
        self.write_decency(False)
        self.write_comprehension(False)
        self.write_counter(0)


    #==========================
    # status parameter display
    #==========================
    def display_status(self):
        """
            display of data values in the question

                - nb_incivility      ==> number of civility
                - nb_indecency       ==> number of decency
                - nb_incomprehension ==> number of comprehension
        """
        print(f"\nquestion = {self.tmp}\n")
        print(f"Valeur de quotas = {self.quotas}")
        print(f"Valeur de civility = {self.civility}")
        print(f"valeur de decency = {self.decency}")
        print(f"valeur de comprehension = {self.comprehension}")
        print(f"Nombre d'incivility = {self.nb_incivility}")
        print(f"Nombre d'indecency = {self.nb_indecency}")
        print(f"Nombre d'incomprehension = {self.nb_incomprehension}")


    #==============================================
    # value of data Civility in the Redis database
    #==============================================
    def write_civility(self, civility):
        """
            saving of civility configuration in Redis database
        """
        self.writing("civility", bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration in Redis database
        """
        return str_convers(self.reading("civility"))


    #============================================
    # value of data quotas in the Redis database
    #============================================
    def write_quotas(self, quotas):
        """
            saving of quotas configuration in Redis database
        """
        self.writing("quotas", bool_convers(quotas))

    @property
    def read_quotas(self):
        """
            reading of quotas configuration in Redis database
        """
        return str_convers(self.reading("quotas"))


    #===============================================
    # value of data decency in the Redis database
    #===============================================
    def write_decency(self, decency):
        """
            saving of decency configuration in Redis database
        """
        self.writing("decency", bool_convers(decency))

    @property
    def read_decency(self):
        """
            reading of decency configuration in Redis database
        """
        return str_convers(self.reading("decency"))


    #===============
    # comprehension
    #===============
    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration in Redis database
        """
        self.comprehension = comprehension
        self.writing(
            "comprehension",
            bool_convers(self.comprehension)
        )

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration in Redis database
        """
        return str_convers(self.reading("comprehension"))


    #=================
    # Counter Request
    #=================
    def increment_counter(self):
        """
            Counter increment in Redis database
        """
        self.nb_request = self.incrementing("nb_request")

    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter) in Redis database
        """
        self.expiry("nb_request", 86400)

    @property
    def read_counter(self):
        """
            reading of counter configuration in Redis database
        """
        return self.reading("nb_request")

    def write_counter(self, value):
        """
            modification of the value
            of the request counter in Redis database
        """
        self.writing("nb_request", value)
