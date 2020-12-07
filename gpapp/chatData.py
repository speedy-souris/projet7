#coding:utf-8
#!/usr/bin/env python

import os
import redis


# Initialization data chat
class Data:
    """
    default variables data
            - quotas           ==> initialisation of quotas attribut
            - nb_indecency     ==> number of user indecency
            - nb_request       ==> number of user requests
            - redis_data_redis()  ==> initialization of the data_redision method
                                   to the Redis database
            - initial_status() ==> initialization of data values
                                   from the Redis database
            - civility
            - decency
            - comprehension
    API Private Key and Constants Management :
        local (development) / external (production)
            keys()
                - key_value['map']         ==> KEY_API_MAP / HEROKU_KEY_API_MAP
                - key_value['staticMap']   ==> KEY_API_STATIC_MAP / HEROKU_KEY_API_STATIC_MAP
                - key_value['status_prod'] ==> True / False
    Management for initializing configuration database Redis
        - redis_data_redis() ==> data_redision initialization for the Redis database
        - writing()       ==> writing of data value for the Redis database
        - incrementing()  ==> incrementing the data value for the Redis database
        - expiry()        ==> data value expiration times for the Redis database
        - reading         ==> read data value for the Redis database
    """
    def __init__(self):
        """
            data chat initialization constructor
        """
        self.key_value = {}
        self.dataDiscussion = self.data_access
        try:
            self.read_civility
        except AttributeError:
            self.initial_data()
        self.grandpy_response = self.read_response
        self.civility = self.read_civility
        self.decency = self.read_decency
        self.comprehension = self.read_comprehension
        self.quotas = self.read_quotas
        self.nb_request = self.read_counter
        self.nb_incivility = self.read_incivility
        self.nb_indecency = self.read_indecency
        self.nb_incomprehension = self.read_incomprehension

#~~~~~~~~~~~~~~~~~~~~~ CALCULATION AND PROPERTY ~~~~~~~~~~~~~~~~~~~~~~~~

    # convert boolean to string
    @staticmethod
    def bool_convers(value):
        """
            conversion from boolean to string
        """
        if value :
            return '1'
        else:
            return '0'

    # convert string to boolean
    @staticmethod
    def str_convers(value):
        """
            conversion from string to boolean
        """
        value = value.decode("utf8")
        if value == '0':
            return False
        elif value == '':
            return False
        else:
            return True

    # convert string to integer
    @staticmethod
    def str_int(value):
        """
            conversion from string to internal
        """
        return int(value)

    # keys for Google APIs in environment variables
    @property
    def keys(self):
        """
            management of environment variables
            local and online
                - key_value["map"]         ==> =|
                - key_value["staticMap"]   ==> =|- private keys for Google APIs
                                                  (local or online)
                - key_value["status_prod"] ==> boolean for redis database
                                              data_redision method
        """
        # keys for local use (Dev)
        if os.environ.get("HEROKU_KEY_API_MAP") is None:
            self.key_value["map"] = os.getenv("KEY_API_MAP")
            self.key_value["staticMap"] = os.getenv("KEY_API_STATIC_MAP")
            self.key_value["status_prod"] = False
        # keys for online use (Prod)
        else:
            self.key_value["map"] = os.getenv("HEROKU_KEY_API_MAP")
            self.key_value["staticMap"] = os.getenv("HEROKU_KEY_API_STATIC_MAP")
            self.key_value["status_prod"] = True
        return self.key_value

#~~~~~~~~~~~~~~~~~~~~~~ ACCESS CHAT DATABASE ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @property
    def data_access(self):
        """
            method for data_redision to the Redis database
                - keys["status_prod"] = False ==> Redis database in local
                - keys["status_prod"] = True ==> Redis database in online
        """
        if not self.keys["status_prod"]:
            return redis.Redis(
                host='localhost',
                port=6379,
                db=0
            )
        else:
            return redis.Redis(
                host="grandpy-papy-robot.herokuapp.com/",
                port=6379,
                db=1
           )
#~~~~~~~~~~~~~~~~~~~~~~~ ACCESS CHAT DATA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def writing(self, data, value):
        """
            writing chat data to Redis database
        """
        self.dataDiscussion.set(data, value)

    def incrementing(self, data):
        """
            incrementing the request counter in Redis database
        """
        self.dataDiscussion.incr(data)

    # data deletion for 24 hours
    def expiry(self, data, value):
        """
            expiration
            of the counter variable in Redis database
            (after 24 hours)
        """
        self.dataDiscussion.expire(data, value)

    def reading(self, data):
        """
            reading data in Redis database
        """
        return self.dataDiscussion.get(data)

    def write_civility(self, civility):
        """
            saving of civility configuration in Redis database
        """
        self.writing('civility', self.bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration in Redis database
        """
        return self.str_convers(self.reading('civility'))

    # request limit
    def write_quotas(self, quotas):
        """
            saving of quotas configuration in Redis database
        """
        self.writing('quotas', self.bool_convers(quotas))

    @property
    def read_quotas(self):
        """
            reading of quotas configuration in Redis database
        """
        return self.str_convers(self.reading('quotas'))

    def write_decency(self, decency):
        """
            saving of decency configuration in Redis database
        """
        self.writing('decency', self.bool_convers(decency))

    @property
    def read_decency(self):
        """
            reading of decency configuration in Redis database
        """
        return self.str_convers(self.reading('decency'))

    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration in Redis database
        """
        self.writing('comprehension', self.bool_convers(comprehension))

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration in Redis database
        """
        return self.str_convers(self.reading('comprehension'))

    # incrementation of the number of requests
    def increment_counter(self):
        """
            Counter increment in Redis database
        """
        self.writing(
            'nb_request', write_counter(self.incrementing('nb_request'))
        ) 

    # delay of expiration of the number of requests
    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter) in Redis database
        """
        self.expiry('nb_request', 86400)

    # number of...
    def write_counter(self, value):
        """
            modification of the value
            of the request counter in Redis database
        """
        self.writing('nb_request', value)

    # number of...
    @property
    def read_counter(self):
        """
            reading of counter configuration in Redis database
        """
        return self.str_int(self.reading('nb_request'))

    # number of...
    def write_incivility(self, value):
        """
            counter incivility in Redis Database
        """
        self.writing('nb_incivility', value)

    # number of...
    @property
    def read_incivility(self):
        """
            reading of incivility count in Redis database
        """
        return self.str_int(self.reading('nb_incivility'))

    # number of...
    def write_indecency(self, value):
        """
            counter indecency in Redis Database
        """
        self.writing('nb_indecency', value)

    # number of...
    @property
    def read_indecency(self):
        """
            reading of indecency count in Redis database
        """
        return self.str_int(self.reading('nb_indecency'))

    # number of...
    def write_incomprehension(self, value):
        """
            counter incomprehension in Redis Database
        """
        self.writing('nb_incomprehension', value)

    # number of...
    @property
    def read_incomprehension(self):
        """
            reading of incomprehension count in Redis database
        """
        return self.str_int(self.reading('nb_incomprehension'))

    # grandpy's response 
    def write_response(self, value):
        """
            grandpy's response in Redis Database
        """
        self.writing('gp_response', value)

    @property
    def read_response(self):
        """
            reading of grandpy's response in Redis database
        """
        return self.reading('gp_response')

#~~~~~~~~~~~~~~~~~ GENERAL PROCESSING OF CHAT DATA ~~~~~~~~~~~~~~~~~~~~~

    def initial_data(self):
        """ creation and initialization by default of data values
            for the Redis database
    
                - write_ civility()      ==> default initialization 
                                             of civility value
                - write_quotas()         ==> default initialization 
                                             of quotas value
                - write_decency()        ==> default initialization
                                             of decency value
                - write_comprehension()  ==> default initialization
                                             of comprehension value
                - write_counter()        ==> default initialization
                                             of counter value
                - write_response()       ==> default initialization
                                             of grandpy's response
        """
        self.write_civility(False)
        self.write_quotas(False)
        self.write_decency(False)
        self.write_comprehension(False)
        self.write_counter(0)
        self.write_incivility(0)
        self.write_indecency(0)
        self.write_incomprehension(0)
        self.write_response('')

    def update_data(self):
        """
            update for database redis
                - Args Value ==> [
                    quotas, civility, decency, comprehension, nb_request, 
                    nb_incivility, nb_indecency, nb_incomprehension,
                    response
                ]
        """
        self.write_quotas(self.quotas)
        self.write_civility(self.civility)
        self.write_decency(self.decency)
        self.write_comprehension(self.comprehension)
        self.write_counter(self.nb_request)
        self.write_incivility(self.nb_incivility)
        self.write_indecency(self.nb_indecency)
        self.write_incomprehension(self.nb_incomprehension)
        self.write_response(self.grandpy_response)

    def display_data(self, question):
        """
            display of data values in the question
                - Args Value ==> [
                    tmp (user question), quotas, civility, decency, comprehension,
                    nb_request, nb_incivility, nb_indecency, nb_incomprehension,
                    grandpy_response (grandpy's response)
                ]
        """
        print(f'question = {question}\n')
        print(f'Valeur de quotas = {self.quotas}')
        print(f'Valeur de civility = {self.civility}')
        print(f'valeur de decency = {self.decency}')
        print(f'valeur de comprehension = {self.comprehension}')
        print(f'Nombre de request = {self.nb_request}')
        print(f'Nombre d\'incivility = {self.nb_incivility}')
        print(f'Nombre d\'indecency = {self.nb_indecency}')
        print(f'Nombre d\'incomprehension = {self.nb_incomprehension}')
        print(f'Réponse de grandpy = {self.grandpy_response}')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def reset_behavior(self):
        """
            initialisation behavior parameters:
                - comprehension --|
                - civility -------| ==> False
                - decency --------|
        """
        self.civility = False 
        self.decency = False
        self.comprehension = False

if __name__ == '__main__':
    pass
