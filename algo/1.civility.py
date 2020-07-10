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
class DataParameter:
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
    DONNEE_CIVILITY = set(
        [
        "bonjour", "bonsoir","salut","hello","hi"
        ]
    )

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
        self.civility = False
        self.value_incivility = 0
        self.nb_request = self.value_incivility
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

                - write_civility()      ==> default initialization of civility values
                                            for the Redis database
                - write_counter()       ==> default initialization of counter values
                                            for the Redis database

        """
        self.write_civility(False)
        self.write_counter("0")

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

    #=================
    # user's civility
    #=================
    @property
    def user_civility(self):
        """
            modification of attributes civility
        """
        # list of words to find in questions
        list_user_home = self.user_home.split()
        # search civility
        result = bool(
            [
            w for w in list_user_home if w.lower() in self.DONNEE_CIVILITY
            ]
        )
        self.civility = result
        self.write_civility(self.civility)

#==================
# script execution
#==================
def main():
    """
        welcome of the user with politeness check
    """
    print("Bonjour Mon petit")
    accueil = input("En quoi puis je t'aider : ")
    request = DataParameter(accueil)
    request.user_civility
    value_civility = request.civility
    nb_incivility = request.value_incivility


    if not value_civility:
        while not value_civility and nb_incivility < 3:
            print("Tu es impoli ...")
            nb_incivility += 1
            request.nb_request = nb_incivility
            accueil = input("Si tu es impoli, je ne peux rien pour toi ... : ")
            request.user_home = accueil
            request.user_civility
            value_civility = request.civility


    if nb_incivility >= 3:
        print("cette impolitesse me FATIGUE ...")
        print("reviens me voir demain !")
        request.expiry_counter
    else:
        print("Que veux tu savoir ... ?")


if __name__ == "__main__":
    main()
