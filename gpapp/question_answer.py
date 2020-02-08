#coding:utf-8
#!/usr/bin/env python

import time
import json
import urllib.request, urllib.parse
from .classSetting.dataInitial import Parameter as config
from .classSetting.dataRedis import DataRedis as setting
from .classSetting.dataDefault import Parameter as default
from .funcDev import fDev as func


class ApiParams:
    """
        management of APi parameters
    """
    DATA = default.data_test()
    CONSTANT = config.constant()
    STATUS = config.status_env()
    #========
    # parser
    #========
    @classmethod
    def parser(cls, question=DATA["question"]):
        """
            function that cuts the string of characters (question asked to GrandPy)
            into a word list then delete all unnecessary words to keep only
            the keywords for the search
        """

        # list of words to remove in questions
        list_question = question.split()
        result = [
            w for w in list_question if w.lower() not in cls.ApiParams.CONSTANT[
                "list_unnecessary"
            ]
        ]

        return result

    #===================================
    # place_id search on Google Map API
    #===================================
    @classmethod
    def get_place_id_list(cls, address=DATA["addressPlace"]):
        """
            Google map API place_id search function
        """
        key = cls.ApiParams.STATUS["map"] # environment variable
        # replacing space by "% 20" in the string of characters
        address_encode = urllib.parse.quote(address)

        place_id = urllib.request.urlopen(
            "https://maps.googleapis.com/maps/api/place/findplacefromtext/"\
            +f"json?input={address_encode}&inputtype=textquery&key={key}"
        )

        result = json.loads(place_id.read().decode("utf8"))

        return result

    #===========================
    # address on Google Map API
    #===========================
    @classmethod
    def get_address(cls, place_id=DATA["placeId"]):
        """
            Google map API address search with place_id function
        """
        key = cls.ApiParams.STATUS["map"] # environment variable
        address_found= urllib.request.urlopen(
            "https://maps.googleapis.com/maps/api/place/details/"\
            f"json?placeid={place_id}&fields=formatted_address,geometry&key={key}"
        )

        result = json.loads(address_found.read().decode("utf8"))

        return result

    #=================================
    # history search on wikimedia API
    #=================================
    def get_history(self, search_history=DATA["search"]):
        """
            wikipedia API (Wikimedia) history search
        """

        # replacing space by "% 20" in the string of characters
        history_encode = urllib.parse.quote(search_history)

        history_found = urllib.request.urlopen(
            "https://fr.wikipedia.org/w/api.php?action=opensearch&search="\
            f"{history_encode}&format=json"
        )

        result = json.loads(history_found.read().decode("utf8"))
        return result

    #=========================================
    # map display in the Google Map Satic API
    #=========================================
    @classmethod
    def get_map_static(cls, location_map):
        """
            function of displaying the geolocation of the address
            asked to grandpy on the map of the Google Map Static API
        """
        key = cls.ApiParams.STATUS["staticMap"]  # environment variable

        # replacing space by "% 20" in the string of characters
        formatting_address = urllib.parse.quote(location_map["address"])
        # longitude and latitude display
        localization = location_map["location"]
        # display map
        display_map = "https://maps.googleapis.com/maps/api/staticmap?center="\
            +formatting_address+\
            "&zoom=18.5&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C"\
            +str(localization['lat'])+","+str(localization['lng'])+f"&key={key}"
        return display_map

class Behaviour:
    """
        user behavior management
            - civility ==> user courtesy
            - decency ==> rude user
            - comprehension ==> inconsistency of user comments
            - quotas ==> user session end setting

    """
    @property
    def t_decency(self):
        return setting.writeDecency(True)

    @property
    def f_decency(self):
        return setting.writeDecency(False)

    @property
    def r_decency(self):
        return setting.readDecency()

    @property
    def t_civility(self):
        return setting.writeCivility(True)

    @property
    def f_civility(self):
        return setting.writeCivility(False)

    @property
    def r_civility(self):
        return setting.readCivility()

    @property
    def t_comprehension(self):
        return setting.writeComprehension(True)

    @property
    def f_comprehension(self):
        return setting.writeComprehension(False)

    @property
    def r_comprehension(self):
        return setting.readComprehension()

    @property
    def t_quotas(self):
        return setting.writeQuotas(True)

    @property
    def f_quotas(self):
        return setting.writeQuotas(False)

    @property
    def r_quotas(self):
        return setting.readQuotas()

    #===========================
    # Initialization wickedness
    #===========================
    def wickedness(self, question):
        """
            Disrespect management function
            initialization of wickedness
                - decency
         """
        self.Behaviour.t_decency
        if question.lower() in self.ApiParams.CONSTANT["list_indecency"]:
            self.Behaviour.f_decency
        return self.Behaviour.r_decency
    #=========================
    # Initialization Civility
    #=========================
    def civility(self, question):
        """
            Incivility management function
            initialization of incivility
                - civility
        """
        self.Behaviour.t_decency
        # ~ setting.writeComprehension(True)
        if question.lower() in self.ApiParams.CONSTANT["list_civility"]:
            self.Behaviour.t_civility
        return self.Behaviour.r_civility

    #==============================
    # Initialization comprehension
    #==============================
    def comprehension(self, question):
        """
            Incomprehension management function
            initialization of incomprehension
                - comprehension
        """
        try:
            func.map_coordinates(question)
        except IndexError:
            self.Behaviour.f_comprehension
            return self.Behaviour.COMPREHENSION
        self.Behaviour.t_comprehension
        return self.Behaviour.r_comprehension

    #===================================
    # Initialization session by counter
    #===================================
    def counter_session(self, question, counter):
        """
            Session management function
            initialization of session
                - nb_request
                - quotas_api
        """
        if counter >= 10:
            self.Behaviour.t_quotas
        setting.incrementCounter()

        return self.Behaviour.r_quotas

    #==========================================
    # Initialization session by API parameters
    #==========================================
    def api_session(self, question, apiParams=False):
        """
            Session management function
            initialization of session
                - quotas_api
        """
        if apiParams:
            self.Behaviour.t_quotas

        try:
            func.map_coordinates(question)
        except (TypeError,KeyError):
            self.Behaviour.t_quotas

        return self.Behaviour.r_quotas

if __name__ == "__main__":
    pass
