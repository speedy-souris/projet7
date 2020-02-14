#coding:utf-8
#!/usr/bin/env python

class DefaultData:
    """
        management of default API parameters
            - PLACEID......
            - QUESTION.....
            - ADDRESSPLACE. ==> dict()
            - SEARCH.......
    """
    PLACEID = "ChIJTei4rhlu5kcRPivTUjAg1RU"
    QUESTION = "ou se trouve la poste de marseille"
    ADDRESSPLACE = "paris poste"
    SEARCH = "montmartre"

    def __init__(self):
        """
            constructor to initialize default variable
        """
        self.data = {}

    @property
    def data_test(self):
        """
            Initialization of API parameters by default for tests
        """
        self.data["placeId"] = DefaultData.PLACEID
        self.data["question"] = DefaultData.QUESTION
        self.data["addressPlace"] = DefaultData.ADDRESSPLACE
        self.data["search"] = DefaultData.SEARCH

        return self.data


if __name__ == "__main__":
    pass
