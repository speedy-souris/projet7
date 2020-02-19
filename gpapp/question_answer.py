#coding:utf-8
#!/usr/bin/env python

import time
import json
import urllib.request, urllib.parse
from .devSetting import dataInitial as config
from .devSetting import dataRedis as setting
from .devSetting import dataDefault as default
from .devSetting import fDev as func


class ApiParams:
    """
        management of APi parameters
    """
    #========
    # parser
    #========
    def parser(self, question=default.DefaultData().data_test["question"]):
        """
            function that cuts the string of characters (question asked to GrandPy)
            into a word list then delete all unnecessary words to keep only
            the keywords for the search
        """

        # list of words to remove in questions
        list_question = question.split()
        result = [
            w for w in list_question if w.lower() not in config.InitData().constant[
                "list_unnecessary"
            ]
        ]

        return result

    #===================================
    # place_id search on Google Map API
    #===================================
    def get_place_id_list(self, address):
        """
            Google map API place_id search function
        """
        key = ApiParams.DATA.status_env["map"] # environment variable
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
    def get_address(self, place_id):
        """
            Google map API address search with place_id function
        """
        key = ApiParams.DATA.status_env["map"] # environment variable
        address_found= urllib.request.urlopen(
            "https://maps.googleapis.com/maps/api/place/details/"\
            f"json?placeid={place_id}&fields=formatted_address,geometry&key={key}"
        )

        result = json.loads(address_found.read().decode("utf8"))

        return result

    #=================================
    # history search on wikimedia API
    #=================================
    def get_history(self, search_history):
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
    def get_map_static(self, location_map):
        """
            function of displaying the geolocation of the address
            asked to grandpy on the map of the Google Map Static API
        """
        key = ApiParams.DATA.status_env["staticMap"]  # environment variable

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
        return setting.DataRedis().writeDecency(True)

    @property
    def f_decency(self):
        return setting.DataRedis().writeDecency(False)

    @property
    def r_decency(self):
        return setting.DataRedis().readDecency()

    @property
    def t_civility(self):
        return setting.DataRedis().writeCivility(True)

    @property
    def f_civility(self):
        return setting.DataRedis().writeCivility(False)

    @property
    def r_civility(self):
        return setting.DataRedis().readCivility()

    @property
    def t_comprehension(self):
        return setting.DataRedis().writeComprehension(True)

    @property
    def f_comprehension(self):
        return setting.DataRedis().writeComprehension(False)

    @property
    def r_comprehension(self):
        return setting.DataRedis().readComprehension()

    @property
    def t_quotas(self):
        return setting.DataRedis().writeQuotas(True)

    @property
    def f_quotas(self):
        return setting.DataRedis().writeQuotas(False)

    @property
    def r_quotas(self):
        return setting.DataRedis().readQuotas()

class Politeness:
    """

    """
    #===========================
    # Initialization wickedness
    #===========================
    def wickedness(self, question):
        """
            Disrespect management function
            initialization of wickedness
                - decency
         """
        Behaviour().t_decency
        if question.lower() in config.InitData().constant["list_indecency"]:
            Behaviour().f_decency
        return Behaviour().r_decency
    #=========================
    # Initialization Civility
    #=========================
    def civility(self, question):
        """
            Incivility management function
            initialization of incivility
                - civility
        """
        Behaviour().t_decency
        # ~ setting.writeComprehension(True)
        if question.lower() in config.InitData().constant["list_civility"]:
            Behaviour().t_civility
        return Behaviour().r_civility

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
            Behaviour().f_comprehension
            return setting.DataRedis().COMPREHENSION
        Behaviour().t_comprehension
        return Behaviour().r_comprehension

class Session:
    """
        management of session parameters
    """
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
            Behaviour().t_quotas
        setting.DataRedis().incrementCounter()

        return Behaviour().r_quotas

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
            Behaviour.t_quotas

        try:
            func.map_coordinates(question)
        except (TypeError,KeyError):
            Behaviour().t_quotas

        return Behaviour().r_quotas

class Response:
    """
        Management class
        for initializing configuration response Grandpy
    """
    API = ApiParams()
    BEHAVIOUR = Behaviour()
    POLITENESS = Politeness()
    SESSION = Session()

    def parsing(self,question=default.DefaultData().data_test["question"]):
        """
            parse the question to grandpy
        """
        return Response.API.parser(qestion=default.DefaultData().data_test["question"])

    @property
    def id_list(self):
        """
            determine the internal API identifier
            for each address requested
        """
        return Response.API.get_place_id_list(
            address=default.DefaultData().data_test["addressPlace"]
        )

    @property
    def address(self):
        """
            show address coordinates
        """
        return Response.API.get_address(
            place_id=default.DefaultData().data_test["placeId"]
        )

    @property
    def history(self):
        """
            view wikipedia history
        """
        return Response.API.get_history(
            search_history=default.DefaultData().data_test["search"]
        )

    def map_static(self):
        """
            show the coordinates on the map
        """
        self.location = map["address"]
        return Response.API.get_get_map_static(self, self.location)

if __name__ == "__main__":
    pass
