#coding:utf-8
#!/usr/bin/env python

# ~ import requests

# ~ from ..wikimediaapi import ApiWikiMedia


# ~ class TestParamsImport:
    # ~ """
        # ~ configuration of imported modules
    # ~ """
    # ~ def __init__(self):
        # ~ self.api_wiki = ApiWikiMedia()

# ~ PARAMS = TestParamsImport()
# ~ WIKIMEDIA = PARAMS.api_wiki

# ~ def get_mockreturn(result):
    # ~ def mock_get(url, params):
        # ~ """
            # ~ Mock function on api object
        # ~ """
        # ~ class JsonResponse:
            # ~ @staticmethod
            # ~ def json():
                # ~ return result
        # ~ return JsonResponse()
    # ~ return mock_get

# ~ class TestApiWikiMedia:
    # ~ """
        # ~ management of APi parameters test 
    # ~ """
    # ~ def test_search_wiki_page(self, monkeypatch):
        # ~ """
            # ~ A.P.I wikipedia test function (wikimedia) that returns a file
            # ~ Json containing the history of the requested address
        # ~ """
        # ~ demand = WIKIMEDIA.get_from_page_url_api('OpenClassrooms')
        # ~ demand2 = WIKIMEDIA.get_from_page_url_api('openClassRooms')
        # ~ result_history = {
            # ~ "batchcomplete": True,
            # ~ 'query': {
                # ~ 'pages': [
                    # ~ {
                        # ~ "pageid": 4338589,
                        # ~ "ns": 0,
                        # ~ "title": "OpenClassrooms",
                        # ~ 'extract': f'OpenClassrooms est un site web de formation '\
                                   # ~ f'en ligne qui propose à ses membres des cours '\
                                   # ~ f'certifiants et des parcours débouchant sur '\
                                   # ~ f'des métiers en croissance. Ses contenus sont '\
                                   # ~ f'réalisés en interne, par des écoles, des '\
                                   # ~ f'universités, des entreprises partenaires '\
                                   # ~ f'comme Microsoft ou IBM, ou historiquement '\
                                   # ~ f"par des bénévoles. Jusqu'en 2018, n'importe "\
                                   # ~ f'quel membre du site pouvait être auteur, via '\
                                   # ~ f'un outil nommé « interface de rédaction » '\
                                   # ~ f'puis « Course Lab ». De nombreux cours sont '\
                                   # ~ f'issus de la communauté, mais ne sont plus '\
                                   # ~ f'mis en avant. Initialement orientée autour '\
                                   # ~ f'de la programmation informatique, la '\
                                   # ~ f'plate-forme couvre depuis 2013 des '\
                                   # ~ f'thématiques plus larges tels que le '\
                                   # ~ f"marketing, l'entrepreneuriat et les "\
                                   # ~ f'sciences.'
                    # ~ }
                # ~ ]
            # ~ }
        # ~ }
        # ~ result_history2 = {
            # ~ 'query': {
                # ~ 'pages': [
                    # ~ {
                        # ~ 'missing': True
                    # ~ }
                # ~ ]
            # ~ }
        # ~ }
        # ~ mockreturn = get_mockreturn('result_history')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand == result_history

        # ~ mockreturn = get_mockreturn('result_history2')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand2 == result_history2

    # ~ def test_contained_wikipage_search(self, monkeypatch):
        # ~ """
            # ~ A.P.I wikipedia (wikimedia) test function that returns a file
              # ~ Json containing the content of the requested page
        # ~ """
        # ~ latitude, longitude = 48.8975156, 2.3833993
        # ~ demand = WIKIMEDIA.get_from_address_url_api(latitude, longitude)
        # ~ demand2 = WIKIMEDIA.get_from_address_url_api(0,0)

        # ~ result_content = {
            # ~ 'batchcomplete': '',
            # ~ 'query': {
                # ~ 'geosearch': [
                    # ~ {
                        # ~ "pageid": 3120649,
                        # ~ "ns": 0,
                        # ~ "title": "Quai de la Gironde",
                        # ~ "lat": 48.8965,
                        # ~ "lon": 2.383164,
                        # ~ "dist": 114.2,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 11988883,
                        # ~ "ns": 0,
                        # ~ "title": "Parc du Pont de Flandre",
                        # ~ "lat": 48.89694,
                        # ~ "lon": 2.38194,
                        # ~ "dist": 124.4,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 3124793,
                        # ~ "ns": 0,
                        # ~ "title": "Square du Quai-de-la-Gironde",
                        # ~ "lat": 48.896194,
                        # ~ "lon": 2.383181,
                        # ~ "dist": 147.8,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 271433,
                        # ~ "ns": 0,
                        # ~ "title": "Avenue Corentin-Cariou",
                        # ~ "lat": 48.896169,
                        # ~ "lon": 2.384151,
                        # ~ "dist": 159.5,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 512073,
                        # ~ "ns": 0,
                        # ~ "title": "Porte de la Villette (métro de Paris)",
                        # ~ "lat": 48.897089223548,
                        # ~ "lon": 2.3858758807182,
                        # ~ "dist": 187.1,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 3120618,
                        # ~ "ns": 0,
                        # ~ "title": "Quai de la Charente",
                        # ~ "lat": 48.895636,
                        # ~ "lon": 2.384586,
                        # ~ "dist": 226.3,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 2960707,
                        # ~ "ns": 0,
                        # ~ "title": "Porte de la Villette",
                        # ~ "lat": 48.898388,
                        # ~ "lon": 2.386341,
                        # ~ "dist": 235.9,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 5422631,
                        # ~ "ns": 0,
                        # ~ "title": "Rue Benjamin-Constant",
                        # ~ "lat": 48.895467,
                        # ~ "lon": 2.382145,
                        # ~ "dist": 245.6,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 3120923,
                        # ~ "ns": 0,
                        # ~ "title": "Quai du Lot",
                        # ~ "lat": 48.899357,
                        # ~ "lon": 2.381539,
                        # ~ "dist": 245.8,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 7065484,
                        # ~ "ns": 0,
                        # ~ "title": "Gare du pont de Flandre",
                        # ~ "lat": 48.8954,
                        # ~ "lon": 2.3815,
                        # ~ "dist": 273.2,
                        # ~ "primary": ""
                    # ~ }
                # ~ ]
            # ~ }
        # ~ }
        # ~ result_content2 = {
            # ~ "batchcomplete": "",
            # ~ "query": {
                # ~ "geosearch": [
                    # ~ {
                        # ~ "pageid": 9999656,
                        # ~ "ns": 0,
                        # ~ "title": "Bouée Soul",
                        # ~ "lat": 0,
                        # ~ "lon": 0,
                        # ~ "dist": 0,
                        # ~ "primary": ""
                    # ~ },
                    # ~ {
                        # ~ "pageid": 8738584,
                        # ~ "ns": 0,
                        # ~ "title": "Null Island",
                        # ~ "lat": 0,
                        # ~ "lon": 0,
                        # ~ "dist": 0,
                        # ~ "primary": ""
                    # ~ }
                # ~ ]
            # ~ }
        # ~ }
        # ~ mockreturn = get_mockreturn('result_content')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand == result_content

        # ~ mockreturn = get_mockreturn('result_content2')
        # ~ monkeypatch.setattr(requests, 'get', mockreturn)
        # ~ assert demand2 == result_content2
