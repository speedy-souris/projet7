#coding:utf-8
#!/usr/bin/env python

import requests

from ..wikimediaapi import ApiWikiMedia


class TestParamsImport:
    """
        configuration of imported modules
    """
    def __init__(self):
        self.api_wiki = ApiWikiMedia()

PARAMS = TestParamsImport()
WIKIMEDIA = PARAMS.api_wiki

def get_mockreturn(result):
    def mock_get(url, params):
        """
            Mock function on api object
        """
        class JsonResponse:
            @staticmethod
            def json():
                return result
        return JsonResponse()
    return mock_get

class TestApiWikiMedia:
    """
        management of APi parameters test 
    """
    def test_search_wiki(self, monkeypatch):
        """
            A.P.I wikipedia test function (wikimedia) that returns a file
            Json containing the history of the requested address
        """
        demand = WIKIMEDIA.get_page_url('OpenClassrooms')
        result_history = {
            'batchcomplete': True,
            'query': {
                'pages': [
                    {
                        'pageid': 4338589,
                        'ns': 0,
                        'title': 'OpenClassrooms',
                        'extract': f'OpenClassrooms est un site web de formation '\
                                   f'en ligne qui propose à ses membres des cours '\
                                   f'certifiants et des parcours débouchant sur '\
                                   f'des métiers en croissance. Ses contenus sont '\
                                   f'réalisés en interne, par des écoles, des '\
                                   f'universités, des entreprises partenaires '\
                                   f'comme Microsoft ou IBM, ou historiquement '\
                                   f"par des bénévoles. Jusqu'en 2018, n'importe "\
                                   f'quel membre du site pouvait être auteur, via '\
                                   f'un outil nommé « interface de rédaction » '\
                                   f'puis « Course Lab ». De nombreux cours sont '\
                                   f'issus de la communauté, mais ne sont plus '\
                                   f'mis en avant. Initialement orientée autour '\
                                   f'de la programmation informatique, la '\
                                   f'plate-forme couvre depuis 2013 des '\
                                   f'thématiques plus larges tels que le '\
                                   f"marketing, l'entrepreneuriat et les "\
                                   f'sciences.'
                    }
                ]
            }
        }
        mockreturn = get_mockreturn('result_history')
        monkeypatch.setattr(requests, 'get', mockreturn)
        assert demand == result_history

