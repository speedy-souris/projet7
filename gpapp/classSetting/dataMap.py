#coding:utf-8
#!/usr/bin/env python

#============================
# Initialization Map Status
#============================

class DataMap:
    """
        management class for geographic coordinates of the map and
        the address history in wikipedia
        initialization of the default settings
        for displaying the map (grandpy response)
            - map_status
    """
    def __init__(self):
        """
            constructeur of initialization data map
        """
        self.map_status = {}
                        #==================
                        # reading data map
                        #==================
    @property
    def readResponse(self):
        """
            reading card data
        """
        return self.map_status

                        #==================
                        # writing data map
                        #==================
    def address_map(self, address):
        """
            write map address data
        """
        self.map_status["address"] = address

    def history_map(self, history):
        """
            write map history data
        """
        self.map_status["history"] = history

if __name__ == "__main__":
    pass
