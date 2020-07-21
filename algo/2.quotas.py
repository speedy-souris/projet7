#coding:utf-8
#!/usr/bin/env python

import redis

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

                           #=================
                           # Script function
                           #=================
#==========================
# attribute initialization
#==========================
def initialization(accueil):
    pass


                           #==============
                           # Script class
                           #==============
# Redis server organization
class Talking:
    """
        Constants for processing keywords for Google Map APIs and grandpy's behavior
        according to the content of the user question
            - DONNEE_CIVILITY----set()

        Management for initializing configuration database Redis
            - redis_connect() ==> connection initialization for the Redis database
            - writing()       ==> writing of data value for the Redis database
            - incrementing()  ==> incrementing the data value for the Redis database
            - expiry()        ==> data value expiration times for the Redis database
            - reading         ==> read data value for the Redis database
    """
#--------------------------------------------------------------
# Data for civility (DONNEE_CIVILITY = set()) ==> line 64 to 68
#--------------------------------------------------------------

    def __init__(self, user_home):
        """
            constructor
            for initializing the API default variables in Redis
                - user_home        ==> content of the question asked to grandpy
                                       by the user containing the keywords
                                       for the Google Map API
                - redis_connect()  ==> initialization of the connection method
                                       to the Redis database
                - initial_status() ==> initialization of data values
                                       from the Redis database
        """
        self.user_home = user_home
        self.quotas = False
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

                - write_quotas()      ==> default initialization of quotas values
                                            for the Redis database
                - write_counter()       ==> default initialization of counter values
                                            for the Redis database

        """
        self.write_quotas(False)
        self.write_counter("0")

#---------------------------------------------------
# Civility in the Redis database ==> line 151 to 162
#---------------------------------------------------

    #==============================================
    # value of data quotas in the Redis database
    #==============================================
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

    #=================
    # Counter Request
    #=================
    @property
    def increment_counter(self):
        """
            Counter increment in Redis database
        """
        self.nb_request = self.incrementing("nb_request")

    @property
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

#==================
# script execution
#==================
def main():
    """
        request limitation to 10
        from the user after politeness check
    """
    #-----------------------------
    # Else (civility) ==> line 244
    #-----------------------------
    question = input("Que veux tu savoir ... ?")
    request = Talking(question)
    quotas = request.quotas
    value_quotas = request.nb_request
    nb_request = request.nb_request

    while not quotas:
        nb_request += 1
        value_quotas = nb_request
        if value_quotas >= 10:
            quotas = True
        if value_quotas == 5:
            print("Houla ma mémoire n'est plus ce qu'elle était ... ")

        print("Voici Ta Réponse !")
        question = input("Que veux tu savoir ... ?")

    print("cette séance de recherche me FATIGUE ...")
    print("reviens me voir demain !")

if __name__ == "__main__":
    main()



