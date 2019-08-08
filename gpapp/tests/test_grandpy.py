#!/usr/bin/env python

from gpapp.grandPy import parser

# parser test on the question asked to grandPy
def test_parser():
    """
    Test function on the separation of the character string (question asked
     a papyRobot alias grandPy) in several words,
     removing unnecessary words in order to keep the keywords for the
     search (location history & geographic coordinates)
    """
    # question asked to grandPy
    demand = "ou est situé le restaurant la_nappe_d_or de lyon"

    assert parser(demand) == ["restaurant","la_nappe_d_or","lyon"]


