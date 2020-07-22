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
#========================================
# reconnection after 24 hours of waiting
#========================================
def reconnection(talk):
    """
        stop questions and answers for 24 hours
    """
    print("reviens me voir demain !")
    # ~ talk.expiry_counter()

#=================
# attent question
#=================
def waiting_question(talk):
    """
        waiting for user question
    """
    question = "Que veux tu savoir ... ?"
    talk.add_message(question, talk.grandpy)
    response = input(question)
    talk.add_message(response, talk.user)
    talk.user_indecency()

#=============
# rude answer
#=============
def rude_user(talk):
    """
        rude user
    """
    question = "Si tu es grossier, je ne peux rien pour toi ... : \n"
    talk.add_message(question, talk.grandpy)
    rudeness = input(question)
    talk.add_message(rudeness, talk.user)
    talk.user_indecency()


#=====================
# stress of indecency
#=====================
def stress_indecency(talk):
    """
        stress of Grandpy
    """
    print("cette grossierete me FATIGUE ...")
    reconnection(talk)

#=======================
# indecency in response
#=======================
def answer_indecency(talk):
    """
        control of indecency in response
    """
    if talk.indecency:
            while talk.indecency and talk.nb_indecency < 3:
                talk.nb_indecency += 1
                talk.nb_request += 1
                rude_user(talk)



                           #==============
                           # Script class
                           #==============
# Redis server organization
class Chat:
    """
        Constants for processing keywords for Google Map APIs and grandpy's behavior
        according to the content of the user question
            - DONNEE_CIVILITY----set()
            - INDECENCY_LIST-----set()

        Management for initializing configuration database Redis
            - redis_connect() ==> connection initialization for the Redis database
            - writing()       ==> writing of data value for the Redis database
            - incrementing()  ==> incrementing the data value for the Redis database
            - expiry()        ==> data value expiration times for the Redis database
            - reading         ==> read data value for the Redis database
    """
    #------------------------
    # Data for test civility
    #------------------------
    DONNEE_CIVILITY = set(
        [
        "bonjour", "bonsoir","salut","hello","hi"
        ]
    )
    #-----------------------
    # Data for test decency
    #-----------------------
    INDECENCY_LIST = set(
        [
        "vieux","con","poussierieux","ancetre","demoder","vieillard","senille",
        "dinosaure","decrepit","arrierer ","rococo","centenaire","senille",
        "vieillot","archaique","gateux","croulant","antiquite","baderne","fossile",
        "bjr","bsr","slt"
        ]
    )


    def __init__(self):
        """
            constructor
            for initializing the API default variables in Redis
                - messages--|       ==> content of the question asked to grandpy
                            |--list    by the user containing the keywords
                            |          for the Google Map API / Grandpy's response
                - chatters--|      ==> speaker for the question / answer (Grandpy / user)
                - civility         ==> initialization of civility attribut
                - quotas           ==> initialisation of quotas attribut
                - indecency        ==> user`s coarseness (value boolean)
                - nb_indecency     ==> number of user indecency
                - nb_request       ==> number of user requests
                - redis_connect()  ==> initialization of the connection method
                                       to the Redis database
                - initial_status() ==> initialization of data values
                                       from the Redis database
        """
        self.messages = []
        self.chatters = []
        self.tmp = ""
        self.grandpy = "Grandpy"
        self.user = "User"
        self.civility = False
        self.quotas = False
        self.indecency = False
        self.nb_indecency = 0
        self.nb_request = 0
        self.redis_connect()
        self.initial_status()

    #=============
    # add message
    #=============
    def add_message(self, message, chatter):
        """
            Add new message with chatter
        """
        self.messages.append(message)
        self.chatters.append(chatter)
        if chatter == "User":
            self.nb_request += 1
            self.tmp = message

    #====================
    # Read list messages
    #====================
    def chat_viewer(self):
        """
            Read full list of messages
        """
        for chatter, message in zip(self.chatters, self.messages):
            print(f"{[chatter]} = {message}")

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
                - write_indecency()   ==> default initialization of indecency values
                                          for the Redis database
                - write_counter()     ==> default initialization of counter values
                                          for the Redis database

        """
        self.write_civility(False)
        self.write_quotas(False)
        self.write_indecency(False)
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
    # value of data Indecency in the Redis database
    #===============================================
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

    #=================
    # user's civility
    #=================
    def user_civility(self):
        """
            modification of attributes civility
        """
        # list of words to find in questions
        user_answer = self.tmp.split()
        # search civility
        result = bool(
            [
            w for w in user_answer if w.lower() in self.DONNEE_CIVILITY
            ]
        )
        self.civility = result
        # ~ self.write_civility(self.civility)

    #=================
    # user's decency
    #=================
    def user_indecency(self):
        """
            modification of attributes indecency
        """
        # list of words to find in questions
        user_answer = self.tmp.split()
        # search indecency
        result = bool(
            [
            w for w in user_answer if w.lower() in self.INDECENCY_LIST
            ]
        )
        self.indecency = result
        # ~ self.write_indecency(self.indecency)

#==================
# script execution
#==================
def main():
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    #---------------------------------
    # awaits the courtesy of the user
    #---------------------------------
    talk = Chat()
    question = "Bonjour Mon petit, en quoi puis je t'aider ?\n"
    talk.add_message(question, talk.grandpy)
    accueil = input(question)
    talk.add_message(accueil, talk.user)
    talk.user_civility()


    # rudeness of the user
    if not talk.civility:
        while not talk.civility and talk.nb_request < 3:
            question = "Si tu es impoli, je ne peux rien pour toi ... : \n"
            talk.add_message(question, talk.grandpy)
            accueil = input(question)
            talk.add_message(accueil, talk.user)
            talk.user_civility()


        # big stress of Grandpy because of incivility ==> back in 24 hours
        if talk.nb_request >= 3:
            print("cette impolitesse me FATIGUE ...")
            reconnection(talk)
    # Waits for user question
    else:
        waiting_question(talk)

        if talk.indecency:
            talk.nb_indecency += 1
            talk.indecency = False

        answer_indecency(talk)

        # big stress of Grandpy because of indecency ==> back in 24 hours
        if talk.nb_indecency >= 3:
            stress_indecency(talk)

        # Waits for user new question
        else:
            while not value_quotas:
                # maximum number of responses reached
                if nb_request >= 10:
                    value_quotas = True

                # Grandpy starts to tire
                if nb_request == 5:
                    print("Houla ma mémoire n'est plus ce qu'elle était ... ")

                # grandpy's reply
                print("Voici Ta Réponse !")
                nb_request = request.nb_request
                nb_request += 1
                question = waiting_question(request)
                value_quotas = question[0]
                value_indecency = question[1]
                request.nb_request = nb_request
                request.indecency = value_indecency
                # User coarseness
                response_user = answer_indecency(
                    (request.indecency, nb_indecency, request.nb_request, request)
                )



                # big stress of Grandpy because of indecency ==> back in 24 hours
                if nb_indecency >= 3:
                    stress_indecency(question)


            # grandpy exhaustion
            print("cette séance de recherche me FATIGUE ...")
            reconnection(question)

if __name__ == "__main__":
    main()



