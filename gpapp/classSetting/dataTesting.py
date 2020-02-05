#coding:utf-8
#!/usr/bin/env python

class TestingConf:
    """
        management of API parameters
    """
    def __init__(self):
        """
            initialization constructor for test data
        """
        self.data = {}
        self.demand = "ou est situé le restaurant la_nappe_d_or de lyon"
        self.parsed = [
            "restaurant","la_nappe_d_or","lyon"
        ]
        self.geoPlaceId = {
            'candidates': [{
                'place_id': "ChIJTei4rhlu5kcRPivTUjAg1RU"
            }]
        }
        self.address = {
            'result': {
                'formatted_address': "16 Rue Étienne Marcel, 75002 Paris, France"
            }
        }
        self.history = [
            [
                """Riche d'un long passé artistique, ce secteur de Paris (France)
                dominé par la Basilique du Sacré-Cœur a toujours été le symbole
                d'un mode de vie bohème où, de Picasso à Modigliani, de nombreux
                artistes trouvèrent refuge."""
            ]
        ]

class ParamsTest:
    """
        API default settings for testing
    """
    TESTING = TestingConf()

    @classmethod
    def testing(cls):
        """
            Initialization of API parameters by default for tests
        """
        cls.TESTING.data["demand"] = cls.TESTING.demand

        cls.TESTING.data["parsed"] = cls.TESTING.parsed
        cls.TESTING.data["geoPlaceId"] = cls.TESTING.geoPlaceId
        cls.TESTING.data["address"] = cls.TESTING.address
        cls.TESTING.data["history"] = cls.TESTING.history

        return cls.TESTING.data
