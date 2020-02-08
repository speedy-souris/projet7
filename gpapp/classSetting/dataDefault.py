#coding:utf-8
#!/usr/bin/env python

class Parameter:
    """
        management of default API parameters
            - PLACEID
            - QUESTION
            - ADDRESSPLACE
            - SEARCH
    """
    PLACEID = "ChIJTei4rhlu5kcRPivTUjAg1RU"
    QUESTION = "ou se trouve la poste de marseille"
    ADDRESSPLACE = "paris poste"
    SEARCH = "montmartre"

    def __init__(self):
        """
            constructor to initialize default variable
                - data
        """
        self.data = {}

    def data_test(self):
        """
            Initialization of API parameters by default for tests
        """
        self.data["placeId"] = Parameter.PLACEID
        self.data["question"] = Parameter.QUESTION
        self.data["addressPlace"] = Parameter.ADDRESSPLACE
        self.data["search"] = Parameter.SEARCH

        return self.data
