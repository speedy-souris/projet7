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
def reconnection(dialog):
    """
        stop questions and answers for 24 hours
    """
    print("reviens me voir demain !")
    # ~ dialog.expiry_counter()

#=================
# attent question
#=================
def waiting_question(dialog):
    """
        waiting for user question
    """
    question = "Que veux tu savoir ... ?\n"
    dialog.add_message(question, dialog.grandpy)
    response = input(question)
    dialog.add_message(response, dialog.user)
    dialog.user_indecency()
    if dialog.indecency:
        dialog.nb_indecency += 1
        dialog.indecency = False

    # big stress of Grandpy because of indecency ==> back in 24 hours
    if dialog.nb_indecency >= 3:
        stress_indecency(dialog)
    else:
        answer_indecency(dialog)

#=============
# rude answer
#=============
def rude_user(dialog):
    """
        rude user
    """
    question = "Si tu es grossier, je ne peux rien pour toi ... : \n"
    dialog.add_message(question, dialog.grandpy)
    rudeness = input(question)
    dialog.add_message(rudeness, dialog.user)
    dialog.user_indecency()


#=====================
# stress of indecency
#=====================
def stress_indecency(dialog):
    """
        stress of Grandpy
    """
    print("cette grossierete me FATIGUE ...")
    reconnection(dialog)

#=======================
# indecency in response
#=======================
def answer_indecency(dialog):
    """
        control of indecency in response
    """
    if dialog.indecency:
            while dialog.indecency and dialog.nb_indecency < 3:
                dialog.nb_indecency += 1
                dialog.nb_request += 1
                rude_user(dialog)
    # Waits for user question
    waiting_question(dialog)



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
        self.tmp = ""  # temporary variable for civility / indecency wordlist
        self.grandpy = "Grandpy" # user for message
        self.user = "User"  # user for message
        self.nb_messages = 0 # number of messages
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
            self.nb_messages += 1
            print(f"{self.nb_messages}.{[chatter]} = {message}")

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
    dialog = Chat()
    question = "Bonjour Mon petit, en quoi puis je t'aider ?\n"
    dialog.add_message(question, dialog.grandpy)
    accueil = input(question)
    dialog.add_message(accueil, dialog.user)
    dialog.user_civility()


    # rudeness of the user
    if not dialog.civility:
        while not dialog.civility and dialog.nb_request < 3:
            question = "Si tu es impoli, je ne peux rien pour toi ... : \n"
            dialog.add_message(question, dialog.grandpy)
            accueil = input(question)
            dialog.add_message(accueil, dialog.user)
            dialog.user_civility()


        # big stress of Grandpy because of incivility ==> back in 24 hours
        if dialog.nb_request >= 3:
            print("cette impolitesse me FATIGUE ...")
            reconnection(dialog)
        # Waits for user question
        else:
            waiting_question(dialog)

        # Waits for user new question
    else:
        while not dialog.quotas:
            # maximum number of responses reached
            if dialog.nb_request >= 10:
                dialog.quotas = True

            # Grandpy starts to tire
            if dialog.nb_request == 5:
                print("Houla ma mémoire n'est plus ce qu'elle était ... ")

            # grandpy's reply
            print("Voici Ta Réponse !")
            dialog.nb_request += 1
            waiting_question(dialog)

        # grandpy exhaustion
        print("cette séance de recherche me FATIGUE ...")
        reconnection(dialog)

if __name__ == "__main__":
    main()



