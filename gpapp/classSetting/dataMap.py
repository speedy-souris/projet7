#coding:utf-8
#!/usr/bin/env python

#============================
# Initialization Map Status
#============================
class InitMap:
    """
        initialization of the default settings
        for displaying the map (grandpy response)
    """
    def __init__(self):
        """
            constructeur of initialization
        """
        self.map_status = {}

class DataMap:
    """
        management class for geographic coordinates of the map and
        the address history in wikipedia
    """
    STATUS = InitMap()
                        #==================
                        # reading data map
                        #==================
    @classmethod
    def readResponse(cls):
        """
            reading card data
        """
        return cls.STATUS.map_status

                        #==================
                        # writing data map
                        #==================
    @classmethod
    def address_map(cls, address):
        """
            write map address data
        """
        cls.STATUS.map_status["address"] = address

    @classmethod
    def history_map(cls, history):
        """
            write map history data
        """
        cls.STATUS.map_status["history"] = history

if __name__ == "__main__":
    pass
