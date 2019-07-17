from gpapp.grandPy import parser
"""
Fonction de test sur la separation la chaine de caractere (question posé
a papyRobot alias grandPy) en plusieurs mots,
suppression des mots inutiles afin de garder les mots clés pour la
recherche (historique du lieux & coordonnée géographique)
"""
# test de parser sur la question posé à grandPy

def test_parser():
    # question posée à grandPy
    demande = "ou est situé le restaurant la_nappe_d_or de lyon"
    assert parser(demande) == ["restaurant","la_nappe_d_or","lyon"]

# def test_geolocalisation():
