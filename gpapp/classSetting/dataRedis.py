#coding:utf-8
#!/usr/bin/env python

import redis
from .dataInitial import Parameter as config

#==============
# Server Redis
#==============
class RedisConnect:
    """
        Initialization of Redis connection parameters
            - CONNECT
    """

    if not config.status_env()["status_prod"]:
        CONNECT = redis.Redis(
            host="localhost",
            port=6379,
            db=0
        )
    else:
        CONNECT = redis.Redis(
            host="grandpy-papy-robot.herokuapp.com/",
            port=6379,
            db=1
        )

    @classmethod
    def writing(cls, data, value):
        """
            writing data to Redis
        """
        cls.CONNECT.set(data, value)

    @classmethod
    def incrementing(cls, data):
        """
            incrementing the request counter in Redis
        """
        cls.CONNECT.incr(data)

    @classmethod
    def expiry(cls, data, value):
        """
            expiration
            of the counter variable in Redis
            (after 24 hours)
        """
        cls.CONNECT.expire(data, value)

    @classmethod
    def reading(cls, data):
        """
            reading data in Redis
        """
        return cls.CONNECT.get(data)


                        #=================
                        # Data of setting
                        #=================
#============
# Quotas_api
#============
class QuotasSetting:
    """
        Management class for saving quotas configuration parameters:
            - quotas_api
    """
    def __init__(self):
        """
            constructor
            for initializing the quota_api variable in Redis
        """
        self.quotas = 0
        RedisConnect.writing("quotas_api", self.quotas)

    def write_quotas(self, quotas):
        """
            saving of quotas configuration
        """
        self.quotas = quotas
        RedisConnect.writing("quotas_api", self.quotas)

    @property
    def read_quotas(self):
        """
            reading of quotas configuration
        """
        return RedisConnect.reading("quotas_api")

#==========
# Civility
#==========
class CivilitySetting:
    """
        Management class for saving civility configuration parameters:
            - civility
    """
    def __init__(self):
        """
            constructor
            for initializing the civility variable in Redis
        """
        self.civility = 0
        RedisConnect.writing("civility", self.civility)

    def write_civility(self, civility):
        """
            saving of civility configuration
        """
        self.civility = civility
        RedisConnect.writing("civility", self.civility)

    @property
    def read_civility(self):
        """
            reading of civility configuration
        """
        return RedisConnect.reading("civility")

#=========
# Decency
#=========
class DecencySetting:
    """
        Management class for saving decency configuration parameters:
            - decency
    """
    def __init__(self):
        """
            constructor
            for initializing the decency variable in Redis
        """
        self.decency = 1
        RedisConnect.writing("decency", self.decency)

    def write_decency(self, decency):
        """
            saving of decency configuration
        """
        self.decency = decency
        RedisConnect.writing("decency", self.decency)

    @property
    def read_decency(self):
        """
            reading of decency configuration
        """
        return RedisConnect.reading("decency")

#===============
# comprehension
#===============
class ComprehensionSetting:
    """
        Management class for saving comprehension configuration parameters:
            - comprehension
    """
    def __init__(self):
        """
            constructor
            for initializing the comprehension variable in Redis
        """
        self.comprehension = 1
        RedisConnect.writing("comprehension", self.comprehension)

    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration
        """
        self.comprehension = comprehension
        RedisConnect.writing("comprehension", self.comprehension)

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration
        """
        return RedisConnect.reading("comprehension")

#=================
# Counter Request
#=================
class CounterSetting:
    """
        Management class for saving counter request configuration parameters:
            - nb_request
    """
    def __init__(self):
        """
            constructor
            for initializing the nb_request variable in Redis
        """
        self.nb_request = 0
        RedisConnect.writing("nb_request", self.nb_request)

    @property
    def increment_counter(self):
        """
            Counter increment
        """
        self.nb_request = RedisConnect.incrementing("nb_request")

    @property
    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter)
        """
        RedisConnect.expiry("nb_request", 86400)

    @property
    def read_counter(self):
        """
            reading of counter configuration
        """
        return RedisConnect.reading("nb_request")

    def write_counter(self, data, value):
        """
            modification of the value
            of the request counter in Redis
        """
        try:
            RedisConnect.writing(data, value)
        except TypeError:
            RedisConnect.writing("nb_request", 0)

                        #=================
                        # Initialization
                        # Data of setting
                        #=================

class DataRedis:
    """
        Management class for initializing configuration data
            - qotas
            - civility
            - decency
            - comprehension
            - counter
    """
    QUOTAS = QuotasSetting()
    CIVILITY = CivilitySetting()
    DECENCY = DecencySetting()
    COMPREHENSION = ComprehensionSetting()
    COUNTER = CounterSetting()

                        #======================
                        # Reading data setting
                        #======================
    @classmethod
    def readQuotas(cls):
        """
            reading the variable in Redis
        """
        return bool(int(cls.QUOTAS.read_quotas))

    @classmethod
    def readCivility(cls):
        """
            reading the variable in Redis
        """
        return bool(int(cls.CIVILITY.read_civility))

    @classmethod
    def readDecency(cls):
        """
            reading the variable in Redis
        """
        return bool(int(cls.DECENCY.read_decency))

    @classmethod
    def readComprehension(cls):
        """
            reading the variable in Redis
        """
        return bool(int(cls.COMPREHENSION.read_comprehension))

    @classmethod
    def readCounter(cls):
        """
            reading the variable in Redis
        """
        return int(cls.COUNTER.read_counter)

                        #======================
                        # writing data setting
                        #======================
    @classmethod
    def writeQuotas(cls, quotas):
        """
            writing the variable in Redis
        """
        cls.QUOTAS.write_quotas(int(quotas))

    @classmethod
    def writeCivility(cls, civility):
        cls.CIVILITY.write_civility(int(civility))

    @classmethod
    def writeDecency(cls, decency):
        """
            writing the variable in Redis
        """
        cls.DECENCY.write_decency(int(decency))

    @classmethod
    def writeComprehension(cls, comprehension):
        """
            writing the variable in Redis
        """
        cls.COMPREHENSION.write_comprehension(int(comprehension))

    @classmethod
    def writeCounter(cls):
        """
            writing the variable in Redis
        """
        cls.COUNTER.write_counter("nb_request", 0)


    @classmethod
    def expiryCounter(cls):
        """
            writing the variable in Redis
        """
        cls.COUNTER.expiry_counter

    @classmethod
    def incrementCounter(cls):
        """
            writing the variable in Redis
        """
        cls.COUNTER.increment_counter

