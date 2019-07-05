# ~ import unittest
# ~ import require
# ~ parser = require('/python')
import grandPy as p

"""separer la chaine de caractere en plusieurs mots"""


# ~ class TestMot(unittest.TestCase):
"""Test du retour de la demande d'adresse"""

def test_parser():
    """ test de la demande """
    demande = "ou est situé le restaurant la_nappe_d'or de lyon"
    assert p.parser(demmande) == "la_nappe_d'or lyon "

# ~ if __name__ == "__main__":
    # ~ unittest.main()

