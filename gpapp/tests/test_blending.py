#coding:utf-8
#!/usr/bin/env python

from .. import blending as script

class TestQuestionrAnalysis:
    """
        analysis of responses with civility, decency comprehension
    """

    def Test_question(self):
        """
            civility / incility analysis on the question asked by the user
        """

        if script.dialog.nb_incility == 3\
            and script.dialog.nb_indecency == 0\
            and script.dialog.nb_incomprehension == 0:

            assert script.inspect.nspect.currentframe().f_lineno == 702
