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
            - data_data_data()  ==> initialization of the data_dataion method
                                   to the data database
            - initial_status() ==> initialization of data values
                                   from the data database
            - civility
            - decency
            - comprehension
    API Private Key and Constants Management :
        local (development) / external (production)
            keys()
                - key_value['map']         ==> KEY_API_MAP / HEROKU_KEY_API_MAP
                - key_value['staticMap']   ==> KEY_API_STATIC_MAP / HEROKU_KEY_API_STATIC_MAP
                - key_value['status_prod'] ==> True / False
    Management for initializing configuration database data
        - data_data_data() ==> data_dataion initialization for the data database
        - writing()       ==> writing of data value for the data database
        - expiry()        ==> data value expiration times for the data database
        - reading         ==> read data value for the data database
    """
    def __init__(self):
        """
            data chat initialization constructor
        """
        self.key_value = {}
        self.data = self.data_access
        self.grandpy_response = ''
        self.grandpy_code = ''
        self.civility = self.read_civility
        self.decency = self.read_decency
        self.comprehension = self.read_comprehension
        self.nb_request = self.read_counter
        self.nb_incivility = self.read_incivility
        self.nb_indecency = self.read_indecency
        self.nb_incomprehension = self.read_incomprehension
        # control of query expiration
        try:
            self.quotas = self.read_quotas
        except AttributeError:
            self.initial_attribute()
            self.initial_dataBase()

#---------------------- CALCULATION AND PROPERTY -----------------------

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

    # keys for Google APIs in environment variables
    @property
    def keys(self):
        """
            management of environment variables
            local and online
                - key_value["map"]         ==> =|
                - key_value["staticMap"]   ==> =|- private keys for Google APIs
                                                  (local or online)
                - key_value["status_prod"] ==> boolean for data database
                                              data_dataion method
        """
        # keys for local use (Dev)
        if os.environ.get('HEROKU_KEY_API_MAP') is None:
            self.key_value = {
                'map': os.getenv('KEY_API_MAP'),
                'staticMap': os.getenv('KEY_API_STATIC_MAP'),
                'status_prod': False
            }
        # keys for online use (Prod)
        else:
            self.key_value = {
                'map': os.getenv('HEROKU_KEY_API_MAP'),
                'staticMap': os.getenv('HEROKU_KEY_API_STATIC_MAP'),
                'status_prod': True
            }
        return self.key_value

#---------------------- ACCESS CHAT DATABASE ---------------------------

    @property
    def data_access(self):
        """
            method for data_dataion to the data database
                - keys["status_prod"] = False ==> data database in local
                - keys["status_prod"] = True ==> data database in online
        """
        if not self.keys['status_prod']:
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
           
#----------------------- ACCESS CHAT DATA ------------------------------

    def writing(self, data, value):
        """
            writing chat data to data database
        """
        self.data.set(data, value)

    def expiry(self, data, value):
        """
            expiration
            of the counter variable in data database
            (after 24 hours)
        """
        self.data.expire(data, value)
        

    def reading(self, data):
        """
            reading data in data database
        """
        return self.data.get(data)

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

#----------------- GENERAL PROCESSING OF CHAT DATA ---------------------

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
        self.write_civility(False)
        self.write_quotas(False)
        self.write_decency(False)
        self.write_comprehension(False)
        self.write_counter(0)
        self.write_incivility(0)
        self.write_indecency(0)
        self.write_incomprehension(0)

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

    def initial_value(self):
        """
            Initialization of counter values
        """
        self.nb_incivility = 0
        self.nb_indecency = 0
        self.nb_incomprehension = 0

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

    def display_data(self, ligne='Inconnu'):
        """
            display of data values in the question
                - Args Value ==> [
                    tmp (user question), quotas, civility, decency, comprehension,
                    nb_request, nb_incivility, nb_indecency, nb_incomprehension,
                    grandpy_response (grandpy's response)
                ]
        """
        print(f'N° de ligne = {ligne}')
        print(f'Valeur de quotas = {self.quotas}')
        print(f'Valeur de civility = {self.civility}')
        print(f'valeur de decency = {self.decency}')
        print(f'valeur de comprehension = {self.comprehension}')
        print(f'Nombre de request = {self.nb_request}')
        print(f'Nombre d\'incivility = {self.nb_incivility}')
        print(f'Nombre d\'indecency = {self.nb_indecency}')
        print(f'Nombre d\'incomprehension = {self.nb_incomprehension}')
        print(f'Réponse de grandpy = {self.grandpy_response}')

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

if __name__ == '__main__':
    pass
