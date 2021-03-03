#coding:utf-8
#!/usr/bin/env python

import urllib.request
from io import BytesIO
import json
from .. import wikimediaapi




def mock(result):
    def mockreturn(request):
        """
            Mock function on api object
        """
        return BytesIO(json.dumps(result).encode())
    return mockreturn
 
class TestApiWikiMedia:
    """
        management of APi parameters test 
    """
    def test_search_wiki(self, monkeypatch):
        """
            A.P.I wikipedia test function (wikimedia) that returns a file
            Json containing the history of the requested address
        """
        demand = wikimediaapi.get_history('openClassRooms')
        result_history = [
            [
                """
                OpenClassrooms est un site web de formation en ligne
                qui propose à ses membres des cours certifiants
                et des parcours débouchant sur des métiers en croissance.
                Ses contenus sont réalisés en interne, par des écoles,
                des universités, des entreprises partenaires comme Microsoft
                ou IBM, ou historiquement par des bénévoles.
                Jusqu'en 2018, n'importe quel membre du site pouvait être auteur,
                via un outil nommé « interface de rédaction » puis « Course Lab ».
                De nombreux cours sont issus de la communauté,
                mais ne sont plus mis en avant. Initialement orientée
                autour de la programmation informatique, la plate-forme
                couvre depuis 2013 des thématiques plus larges tels que
                le marketing, l'entrepreneuriat et les sciences.
                """
            ]
        ]

        mockreturn = mock('result_history')
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert demand.get_history("montmartre") == resul_history

