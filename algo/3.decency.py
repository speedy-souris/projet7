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
            - INDECENCY_LIST----set()

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
    INDECENCY_LIST = set(
        [
        "vieux","con","poussierieux","ancetre","demoder","vieillard","senille",
        "dinosaure","decrepit","arrierer ","rococo","centenaire","senille",
        "vieillot","archaique","gateux","croulant","antiquite","baderne","fossile",
        "bjr","bsr","slt"
        ]
    )

    def __init__(self, user_home):
        """
            constructor
            for initializing the API default variables in Redis
                - user_home        ==> content of the question asked to grandpy
                                       by the user containing the keywords
                                       for the Google Map API
                - indecency        ==> user`s coarseness (value boolean)
                - nb_request       ==> number of user requests
                - redis_connect()  ==> initialization of the connection method
                                       to the Redis database
                - initial_status() ==> initialization of data values
                                       from the Redis database
        """
        self.user_home = user_home
        self.indecency = False
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

                - write_indecency()      ==> default initialization of indecency values
                                            for the Redis database
                - write_counter()       ==> default initialization of counter values
                                            for the Redis database

        """
        self.write_indecency(False)
        self.write_counter("0")

#---------------------------------------------------
# Civility in the Redis database ==> line 151 to 162
#---------------------------------------------------
#---------------------------------------------------
# quotas in the Redis database ==> line 152 to 163
#---------------------------------------------------

    #=========
    # Decency
    #=========
    def write_indecency(self, indecency):
        """
            saving of indecency configuration in Redis database
        """
        self.writing("indecency", bool_convers(indecency))

    @property
    def read_indecency(self):
        """
            reading of indecency configuration in Redis database
        """
        return str_convers(self.reading("indecency"))

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
    # user's decency
    #=================
    @property
    def user_indecency(self):
        """
            modification of attributes indecency
        """
        # list of words to find in questions
        list_user_home = self.user_home.split()
        # search indecency
        result = bool(
            [
            w for w in list_user_home if w.lower() in self.INDECENCY_LIST
            ]
        )
        self.indecency = result

#==================
# script execution
#==================
def main():
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    #-----------------------------
    # Else (civility) ==> line 244
    #-----------------------------
    #--------------------------------------------
    # question = ... (quotas) ==> line 207 to 211
    #--------------------------------------------
    question = input("Que veux tu savoir ... ?")
    request = DataParameter(question)
    request.user_indecency
    value_indecency = request.indecency
    nb_indecency = request.nb_request
    nb_request = request.nb_request

    while value_indecency and nb_indecency < 3:
            print("Tu es grossier ...")
            nb_request += 1
            nb_indecencency = request.nb_request
            accueil = input("Si tu es grossier, je ne peux rien pour toi ... : ")
            request.user_home = accueil
            request.user_indecency
            value_indecency = request.indecency


    if nb_indecency >= 3:
        print("cette grossierete me FATIGUE ...")
        print("reviens me voir demain !")
        request.expiry_counter
    else:
        print("Que veux tu savoir ... ?")

if __name__ == "__main__":
    main()
