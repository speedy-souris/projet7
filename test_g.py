import unittest
# ~ import require
# ~ parser = require('/python')
from python.grandPy import parser as p
"""separer la chaine de caractere en plusieurs mots"""


class TestMot(unittest.TestCase):
    """Test du retour de la demande d'adresse"""

    def test_demande(self):
        """ test de la demande """
        demande = "ou est situé le restaurant la_nappe_d\'or"
        result = p.parser(demande)
        self.assertIn(result, "lyon")

if __name__ == "__main__":
    unittest.main()

