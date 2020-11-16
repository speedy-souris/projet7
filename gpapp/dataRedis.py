#coding:utf-8
#!/usr/bin/env python

import os
import redis


#=============================
# Initialization Server Redis
#=============================
class redis_connect:
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
        self.civility = False
        self.decency = False
        self.comprehension = False
        self.quotas = False
        self.nb_request = 0
        self.nb_incivility = 0
        self.nb_indecency = 0
        self.nb_incomprehension = 0
        self.key_data = {}
        self.connect()

    def connect(self):
        """
            method for connection to the Redis database
                - status_env["status_prod"] = False ==> Redis database in local
                - status_env["status_prod"] = True ==> Redis database in online
        """
        if not self.status_env["status_prod"]:
            redis.Redis(
                host='localhost',
                port=6379,
                db=0
            )
        else:
            redis.Redis(
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
    def status_env():
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
    def writing(data, value, connect):
        """
            writing data to Redis database
        """
        connect.set(data, value)

    # increment
    def incrementing(data, connect):
        """
            incrementing the request counter in Redis database
        """
        connect.incr(data)

    # expiration time
    def expiry(data, value, connect):
        """
            expiration
            of the counter variable in Redis database
            (after 24 hours)
        """
        connect.expire(data, value)

    # reading
    def reading(data, connect):
        """
            reading data in Redis database
        """
        return connect.get(data)


    #==============================================
    # value of data Civility in the Redis database
    #==============================================
    def write_civility(civility, connect):
        """
            saving of civility configuration in Redis database
        """
        connect.writing('civility', bool_convers(civility))

    def read_civility(connect):
        """
            reading of civility configuration in Redis database
        """
        return str_convers(connect.reading('civility'))


    #============================================
    # value of data quotas in the Redis database
    #============================================
    def write_quotas(quotas, connect):
        """
            saving of quotas configuration in Redis database
        """
        connect.writing('quotas', bool_convers(quotas))

    def read_quotas(connect):
        """
            reading of quotas configuration in Redis database
        """
        return str_convers(connect.reading('quotas'))


    #=============================================
    # value of data decency in the Redis database
    #=============================================
    def write_decency(decency, connect):
        """
            saving of decency configuration in Redis database
        """
        connect.writing('decency', bool_convers(decency))

    def read_decency(connect):
        """
            reading of decency configuration in Redis database
        """
        return str_convers(connect.reading('decency'))


    #===================================================
    # value of data comprehension in the Redis database
    #===================================================
    def write_comprehension(comprehension, connect):
        """
            saving of comprehension configuration in Redis database
        """
        connect.writing('comprehension', bool_convers(comprehension))

    def read_comprehension(connect):
        """
            reading of comprehension configuration in Redis database
        """
        return str_convers(connect.reading('comprehension'))


    #=================================================
    # value of data Counter Request in Redis database
    #=================================================
    def increment_counter(connect):
        """
            Counter increment in Redis database
        """
        connect.writing(
            'nb_request', write_counter(connect.incrementing('nb_request'))
        ) 

    def expiry_counter(connect):
        """
            Expiration of the key nb_request (counter) in Redis database
        """
        connect.expiry('nb_request', 86400)

    def write_counter(value, connect):
        """
            modification of the value
            of the request counter in Redis database
        """
        connect.writing('nb_request', value)

    def read_counter(connect):
        """
            reading of counter configuration in Redis database
        """
        return connect.reading('nb_request')


    #====================================================
    # value of data Counter incivility in Redis database
    #====================================================
    def write_incivility(value, connect):
        """
            counter incivility in Redis Database
        """
        connect.writing('nb_incivility', value)
    
    def read_incicility(connect):
        """
            reading of incivility count in Redis database
        """
        return connect.reading('nb_incivility')


    #====================================================
    # value of data Counter indecency in Redis database
    #====================================================
    def write_indecency(value, connect):
        """
            counter indecency in Redis Database
        """
        connect.writing('nb_indecency', value)

    def read_indecency(connect):
        """
            reading of indecency count in Redis database
        """
        return connect.reading('nb_indecency')


    #====================================================
    # value of data Counter incomprehension in Redis database
    #====================================================
    def write_incomprehension(value, connect):
        """
            counter incomprehension in Redis Database
        """
        connect.writing('nb_incomprehension', value)

    def read_incomprehension(connect):
        """
            reading of incomprehension count in Redis database
        """
        return connect.reading('nb_incomprehension')


    #==================================
    # Initialization status parameters
    #==================================
    def initial_status(connect):
        """ creation and initialization by default of data values
            for the Redis database
    
                - write_ civility()  ==> default initialization 
                                         of civility value
                - write_quotas()  ==> default initialization 
                                      of quotas value
                - write_decency()  ==> default initialization
                                       of decency value
                - write_comprehension()  ==> default initialization
                                             of comprehension value
                - write_counter()  ==> default initialization of counter value
        """
        connect.write_civility(False)
        connect.write_quotas(False)
        connect.write_decency(False)
        connect.write_comprehension(False)
        connect.write_counter(0)
        connect.write_incivility(0)
        connect.write_indecency(0)
        connect.write_incomprehension(0)

    def update_redis(Args, connect):
        """
            update for database redis
                - Args Value ==> [
                    quotas, civility, decency, comprehension, nb_request, 
                    nb_incivility, nb_indecency, nb_incomprehension
                ]
        """
        connect.write_quotas(Args[0])
        connect.write_civility(Args[1])
        connect.write_decency(Args[2])
        connect.write_comprehension(Args[3])
        connect.write_counter(Args[4])
        connect.write_incivility(Args[5])
        connect.write_indecency(Args[6])
        connect.writeiincomprehension(Args[7])

    def reset_behavior(self):
        """
            initialisation behavior parameters:
                - comprehension --|
                - civility -------| ==> False
                - decency --------|
                - data -----------|
        """
        self.comprehension = False
        self.decency = False
        self.civility = False


    #==========================
    # status parameter display
    #==========================
    def display_status(Args):
        """
            display of data values in the question
                - Args Value ==> [
                    tmp (user question), quotas, civility, decency, comprehension,
                    nb_request, nb_incivility, nb_indecency, nb_incomprehension
                ]
        """
        print(f'question = {Args[0]}\n')
        print(f'Valeur de quotas = {Args[1]}')
        print(f'Valeur de civility = {Args[2]}')
        print(f'valeur de decency = {Args[3]}')
        print(f'valeur de comprehension = {Args[4]}')
        print(f'Nombre de request = {Args[5]}')
        print(f"Nombre d'incivility = {Args[6]}")
        print(f"Nombre d'indecency = {Args[7]}")
        print(f"Nombre d'incomprehension = {Args[8]}")


