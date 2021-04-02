#coding:utf-8
#!/usr/bin/env python
"""
    wikimedia API test module
"""
import requests
from ..wikimediaapi import WikiMediaAddressProcessing, ApiResultComparison


def get_mockreturn(result):
    """
        mock template call
    """
    def mock_get(url, params):
        """
            Mock function on api object
        """
        class JsonResponse:
            """
                mock result in JSON format
            """
            @staticmethod
            def json():
                """
                    Json method
                """
                return result
        return JsonResponse()
    return mock_get

class TestApiWikiMedia:
    """
        management of APi parameters test 
    """
    def setup_method(self):
        self.wikimedia_value1 = WikiMediaAddressProcessing(48.8975156, 2.3833993)
        self.wikimedia_value2 = WikiMediaAddressProcessing(0, 0)

    def test_search_wiki_page(self, monkeypatch):
        """
            A.P.I wikipedia test function (wikimedia) that returns a file
            Json containing the history of the requested address
        """
        demand1 = self.wikimedia_value1.get_from_pages_api()
        demand2 = self.wikimedia_value2.get_from_pages_api()
        result_history1 = {
            'batchcomplete': '',
            'query': {
                'geosearch': [
                    {
                        'pageid': 3120649, 'ns': 0, 'title': 'Quai de la Gironde',
                        'lat': 48.8965, 'lon': 2.383164, 'dist': 114.2, 'primary': ''
                    },
                    {
                        'pageid': 11988883, 'ns': 0, 'title': 'Parc du Pont de Flandre',
                        'lat': 48.89694, 'lon': 2.38194, 'dist': 124.4, 'primary': ''
                    },
                    {
                        'pageid': 3124793, 'ns': 0, 'title': 'Square du Quai-de-la-Gironde',
                        'lat': 48.896194, 'lon': 2.383181, 'dist': 147.8, 'primary': ''
                    },
                    {
                        'pageid': 271433, 'ns': 0, 'title': 'Avenue Corentin-Cariou',
                        'lat': 48.896169, 'lon': 2.384151, 'dist': 159.5, 'primary': ''
                    },
                    {
                        'pageid': 512073, 'ns': 0, 'title': 'Porte de la Villette (métro de Paris)',
                        'lat': 48.897089223548, 'lon': 2.3858758807182, 'dist': 187.1, 'primary': ''
                    },
                    {
                        'pageid': 3120618, 'ns': 0, 'title': 'Quai de la Charente',
                        'lat': 48.895636, 'lon': 2.384586, 'dist': 226.3, 'primary': ''
                    },
                    {
                        'pageid': 2960707, 'ns': 0, 'title': 'Porte de la Villette',
                        'lat': 48.898388, 'lon': 2.386341, 'dist': 235.9, 'primary': ''
                    },
                    {
                        'pageid': 5422631, 'ns': 0, 'title': 'Rue Benjamin-Constant',
                        'lat': 48.895467, 'lon': 2.382145, 'dist': 245.6, 'primary': ''
                    },
                    {
                        'pageid': 3120923, 'ns': 0, 'title': 'Quai du Lot',
                        'lat': 48.899357, 'lon': 2.381539, 'dist': 245.8, 'primary': ''
                    },
                    {
                        'pageid': 7065484, 'ns': 0, 'title': 'Gare du pont de Flandre',
                        'lat': 48.8954, 'lon': 2.3815, 'dist': 273.2, 'primary': ''
                    }
                ]
            }
        }
        result_history2 = {
            'batchcomplete': '',
            'query': {
                'geosearch': [
                    {
                        'pageid': 9999656, 'ns': 0, 'title': 'Bouée Soul',
                        'lat': 0, 'lon': 0, 'dist': 0, 'primary': ''
                    },
                    {
                        'pageid': 8738584, 'ns': 0, 'title': 'Null Island',
                        'lat': 0, 'lon': 0, 'dist': 0, 'primary': ''
                    }
                ]
            }
        }
        mockreturn = get_mockreturn('result_history1')
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert demand1 == result_history1

        mockreturn = get_mockreturn('result_history2')
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert demand2 == result_history2

    def test_wiki_page_content(self, monkeypatch):
        """
            A.P.I wikipedia (wikimedia) test function that returns a file
              Json containing the content of the requested page
        """
        demand1 = self.wikimedia_value1.get_from_address_list_creation()
        demand2 = self.wikimedia_value2.get_from_address_list_creation()
        result_content1 = [
            ['Quai', 'de', 'la', 'Gironde'],
            ['Parc', 'du', 'Pont', 'de', 'Flandre'],
            ['Square', 'du', 'Quai-de-la-Gironde'],
            ['Avenue', 'Corentin-Cariou'],
            ['Porte', 'de', 'la', 'Villette', '(métro', 'de', 'Paris)'],
            ['Quai', 'de', 'la', 'Charente'],
            ['Porte', 'de', 'la', 'Villette'],
            ['Rue', 'Benjamin-Constant'],
            ['Quai', 'du', 'Lot'],
            ['Gare', 'du', 'pont', 'de', 'Flandre']
        ]
        result_content2 = [
            ['Bouée', 'Soul'], ['Null', 'Island']
        ]

        mockreturn = get_mockreturn('result_content1')
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert demand1 == result_content1

        mockreturn = get_mockreturn('result_content2')
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert demand2 == result_content2

class TestApiComparison:
    """
        management of APi comparison test 
    """
    def setup_method(self):
        self.address = '10 Quai de la Charente, 75019 Paris, France'
        self.list_address_page = [
            ['Quai', 'de', 'la', 'Gironde'],
            ['Parc', 'du', 'Pont', 'de', 'Flandre'],
            ['Square', 'du', 'Quai-de-la-Gironde'],
            ['Avenue', 'Corentin-Cariou'],
            ['Porte', 'de', 'la', 'Villette', '(métro', 'de', 'Paris)'],
            ['Quai', 'de', 'la', 'Charente'],
            ['Porte', 'de', 'la', 'Villette'],
            ['Rue', 'Benjamin-Constant'],
            ['Quai', 'du', 'Lot'],
            ['Gare', 'du', 'pont', 'de', 'Flandre']
        ]
        self.api_comparison =\
            ApiResultComparison(self.address, self.list_address_page)

    def test_address_conversion(self):
        """
            conversion of the address found by the google Maps API
        """
        self.api_comparison.get_from_list_address_convertion()
        result_conversion =\
            ['10', 'quai', 'de', 'la', 'charente', '75019', 'paris', 'france']
        assert result_conversion

    def test_common_string(self):
        """
            found the string common
            to the Google Maps API and the wikimedia API
        """
        demand = self.api_comparison.get_from_common_string_creation().lower()
        result_common_string = 'quai de la charente'
        assert demand == result_common_string
