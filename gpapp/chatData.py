#coding:utf-8
#!/usr/bin/env python

import os
import redis
from .answerSearch import KeyManagement 

class BehaviorDatabase:
    """
        Management for initializing configuration database data
        - data_data_data() ==> data_dataion initialization for the data database
        - writing()       ==> writing of data value for the data database
        - expiry()        ==> data value expiration times for the data database
        - reading         ==> read data value for the data database
    """
    def __init__(self):
        """
            database initialization 
        """
        self.statusProd = KeyManagement().keys['status_prod']
        self.data = self.data_access

    #---------------------- CALCULATION AND PROPERTY -------------------

    @staticmethod
    def bool_convers(value):
        """
            conversion from boolean to string
        """
        if value :
            return '1'
        else:
            return '0'

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

    @staticmethod
    def str_int(value):
        """
            conversion from string to integer
        """
        return int(value)

    #---------------------- ACCESS CHAT DATABASE -----------------------

    @property
    def data_access(self):
        """
            method for data_connection to the database
                - keys["status_prod"] = False ==> data in local
                - keys["status_prod"] = True ==> data in online
        """
        if not self.statusProd:
            return redis.Redis(
                host='localhost',
                port=6379,
                db=0
            )
        else:
            return redis.Redis(
                host='grandpy-papy-robot.herokuapp.com/',
                port=6379,
                db=1
           )

    #----------------------- ACCESS CHAT DATA --------------------------

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
            counter incivility in data Database
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
            counter indecency in data Database
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
            counter incomprehension in data Database
        """
        self.writing('nb_incomprehension', value)

    @property
    def read_incomprehension(self):
        """
            reading of incomprehension count in data database
        """
        return self.str_int(self.reading('nb_incomprehension'))

    #----------------- GENERAL PROCESSING OF CHAT DATA -----------------

    def initial_dataBase(self):
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

    def update_dataBase(self):
        """
            update for database data
                - Args Value ==> [
                    quotas, civility, decency, comprehension, nb_request, 
                    nb_incivility, nb_indecency, nb_incomprehension
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

# Initialization data chat
class BehaviorData:
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
        self.behaviorDB = BehaviorDatabase()
        self.grandpy_response = ''
        self.grandpy_code = ''
        # control of query expiration
        try:
            self.nb_incomprehension = self.behaviorDB.read_incomprehension
            self.quotas = self.behaviorDB.read_quotas
        except (AttributeError, TypeError):
            self.behaviorDB.initial_dataBase()
            self.initial_attribute()
        self.civility = self.behaviorDB.read_civility
        self.decency = self.behaviorDB.read_decency
        self.comprehension = self.behaviorDB.read_comprehension
        self.nb_request = self.behaviorDB.read_counter
        self.nb_incivility = self.behaviorDB.read_incivility
        self.nb_indecency = self.behaviorDB.read_indecency

    def initial_attribute(self):
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

    def display_data(self, ligne='Inconnu'):
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

    def reset_behavior(self):
        """
            initialisation behavior parameters:
                - comprehension --|
                                  | ==> False
                - decency --------|
        """
        self.decency = False
        self.comprehension = False

    # Expiration data of request
    def expiration_data(self):
        self.quotas = True
        self.grandpy_code = 'exhausted'
        self.display_data()

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
    def question(self, check):
        return self.user.message(check)

    #------------------- grandpy robot behavior ------------------------
    def answer(self, stage):
        return self.grandpy.message(stage)

if __name__ == '__main__':
    pass
