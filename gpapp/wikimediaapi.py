#coding:utf-8
#!/usr/bin/env python

import urllib.request
import json


# ~ # WikiMedia APi test on search
    # ~ def test_search_wiki(self, monkeypatch):
        # ~ """
            # ~ A.P.I wikipedia test function (wikimedia) that returns a file
            # ~ Json containing the history of the requested address
        # ~ """
        # ~ demand = script.DataParameter("bonjour")
        # ~ resul_history = [
            # ~ [
                # ~ """Riche d'un long passé artistique, ce secteur de Paris (France)
                # ~ dominé par la Basilique du Sacré-Cœur a toujours été le symbole
                # ~ d'un mode de vie bohème où, de Picasso à Modigliani, de nombreux
                # ~ artistes trouvèrent refuge."""
            # ~ ]
        # ~ ]

        # ~ def mockreturn(request):
            # ~ """
                # ~ Mock function on history search
            # ~ """

            # ~ return BytesIO(json.dumps(resul_history).encode())

        # ~ monkeypatch.setattr(
            # ~ urllib.request, 'urlopen',mockreturn
        # ~ )

        # ~ assert demand.get_history("montmartre") == resul_history
