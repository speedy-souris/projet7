#coding:utf-8
#!/usr/bin/env python

from .initial import Parameter as config
import redis

#==============
# Server Redis
#==============
class RedisConnect:
    """
        Initialization of Redis connection parameters
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
    def writing(cls, data):
        cls.CONNECT.set(data[0], data[1])

    @classmethod
    def incrementing(cls, counter):
        cls.CONNECT.incr(counter)

    @classmethod
    def expiry(cls, counter):
        cls.CONNECT.expire(counter[0],counter[1])

    @classmethod
    def reading(cls, data):
        return cls.CONNECT.get(data)

#============================
# Initialization Map Status
#============================
class InitMap:
    """
        initialization of the default settings
        for displaying the map (grandpy response)
    """
    def __init__(self):
        self.map_status = {}

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
        self.quotas = 0
        data_redis = ("quotas_api", self.quotas)
        RedisConnect.writing(data_redis)

    def write_quotas(self, quotas):
        """
            saving of quotas configuration
        """
        self.quotas = quotas
        data_quotas = ("quotas_api", self.quotas)
        RedisConnect.writing(data_quotas)

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
        self.civility = 0
        data_redis = ("civility", self.civility)
        RedisConnect.writing(data_redis)

    def write_civility(self, civility):
        """
            saving of civility configuration
        """
        self.civility = civility
        data_civility = ("civility", self.civility)
        RedisConnect.writing(data_civility)

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
        self.decency = 1
        data_redis = ("decency", self.decency)
        RedisConnect.writing(data_redis)

    def write_decency(self, decency):
        """
            saving of decency configuration
        """
        self.decency = decency
        data_decency = ("decency", self.decency)
        RedisConnect.writing(data_decency)

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
        self.comprehension = 1
        data_redis = ("comprehension", self.comprehension)
        RedisConnect.writing(data_redis)

    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration
        """
        self.comprehension = comprehension
        data_comprehension = ("comprehension", self.comprehension)
        RedisConnect.writing(data_comprehension)

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
        self.nb_request = 0
        RedisConnect.writing(("nb_request", self.nb_request))

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
        RedisConnect.expiry(("nb_request", 86400))

    @property
    def read_counter(self):
        """
            reading of counter configuration
        """
        return RedisConnect.reading("nb_request")

    def write_counter(self, counter):
        try:
            RedisConnect.writing((counter[0], counter[1]))
        except TypeError:
            RedisConnect.writing(("nb_request", 0))

                        #=================
                        # Initialization
                        # Data of setting
                        #=================

class DataSetting:
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
    STATUS = InitMap()

                        #======================
                        # Reading data setting
                        #======================
    @classmethod
    def readQuotas(cls):
        return bool(int(cls.QUOTAS.read_quotas))

    @classmethod
    def readCivility(cls):
        return bool(int(cls.CIVILITY.read_civility))

    @classmethod
    def readDecency(cls):
        return bool(int(cls.DECENCY.read_decency))

    @classmethod
    def readComprehension(cls):
        return bool(int(cls.COMPREHENSION.read_comprehension))

    @classmethod
    def readCounter(cls):
        return int(cls.COUNTER.read_counter)

                        #======================
                        # writing data setting
                        #======================
    @classmethod
    def writeQuotas(cls, quotas):
        cls.QUOTAS.write_quotas(int(quotas))

    @classmethod
    def writeCivility(cls, civility):
        cls.CIVILITY.write_civility(int(civility))

    @classmethod
    def writeDecency(cls, decency):
        cls.DECENCY.write_decency(int(decency))

    @classmethod
    def writeComprehension(cls, comprehension):
        cls.COMPREHENSION.write_comprehension(int(comprehension))

    @classmethod
    def writeCounter(cls):
        cls.COUNTER.write_counter(("nb_request", 0))


    @classmethod
    def expiryCounter(cls):
        cls.COUNTER.expiry_counter

    @classmethod
    def incrementCounter(cls):
        cls.COUNTER.increment_counter

                        #==================
                        # reading data map
                        #==================
    @classmethod
    def readResponse(cls):
        return cls.STATUS.map_status
                        #==================
                        # writing data map
                        #==================
    # ~ @classmethod
    # ~ def response(cls, data):
        # ~ cls.STATUS.map_status["address"] = data[0]
        # ~ cls.STATUS.map_status["history"] = data[1]
        # ~ return cls.STATUS.map_status

    @classmethod
    def address_map(cls, address):
        cls.STATUS.map_status["address"] = address
        return cls.STATUS.map_status

    @classmethod
    def history_map(cls, history):
        cls.STATUS.map_status["history"] = history
        return cls.STATUS.map_status

if __name__ == "__main__":
    pass
