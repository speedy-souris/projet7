#coding:utf-8
#!/usr/bin/env python

class ParamsTest:
    """
        management of API parameters default settings for testing
    """
    DEMAND = "ou est situé le restaurant la_nappe_d_or de lyon"
    PARSED = [
        "restaurant","la_nappe_d_or","lyon"
    ]
    GEOPLACEID = {
        'candidates': [{
            'place_id': "ChIJTei4rhlu5kcRPivTUjAg1RU"
        }]
    }
    ADDRESS = {
        'result': {
            'formatted_address': "16 Rue Étienne Marcel, 75002 Paris, France"
        }
    }
    HISTORY = [
        [
            """Riche d'un long passé artistique, ce secteur de Paris (France)
            dominé par la Basilique du Sacré-Cœur a toujours été le symbole
            d'un mode de vie bohème où, de Picasso à Modigliani, de nombreux
            artistes trouvèrent refuge."""
        ]
    ]
    def __init__(self):
        """
            initialization constructor for test data
        """
        self.data = {}

    @property
    def testing(self):
        """
            Initialization of API parameters by default for tests
        """
        self.data["demand"] = ParamsTest.DEMAND

        self.data["parsed"] = ParamsTest.PARSED
        self.data["geoPlaceId"] = ParamsTest.GEOPLACEID
        self.data["address"] = ParamsTest.ADDRESS
        self.data["history"] = ParamsTest.HISTORY

        return self.data

if __name__ == "__main__":
    pass
