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
                        # writing data map
                        #==================
    def data_map(self, address, history):
        """
            write map address data / history data
        """
        self.map_status["address"] = address
        self.map_status["history"] = history

        return self.map_status


if __name__ == "__main__":
    pass

