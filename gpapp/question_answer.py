#coding:utf-8
#!/usr/bin/env python

import time
import json
import urllib.request, urllib.parse
from . import devSetting
# ~ from .devSetting.dataInitial import InitData as config
from .devSetting.dataRedis import Conversation
# ~ from .devSetting.dataDefault import DefaultData as default
from .devSetting import fDev as func


# ~ class ApiParams:
    # ~ """
        # ~ management of APi parameters
    # ~ """

class Behaviour:
    """
        user behavior management
            - civility ==> user courtesy
            - decency ==> rude user
            - comprehension ==> inconsistency of user comments
            - quotas ==> user session end setting

    """
    def attribute_analysis(self):
        """
            attribute analysis
                - civility
                - decency
                - comprehension
        """
        self.civlity = Conversation.read_civility
        self.decency = Conversation.read_decency
        self.comprehension = Conversation.read_comprehension

    # ~ @property
    # ~ def t_decency(self):
        # ~ return setting().writeDecency(True)

    # ~ @property
    # ~ def f_decency(self):
        # ~ return setting().writeDecency(False)

    # ~ @property
    # ~ def r_decency(self):
        # ~ return setting().readDecency()

    # ~ @property
    # ~ def t_civility(self):
        # ~ return setting().writeCivility(True)

    # ~ @property
    # ~ def f_civility(self):
        # ~ return setting().writeCivility(False)

    # ~ @property
    # ~ def r_civility(self):
        # ~ return setting().readCivility()

    # ~ @property
    # ~ def t_comprehension(self):
        # ~ return setting().writeComprehension(True)

    # ~ @property
    # ~ def f_comprehension(self):
        # ~ return setting().writeComprehension(False)

    # ~ @property
    # ~ def r_comprehension(self):
        # ~ return setting().readComprehension()

    # ~ @property
    # ~ def t_quotas(self):
        # ~ return setting().writeQuotas(True)

    # ~ @property
    # ~ def f_quotas(self):
        # ~ return setting().writeQuotas(False)

    # ~ @property
    # ~ def r_quotas(self):
        # ~ return setting().readQuotas()

# ~ class Politeness:
    # ~ """

    # ~ """
    # ~ #===========================
    # ~ # Initialization wickedness
    # ~ #===========================
    # ~ def wickedness(self, question):
        # ~ """
            # ~ Disrespect management function
            # ~ initialization of wickedness
                # ~ - decency
         # ~ """
        # ~ Behaviour().t_decency
        # ~ if question.lower() in config().constant["list_indecency"]:
            # ~ Behaviour().f_decency
        # ~ return Behaviour().r_decency
    # ~ #=========================
    # ~ # Initialization Civility
    # ~ #=========================
    # ~ def civility(self, question):
        # ~ """
            # ~ Incivility management function
            # ~ initialization of incivility
                # ~ - civility
        # ~ """
        # ~ Behaviour().t_decency
        # ~ setting.writeComprehension(True)
        # ~ if question.lower() in config().constant["list_civility"]:
            # ~ Behaviour().t_civility
        # ~ return Behaviour().r_civility

    # ~ #==============================
    # ~ # Initialization comprehension
    # ~ #==============================
    # ~ def comprehension(self, question):
        # ~ """
            # ~ Incomprehension management function
            # ~ initialization of incomprehension
                # ~ - comprehension
        # ~ """
        # ~ try:
            # ~ func.map_coordinates(question)
        # ~ except IndexError:
            # ~ Behaviour().f_comprehension
            # ~ return setting().COMPREHENSION
        # ~ Behaviour().t_comprehension
        # ~ return Behaviour().r_comprehension

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
        setting().incrementCounter()

        return Behaviour().r_quotas

    #==========================================
    # Initialization session by API parameters
    #==========================================
    # ~ def api_session(self, question, apiParams=False):
        # ~ """
            # ~ Session management function
            # ~ initialization of session
                # ~ - quotas_api
        # ~ """
        # ~ if apiParams:
            # ~ Behaviour().t_quotas

        # ~ try:
            # ~ func.map_coordinates(question)
        # ~ except (TypeError,KeyError):
            # ~ Behaviour().t_quotas

        # ~ return Behaviour().r_quotas

class Response:
    """
        Management class
        for initializing configuration response Grandpy
    """
    API = ApiParams()
    BEHAVIOUR = Behaviour()
    POLITENESS = Politeness()
    SESSION = Session()

    def parsing(self,question=default().data_test["question"]):
        """
            parse the question to grandpy
        """
        return Response.API.parser(qestion=default().data_test["question"])

    @property
    def id_list(self):
        """
            determine the internal API identifier
            for each address requested
        """
        return Response.API.get_place_id_list(
            address=default().data_test["addressPlace"]
        )

    @property
    def address(self):
        """
            show address coordinates
        """
        return Response.API.get_address(
            place_id=default().data_test["placeId"]
        )

    @property
    def history(self):
        """
            view wikipedia history
        """
        return Response.API.get_history(
            search_history=default().data_test["search"]
        )

    def map_static(self):
        """
            show the coordinates on the map
        """
        self.location = map["address"]
        return Response.API.get_get_map_static(self, self.location)

if __name__ == "__main__":
    pass
