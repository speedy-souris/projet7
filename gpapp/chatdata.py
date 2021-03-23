#coding:utf-8
#!/usr/bin/env python
"""
    internal conversation data processing module
"""
import redis

from .dataapi import ApiGoogleMaps


class BehaviorDatabase(ApiGoogleMaps):
    """
        Management for initializing configuration database data
          - get_data_access() ==> data initialization for the data database
          - bool_convers()
          - str_convers()
          - int_convers()
    """
    def __init__(self):
        """
            database initialization
        """
        super().__init__()
        self.data = self.get_data_access

    #---------------------- CALCULATION AND PROPERTY -------------------

    @staticmethod
    def bool_convers(value):
        """
            conversion from boolean to string
        """
        if value :
            value = '1'
        else:
            value = '0'
        return value

    @staticmethod
    def str_convers(value):
        """
            conversion from string to boolean
        """
        value = value.decode("utf8")
        if value == '0':
            value = False
        elif value == '':
            value = False
        else:
            value = True
        return value

    @staticmethod
    def str_int(value):
        """
            conversion from string to integer
        """
        return int(value)

    #---------------------- ACCESS CHAT database -----------------------

    @property
    def get_data_access(self):
        """
            method for data_connection to the database
                - keys["status_prod"] = False ==> data in local
                - keys["status_prod"] = True ==> data in online
        """
        redis_connect = ''
        if not self.get_keys['status_prod']:
            redis_connect = redis.Redis(
                host='localhost',
                port=6379,
                db=0
            )
        else:
            redis_connect = redis.Redis(
                host='grandpy-papy-robot.herokuapp.com/',
                port=6379,
                db=1
           )
        return redis_connect

    #----------------------- ACCESS CHAT DATA --------------------------

class CreateBehaviorDataBase(BehaviorDatabase):
    """
        redis data processing initialization
        - writing()  ==> writing of data value for the data database
        - expiry()   ==> data value expiration times for the data database
        - reading()  ==> read data value for the data database
        - deleting() ==> data erasure from the database
    """
    def writing(self, data, value):
        """
            writing chat data to data database
        """
        self.data.set(data, value)

    def expiry(self, data, value):
        """
            expiration
            of the counter variable in database
            (after 24 hours)
        """
        self.data.expire(data, value)


    def reading(self, data):
        """
            reading data in database
        """
        return self.data.get(data)

    def deleting(self):
        """
            deleting all data
        """
        return self.data.flushall()

                    #----------------------------

class AccessBehaviorDataBase(CreateBehaviorDataBase):
    """
        access to redis data processing
        - reading
        - writing
    """
    def write_civility(self, civility):
        """
            saving of civility configuration in data database
        """
        self.writing('civility', self.bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration in data database
        """
        return self.str_convers(self.reading('civility'))

                   #-----------------------------

    def write_decency(self, decency):
        """
            saving of decency configuration in data database
        """
        self.writing('decency', self.bool_convers(decency))

    @property
    def read_decency(self):
        """
            reading of decency configuration in data database
        """
        return self.str_convers(self.reading('decency'))

                    #-----------------------------

    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration in data database
        """
        self.writing('comprehension', self.bool_convers(comprehension))

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration in data database
        """
        return self.str_convers(self.reading('comprehension'))

                    #---------request limit--------------------

    def write_quotas(self, quotas):
        """
            saving of quotas configuration in data database
        """
        self.writing('quotas', self.bool_convers(quotas))

    def expiry_request(self):
        """
            Expiration of the key quotas (limit of request) in data database
        """
        self.expiry('quotas', 60)

    @property
    def read_quotas(self):
        """
            reading of quotas configuration in data database
        """
        return self.str_convers(self.reading('quotas'))

                        #-----------------------

    def write_counter(self, value):
        """
            modification of the value
            of the request counter in data database
        """
        self.writing('nb_request', value)

    @property
    def read_counter(self):
        """
            reading of counter configuration in data database
        """
        return self.str_int(self.reading('nb_request'))

                        #------------------------

    def write_incivility(self, value):
        """
            counter incivility in data database
        """
        self.writing('nb_incivility', value)

    @property
    def read_incivility(self):
        """
            reading of incivility count in data database
        """
        return self.str_int(self.reading('nb_incivility'))

                    #---------------------------

    def write_indecency(self, value):
        """
            counter indecency in data database
        """
        self.writing('nb_indecency', value)

    @property
    def read_indecency(self):
        """
            reading of indecency count in data database
        """
        return self.str_int(self.reading('nb_indecency'))

                    #--------------------------

    def write_incomprehension(self, value):
        """
            counter incomprehension in data database
        """
        self.writing('nb_incomprehension', value)

    @property
    def read_incomprehension(self):
        """
            reading of incomprehension count in data database
        """
        return self.str_int(self.reading('nb_incomprehension'))

    #----------------- GENERAL PROCESSING OF CHAT DATA -----------------

    def get_initial_database(self):
        """ creation and initialization by default of data values
            for the data database
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
        """
        self.deleting()
        self.write_civility(False)
        self.write_quotas(False)
        self.write_decency(False)
        self.write_comprehension(False)
        self.write_counter(0)
        self.write_incivility(0)
        self.write_indecency(0)

    def get_update_database(self):
        """
            update for database data
                - Args Value ==> [
                    quotas, civility, decency, comprehension, nb_request,
                    nb_incivility, nb_indecency, nb_incomprehension
                ]
        """
        local_data = BehaviorData()
        self.write_quotas(local_data.quotas)
        self.write_civility(local_data.civility)
        self.write_decency(local_data.decency)
        self.write_comprehension(local_data.comprehension)
        self.write_counter(local_data.nb_request)
        self.write_incivility(local_data.nb_incivility)
        self.write_indecency(local_data.nb_indecency)
        self.write_incomprehension(local_data.nb_incomprehension)

# Initialization data chat
class BehaviorData(AccessBehaviorDataBase):
    """
        default variables data
            - quotas           ==> initialisation of quotas attribut
            - nb_indecency     ==> number of user indecency
            - nb_request       ==> number of user requests
            - data_data_data()  ==> initialization of the data_dataion method
                                   to the data database
            - initial_status() ==> initialization of data values
                                   from the data database
            - civility
            - decency
            - comprehension
    """
    def __init__(self):
        """
            data chat initialization
        """
        super().__init__()
        self.grandpy_response = ''
        self.grandpy_code = ''
        # control of query expiration
        try:
            self.nb_incomprehension = self.read_incomprehension
            self.quotas = self.read_quotas
        except (AttributeError, TypeError):
            self.get_initial_database()
            self.get_initial_attribute()
        self.civility = self.read_civility
        self.decency = self.read_decency
        self.comprehension = self.read_comprehension
        self.nb_request = self.read_counter
        self.nb_incivility = self.read_incivility
        self.nb_decency = self.read_indecency

    def get_initial_attribute(self):
        """
            Initialization all values
        """
        self.civility = False
        self.quotas = False
        self.decency = False
        self.comprehension = False
        self.nb_request = 0
        self.nb_incivility = 0
        self.nb_indecency = 0
        self.nb_incomprehension = 0

    def get_display_data(self, ligne='Inconnu'):
        """
            display of data values in the question
                - Args Value ==> [
                    tmp (user question), quotas, civility, decency, comprehension,
                    nb_request, nb_incivility, nb_indecency, nb_incomprehension,
                    grandpy_response (grandpy's response)
                ]
        """
        print(f'\nN° de ligne = {ligne}')
        print(f'Valeur de quotas = {self.quotas}')
        print(f'Valeur de civility = {self.civility}')
        print(f'valeur de decency = {self.decency}')
        print(f'valeur de comprehension = {self.comprehension}')
        print(f'Nombre de request = {self.nb_request}')
        print(f'Nombre d\'incivility = {self.nb_incivility}')
        print(f'Nombre d\'indecency = {self.nb_indecency}')
        print(f'Nombre d\'incomprehension = {self.nb_incomprehension}')
        print(f'Réponse de grandpy = {self.grandpy_response}\n')

    def get_reset_behavior(self):
        """
            initialisation behavior parameters:
                - comprehension --|
                                  | ==> False
                - decency --------|
        """
        self.decency = False
        self.comprehension = False

    # Expiration data of request
    def get_expiration_data(self):
        """
            update quota data for its expiration
        """
        self.quotas = True
        self.grandpy_code = 'exhausted'
        self.get_display_data()

# chat organization
class Chat:
    """
        object management user and grandpy chat
    """
    def __init__(self, user, grandpy):
        """
            Initialization
                - user object
                - grandpy objet
        """
        self.user = user
        self.grandpy = grandpy

    #-------------------- user behavior --------------------------------

    def get_question(self, check):
        """
            Processing user's questions
        """
        return self.user.get_user_question(check)

    #------------------- grandpy robot behavior ------------------------

    def get_answer(self, stage):
        """
            Processing grandpy's responses
        """
        return self.grandpy.get_response_grandpy(stage)

if __name__ == '__main__':
    pass
