#coding:utf-8
#!/usr/bin/env python
"""
    internal conversation data processing module
"""

import redis
from .dataapi import ApiDataConfig
from .user import Question
from . import grandpyrobot

class BehaviorDatabase:
    """
        Management for initializing configuration database data
          - get_data_access() ==> data initialization for the data database
          - boolean_to_string_conversion()--
                                            |
          - string_to_boolean_conversion()--|-- ==> converter between
                                            |       database and local data
          - string_to_int_conversion()------
    """
    def __init__(self):
        """
            database initialization
        """
        self.return_grandpy_response = grandpyrobot
        self._api_config = ApiDataConfig()
        self.status_prod = self._api_config.get_keys['status_prod']
        self.data = self.get_data_access()

    #---------------------- CALCULATION AND PROPERTY -------------------

    @staticmethod
    def boolean_to_string_conversion(value):
        """
            conversion from boolean to string
        """
        if value :
            value = 'True'
        else:
            value = 'False'
        return value

    @staticmethod
    def string_to_boolean_conversion(value):
        """
            conversion from string to boolean
        """
        if value == 'False':
            value = False
        elif value == 'True':
            value = True
        else:
            value = False
        return value

    @staticmethod
    def string_to_int_conversion(value):
        """
            conversion from string to integer
        """
        return int(value)

    #---------------------- ACCESS CHAT database -----------------------

    def get_data_access(self):
        """
            method for data_connection to the database
                - keys["status_prod"] = False ==> data in local
                - keys["status_prod"] = True ==> data in online
        """
        redis_connect = ''
        if not self.status_prod:
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

#----------------------- ACCESS CHAT DATA ------------------------------

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
    def write_user_civility(self, civility):
        """
            saving of civility configuration in data database
        """
        self.writing('user_civility', self.boolean_to_string_conversion(civility))

    @property
    def read_user_civility(self):
        """
            reading of civility configuration in data database
        """
        return self.string_to_boolean_conversion(self.reading('user_civility'))

                   #-----------------------------

    def write_user_decency(self, decency):
        """
            saving of decency configuration in data database
        """
        self.writing('user_decency', self.boolean_to_string_conversion(decency))

    @property
    def read_user_decency(self):
        """
            reading of decency configuration in data database
        """
        return self.string_to_boolean_conversion(self.reading('user_decency'))

                    #-----------------------------

    def write_user_comprehension(self, comprehension):
        """
            saving of comprehension configuration in data database
        """
        self.writing(
            'user_comprehension', self.boolean_to_string_conversion(comprehension)
        )

    @property
    def read_user_comprehension(self):
        """
            reading of comprehension configuration in data database
        """
        return self.string_to_boolean_conversion(
            self.reading('user_comprehension')
        )

                    #---------request limit--------------------

    def write_user_request_quotas(self, quotas):
        """
            saving of quotas configuration in data database
        """
        self.writing('request_quotas', self.boolean_to_string_conversion(quotas))

    def expiry_user_request_quotas(self):
        """
            Expiration of the key quotas (limit of request) in data database
        """
        self.expiry('request_quotas', 60)

    @property
    def read_user_request_quotas(self):
        """
            reading of quotas configuration in data database
        """
        return self.string_to_boolean_conversion(self.reading('request_quotas'))

                        #-----------------------

    def write_counter_of_number_of_user_request(self, value):
        """
            modification of the value
            of the request counter in data database
        """
        self.writing('number_request', value)

    @property
    def read_counter_of_number_of_user_request(self):
        """
            reading of counter configuration in data database
        """
        return self.string_to_int_conversion(self.reading('number_request'))

                        #------------------------

    def write_counter_of_number_of_user_incivility(self, value):
        """
            counter incivility in data database
        """
        self.writing('number_incivility', value)

    @property
    def read_counter_of_number_of_user_incivility(self):
        """
            reading of incivility count in data database
        """
        return self.string_to_int_conversion(self.reading('number_incivility'))

                    #---------------------------

    def write_counter_of_number_of_user_indecency(self, value):
        """
            counter indecency in data database
        """
        self.writing('number_indecency', value)

    @property
    def read_counter_of_number_of_user_indecency(self):
        """
            reading of indecency count in data database
        """
        return self.string_to_int_conversion(self.reading('number_indecency'))

                    #--------------------------

    def write_counter_of_number_of_user_incomprehension(self, value):
        """
            counter incomprehension in data database
        """
        self.writing('number_incomprehension', value)

    @property
    def read_counter_of_number_of_user_incomprehension(self):
        """
            reading of incomprehension count in data database
        """
        return self.string_to_int_conversion(
            self.reading('number_incomprehension')
        )

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
                                             of all counters value
        """
        self.deleting()
        self.write_user_civility(False)
        self.write_user_request_quotas(False)
        self.write_user_decency(False)
        self.write_user_comprehension(False)
        self.write_counter_of_number_of_user_request(0)
        self.write_counter_of_number_of_user_incivility(0)
        self.write_counter_of_number_of_user_indecency(0)
        self.write_counter_of_number_of_user_incomprehension(0)

# Initialization data chat
class BehaviorData(AccessBehaviorDataBase):
    """
        default variables data
            - request_quotas       ==> user behavior limit
            - number_incivility    ==> number of user incivlity
            - number_indecency     ==> number of user indecency
            - number_request       ==> number of user requests
            - initial_status() ==> initialization of data values
                                   from the data database
            - user_civility
            - user_decency
            - user_comprehension
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
            self.number_incomprehension =\
                self.read_counter_of_number_of_user_incomprehension
            self.request_quotas = self.read_user_request_quotas
        except (AttributeError, TypeError):
            self.get_initial_database()
            self.get_initial_attribute()
        self.user_civility = self.read_user_civility
        self.user_decency = self.read_user_decency
        self.user_comprehension = self.read_user_comprehension
        self.number_request = self.read_counter_of_number_of_user_request
        self.number_incivility = self.read_counter_of_number_of_user_incivility
        self.number_indecency = self.read_counter_of_number_of_user_indecency

    def get_initial_attribute(self):
        """
            Initialization all local values
        """
        self.user_civility = False
        self.request_quotas = False
        self.user_decency = False
        self.user_comprehension = False
        self.number_request = 0
        self.number_incivility = 0
        self.number_indecency = 0
        self.number_incomprehension = 0

    def get_display_data(self, ligne='Inconnu'):
        """
            display of data values in the question
                - Args Value ==>
                    request_quotas, user_civility, user_decency,
                    user_comprehension, number_request , number_incivility,
                    number_indecency, number_incomprehension, grandpy_response
        """
        print(f'\nN° de ligne = {ligne}')
        print(f'Valeur de quotas = {self.request_quotas}')
        print(f'Valeur de civility = {self.user_civility}')
        print(f'valeur de decency = {self.user_decency}')
        print(f'valeur de comprehension = {self.user_comprehension}')
        print(f'Nombre de request = {self.number_request}')
        print(f'Nombre d\'incivility = {self.number_incivility}')
        print(f'Nombre d\'indecency = {self.number_indecency}')
        print(f'Nombre d\'incomprehension = {self.number_incomprehension}')
        print(f'Réponse de grandpy = {self.grandpy_response}\n')

    def get_update_database(self):
        """
            update for database values
                - Args Value ==> 
                    request_quotas, user_civility, user_decency,
                    user_comprehension, number_request, number_incivility,
                    number_indecency, number_incomprehension
        """
        self.write_user_request_quotas(self.request_quotas)
        self.write_user_civility(self.user_civility)
        self.write_user_decency(self.user_decency)
        self.write_user_comprehension(self.user_comprehension)
        self.write_counter_of_number_of_user_request(self.number_request)
        self.write_counter_of_number_of_user_incivility(self.number_incivility)
        self.write_counter_of_number_of_user_indecency(self.number_indecency)
        self.write_counter_of_number_of_user_incomprehension(
            self.number_incomprehension
        )

    def get_reset_behavior(self):
        """
            initialisation behavior parameters:
                - comprehension --|
                                  | ==> False
                - decency --------|
        """
        self.user_decency = False
        self.user_comprehension = False
        self.user_civility = False
        self.number_incivility = 0
        self.number_indecency = 0
        self.number_incomprehension = 0

    # Expiration data of request
    def get_expiration_data(self):
        """
            update quota data for its expiration
        """
        self.request_quotas = True
        self.grandpy_code = 'exhausted'
        self.get_display_data()

    def user_behavior_limited(self):
        """
            user  behavior limited a 
                - 3 incivilities     ==> number_incivility
                - 3 indecencies      ==> number_indecency
                - 3 incomprehensions ==> number_indecency
                - 10 requests        ==> limit of request before saturation of grandpy
            user behavior journey 
            up to 4 requests no fatigue from grandpy
            at the 5th request grandpy starts to get tired
        """
        if self.number_incivility >= 3:
            self.return_grandpy_response.get_response_grandpy('incivility_limit')
        if self.number_indecency >= 3:
            self.return_grandpy_response.get_response_grandpy('indecency_limit')
        if self.number_incomprehension >= 3:
            self.return_grandpy_response.get_response_grandpy('incomprehension_limit')
        if self.number_request == 0:
            self.return_grandpy_response.get_response_grandpy('wait1')
            self.grandpy_code = ''
        elif 1 <= self.number_request <= 4 or 6 <= self.number_request <= 9 :
            self.return_grandpy_response.get_response_grandpy('response')
            self.grandpy_code = 'response'
        elif self.number_request == 5:
            self.return_grandpy_response.get_response_grandpy('response')
            self.grandpy_code = 'tired'
        else:
            self.get_expiration_data()
            self.return_grandpy_response.get_response_grandpy('quotas')

# chat organization
class Chat:
    """
        object management user and grandpy chat
    """
    def __init__(self, user_question):
        """
            Initialization
                - user object
                - grandpy objet
        """
        self.behavior_data = BehaviorData()
        self.return_grandpy_response =\
            self.behavior_data.return_grandpy_response
        self.return_user_behavior_data = Question(
            user_question, self.behavior_data
        )

    #-------------------- user behavior --------------------------------

    def obtain_processing_of_user_behavior_data(
        self, user_behavior_processing_key
    ):
        """
            Processing user's questions
        """
        user_behavior_data =\
            self.return_user_behavior_data.\
            get_return_user_behavior_data(user_behavior_processing_key)
            
        return user_behavior_data

    #------------------- grandpy robot behavior ------------------------

    def get_grandpy_answer_processing(self, grandpy_response_processing_key):
        """
            Processing grandpy's responses
        """
        grandpy_message =\
            self.return_grandpy_response.\
            get_response_grandpy(grandpy_response_processing_key)
        return grandpy_message

if __name__ == '__main__':
    pass
