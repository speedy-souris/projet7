#coding:utf-8
#!/usr/bin/env python

class ParamsDefault:
    """
        management of API parameters
    """
    def __init__(self):
        """
            constructor to initialize default variables
        """
        self.data = {}
        self.placeId = "ChIJTei4rhlu5kcRPivTUjAg1RU"
        self.question = "ou se trouve la poste de marseille"
        self.addressPlace = "paris poste"
        self.search = "montmartre"

class Params:
    """
        API default settings for testing
    """
    DEFAULT = ParamsDefault()

    @classmethod
    def data_test(cls):
        """
            Initialization of API parameters by default for tests
        """
        cls.DEFAULT.data["placeId"] = cls.DEFAULT.placeId
        cls.DEFAULT.data["question"] = cls.DEFAULT.question
        cls.DEFAULT.data["addressPlace"] = cls.DEFAULT.addressPlace
        cls.DEFAULT.data["search"] = cls.DEFAULT.search

        return cls.DEFAULT.data
