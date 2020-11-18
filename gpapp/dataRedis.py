#coding:utf-8
#!/usr/bin/env python

import os
import redis


#=============================
# Initialization Server Redis
#=============================
class RedisConnect:
    """
    default variables in Redis
            - quotas           ==> initialisation of quotas attribut
            - nb_indecency     ==> number of user indecency
            - nb_request       ==> number of user requests
            - redis_connect()  ==> initialization of the connection method
                                   to the Redis database
            - initial_status() ==> initialization of data values
                                   from the Redis database
            - civility
            - decency
            - comprehension

    API Private Key and Constants Management :
        local (development) / external (production)
            status_env()
                - key_data['map']         ==> KEY_API_MAP / HEROKU_KEY_API_MAP
                - key_data['staticMap']   ==> KEY_API_STATIC_MAP / HEROKU_KEY_API_STATIC_MAP
                - key_data['status_prod'] ==> True / False

    Management for initializing configuration database Redis
        - redis_connect() ==> connection initialization for the Redis database
        - writing()       ==> writing of data value for the Redis database
        - incrementing()  ==> incrementing the data value for the Redis database
        - expiry()        ==> data value expiration times for the Redis database
        - reading         ==> read data value for the Redis database
    """
    def __init__(self):
        """
            redis server initialization constructor
        """
        self.civility = self.read_civility()
        self.decency = self.read_decency()
        self.comprehension = self.read_comprehension()
        self.quotas = self.read_quotas()
        self.nb_request = self.read_nb_request()
        self.nb_incivility = self.read_nb_incivility()
        self.nb_indecency = self.read_nb_indecency()
        self.nb_incomprehension = self.read_nb_incomprehension()
        self.tmp_response = ''  # tempory attribut for message of grandpy
        self.key_data = {}
        self.redis_connect()

    def redis_connect(self):
        """
            method for connection to the Redis database
                - status_env["status_prod"] = False ==> Redis database in local
                - status_env["status_prod"] = True ==> Redis database in online
        """
        if not self.status_env["status_prod"]:
            self.connect = redis.Redis(
                host='localhost',
                port=6379,
                db=0
            )
        else:
            self.connect = redis.Redis(
                host="grandpy-papy-robot.herokuapp.com/",
                port=6379,
                db=1
           )


    #==================================
    # converting data values for Redis
    #==================================
    # boolean ==> string
    @staticmethod
    def bool_convers(value):
        """
            conversion from boolean to string
        """
        if value :
            return '1'
        else:
            return '0'
    
    # string ==> boolean
    @staticmethod
    def str_convers(value):
        """
            conversion from string to boolean
        """
        value = value.decode('utf8')
        if value == '0':
            return False
        elif value == '':
            return False
        else:
            return True

    # Google API keys
    @property
    def status_env(self):
        """
            management of environment variables
            local and online
                - key_data["map"]         ==> =|
                - key_data["staticMap"]   ==> =|- private keys for Google APIs
                                                  (local or online)
                - key_data["status_prod"] ==> boolean for redis database
                                              connection method
        """
        if os.environ.get("HEROKU_KEY_API_MAP") is None:
            self.key_data["map"] = os.getenv("KEY_API_MAP")
            self.key_data["staticMap"] = os.getenv("KEY_API_STATIC_MAP")
            self.key_data["status_prod"] = False
        else:
            self.key_data["map"] = os.getenv("HEROKU_KEY_API_MAP")
            self.key_data["staticMap"] = os.getenv("HEROKU_KEY_API_STATIC_MAP")
            self.key_data["status_prod"] = True
        return self.key_data

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


    #==============================================
    # value of data Civility in the Redis database
    #==============================================
    def write_civility(self, civility):
        """
            saving of civility configuration in Redis database
        """
        self.writing('civility', self.bool_convers(civility))

    def read_civility(self):
        """
            reading of civility configuration in Redis database
        """
        return self.str_convers(self.reading('civility'))


    #============================================
    # value of data quotas in the Redis database
    #============================================
    def write_quotas(self, quotas):
        """
            saving of quotas configuration in Redis database
        """
        self.writing('quotas', self.bool_convers(quotas))

    def read_quotas(self):
        """
            reading of quotas configuration in Redis database
        """
        return self.str_convers(self.reading('quotas'))


    #=============================================
    # value of data decency in the Redis database
    #=============================================
    def write_decency(self, decency):
        """
            saving of decency configuration in Redis database
        """
        self.writing('decency', self.bool_convers(decency))

    def read_decency(self):
        """
            reading of decency configuration in Redis database
        """
        return self.str_convers(self.reading('decency'))


    #===================================================
    # value of data comprehension in the Redis database
    #===================================================
    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration in Redis database
        """
        self.writing('comprehension', self.bool_convers(comprehension))

    def read_comprehension(self):
        """
            reading of comprehension configuration in Redis database
        """
        return self.str_convers(self.reading('comprehension'))


    #=================================================
    # value of data Counter Request in Redis database
    #=================================================
    def increment_counter(self):
        """
            Counter increment in Redis database
        """
        self.writing(
            'nb_request', write_counter(self.incrementing('nb_request'))
        ) 

    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter) in Redis database
        """
        self.expiry('nb_request', 86400)

    def write_counter(self, value):
        """
            modification of the value
            of the request counter in Redis database
        """
        self.writing('nb_request', value)

    def read_counter(self):
        """
            reading of counter configuration in Redis database
        """
        return self.reading('nb_request')


    #====================================================
    # value of data Counter incivility in Redis database
    #====================================================
    def write_incivility(self, value):
        """
            counter incivility in Redis Database
        """
        self.writing('nb_incivility', value)
    
    def read_incicility(self):
        """
            reading of incivility count in Redis database
        """
        return self.reading('nb_incivility')


    #===================================================
    # value of data Counter indecency in Redis database
    #===================================================
    def write_indecency(self, value):
        """
            counter indecency in Redis Database
        """
        self.writing('nb_indecency', value)

    def read_indecency(self):
        """
            reading of indecency count in Redis database
        """
        return self.reading('nb_indecency')


    #=========================================================
    # value of data Counter incomprehension in Redis database
    #=========================================================
    def write_incomprehension(self, value):
        """
            counter incomprehension in Redis Database
        """
        self.writing('nb_incomprehension', value)

    def read_incomprehension(self):
        """
            reading of incomprehension count in Redis database
        """
        return self.reading('nb_incomprehension')


    #============================================
    # grandpy's response value in Redis database
    #============================================
    def write_response(self, value):
        """
            grandpy's response in Redis Database
        """
        self.writing('gp_response', value)

    def read_response(self):
        """
            reading of grandpy's response in Redis database
        """
        return self.reading('gp_response')

    #==================================
    # Initialization status parameters
    #==================================
    def initial_status(self):
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

    def update_redis(self):
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
        self.write_response(self.tmp_response)

    def reset_behavior(self):
        """
            initialisation behavior parameters:
                - comprehension --|
                - civility -------| ==> False
                - decency --------|
        """
        self.comprehension = False
        self.decency = False
        self.civility = False


    #==========================
    # status parameter display
    #==========================
    def display_status(self, question):
        """
            display of data values in the question
                - Args Value ==> [
                    tmp (user question), quotas, civility, decency, comprehension,
                    nb_request, nb_incivility, nb_indecency, nb_incomprehension,
                    tmp_response (grandpy's response)
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
        print(f'Réponse de grandpy = {self.tmp_response}')


if __name__ == '__main__':
    pass
