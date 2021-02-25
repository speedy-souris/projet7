#coding:utf-8
#!/usr/bin/env python

import os
import inspect

# question organization
class Question:
    """
        organization of the user's question
    """
    # Data for check civility
    DONNEE_CIVILITY = set(
        [
        'bonjour', 'bonsoir','salut','hello','hi'
        ]
    )

    # Data for check decency
    INDECENCY_LIST = set(
        [
        'vieux','con','poussierieux','ancetre','demoder','vieillard','senille',
        'dinosaure','decrepit','arrierer ','rococo','centenaire','senille',
        'vieillot','archaique','gateux','croulant','antiquite','baderne','fossile',
        'bjr','bsr','slt'
        ]
    )

    # Data for parser (deleted for research)
    UNNECESSARY_LIST = set(
        [
        'a','abord','absolument','afin','ah','ai','aie','ailleurs','ainsi','ait',
        'allaient','allo','allons','allô','alors','ancetre','ancetre demode',
        'anterieur','anterieure','anterieures','antiquite','apres','après',
        'arriere rococo','as','assez','attendu','au','aucun','aucune','aujourd',
        "aujourd'hui",'aupres','auquel','aura','auraient','aurait','auront','aussi',
        'autre','autrefois','autrement','autres','autrui','aux','auxquelles',
        'auxquels','avaient','avais','avait','avant','avec','avoir','avons','ayant',
        'b','bah','bas','basee','bat','beau','beaucoup','bien','bigre','bonjour',
        'bonjour grandpy','bonjour grandPy\, comment vas tu','bonsoir grandpy','boum',
        'bravo','brrr','c','car','ce','ceci','cela','celle','celle-ci','celle-là',
        'celles','celles-ci','celles-là','celui','celui-ci','celui-là','cent',
        'centenaire senille','cependant','certain','certaine','certaines','certains',
        'certes','ces','cet','cette','ceux','ceux-ci','ceux-là','chacun','chacune',
        'chaque','cher','chers','chez','chiche','chut','chère','chères','ci','cinq',
        'cinquantaine','cinquante','cinquantième','cinquième','clac','clic','combien',
        'comme','comment','comment allez vous, grandpy','comparable','comparables',
        'compris','concernant','contre','couic','crac','d','da','dans','de','debout',
        'dedans','dehors','deja','delà','depuis','dernier','derniere','derriere',
        'derrière','des','desormais','desquelles','desquels','dessous','dessus','deux',
        'deuxième','deuxièmement','devant','devers','devra','different','differentes',
        'differents','différent','différente','différentes','différents',
        'dinosaure decrepit','dire','directe','directement','dit','dite','dits',
        'divers','diverse','diverses','dix','e','effet','egale','egalement','egales',
        'eh','elle','elle-même','elles','elles-mêmes','en','encore','enfin','entre',
        'envers','environ','es','est','et','etant','etc','etre','eu','euh','eux',
        'eux-mêmes','exactement','excepté','extenso','exterieur','f','fais',
        'faisaient','faisant','fait','façon','feront','fi','flac','floc','font','g',
        'gens','grandpy','h','ha','hello grandpy','hein','hem','hep','hey','hi','ho',
        'holà','hop','hormis','hors','hou','houp','hue','hui','huit','huitième','hum',
        'hurrah','hé','hélas','i','il','ils','importe','j','je','jusqu','jusque',
        'juste','k','l','la','laisser','laquelle','las','le','lequel','les',
        'lesquelles','lesquels','leur','leurs','longtemps','lors','lorsque','lui',
        'lui-meme','lui-même','là','lès','m','ma','maint','maintenant','mais','malgre',
        'malgré','maximale','me','meme','memes','merci','mes','mien',"m'indiquer",
        "m'orienter",'mienne','miennes','miens','mille','mince','minimale','moi',
        'moi-meme','moi-même','moindres','moins','mon','moyennant','multiple',
        'multiples','même','mêmes','n','na','naturel','naturelle','naturelles','ne',
        'neanmoins','necessaire','necessairement','neuf','neuvième','ni','nombreuses',
        'nombreux','non','nos','notamment','notre','nous','nous-mêmes','nouveau','nul',
        'néanmoins','nôtre','nôtres','o','oh','ohé','ollé','olé','on','ont','onze',
        'onzième','ore','ou','ouf','ouias','oust','ouste','outre','ouvert','ouverte',
        'ouverts','o|','où','p','paf','pan','papi','papy','par','parce','parfois',
        'parle','parlent','parler','parmi', 'parseme','partant','particulier',
        'particulière','particulièrement','pas','passé','pendant','pense','permet',
        'personne','peu','peut','peuvent','peux','pff','pfft','pfut','pif','pire',
        'plein','plouf','plus','plusieurs','plutôt','possessif','possessifs',
        'possible','possibles','pouah','pour','pourquoi','pourrais','pourrait',
        'pouvait','prealable','precisement','premier','première','premièrement','pres',
        'probable','probante','procedant','proche','près','psitt','pu','puis',
        'puisque','pur','pure','q','qu','quand','quant','quant-à-soi','quanta',
        'quarante','quatorze','quatre','quatre-vingt','quatrième','quatrièmement',
        'que','quel','quelconque','quelle','quelles',"quelqu'un",'quelque','quelques',
        'quels','qui','quiconque','quinze','quoi','quoique','r','rare','rarement',
        'rares','relative','relativement','remarquable','rend','rendre','restant',
        'reste','restent','restrictif','retour','revoici','revoilà','rien','s','sa',
        'sacrebleu','sait','salut','salut grandpy, comment ca va','sans','sapristi',
        'sauf','se','sein','seize','selon','semblable','semblaient','semble',
        'semblent','sent','sept','septième','sera','seraient','serait','seront','ses',
        'seul','seule','seulement','si','sien','sienne','siennes','siens','sinon',
        'situe','situé','six','sixième','soi','soi-même','soit','soixante','son',
        'sont','sous','souvent','specifique','specifiques','speculatif','stop',
        'strictement','subtiles','suffisant','suffisante','suffit','suis','suit',
        'suivant','suivante','suivantes','suivants','suivre','superpose','sur',
        'surtout','t','ta','tac','tant','tardive','te','tel','telle','tellement',
        'telles','tels','tenant','tend','tenir','tente','tes','tic','tien','tienne',
        'tiennes','tiens','toc','toi','toi-même','ton','touchant','toujours','tous',
        'tout','toute','toutefois','toutes','treize','trente','tres','trois',
        'troisième','troisièmement','trop','trouve','très','tsoin','tsouin','tu','té',
        'u','un','une','unes','uniformement','unique','uniques','uns','v','va','vais',
        'vas','vers','via','vieillard senille','vieille baderne','vieillot archaique',
        'vieux','vieux croulant','vieux fossile','vieux gateux','vieux poussierieux',
        'vif','vifs','vingt','vivat','vive','vives','vlan','voici','voilà','vont',
        'vos','votre','vous','vous-mêmes','vu','vé','vôtre','vôtres','w','x','y','z',
        'zut','à','â','ça','ès','étaient','étais','était','étant','été','être','ô',',',
        ';','.','?','!','donner',"l'adresse",'du','connais','donnez','connaissez'
        ]
    )
#---------------- constructor ------------------------------------------
    def __init__(self, question, dataDiscussion):
        """
            constructor
                organization of the user's question
        """
        self.question = question
        self.dataDiscussion = dataDiscussion

#----------------- user behavior check ---------------------------------

    def user_civility(self):
        """
            modification of attributes civility ==> parser
        """
        # list of words to find in questions
        user_answer = self.question.split()
        # search civility
        result = bool(
            [
            w for w in user_answer if w.lower() in self.DONNEE_CIVILITY
            ]
        )
        self.dataDiscussion.civility = result

    def user_decency(self):
        """
            modification of attributes decency ==> parser
        """
        # list of words to find in questions
        user_answer = self.question.split()
        # search decency
        result = bool(
            [
            w for w in user_answer if w.lower() not in self.INDECENCY_LIST
            ]
        )
        self.dataDiscussion.decency = result

    def user_comprehension(self):
        """
            modification of attributes comprehension ==> parser
        """
        # list of words to find in questions
        user_answer = self.question.split()
        # search comprehension
        result = bool(
            [
            w for w in user_answer if w.lower() in self.DONNEE_CIVILITY
                or w.lower() in self.INDECENCY_LIST
                or w.lower() in self.UNNECESSARY_LIST
            ]
        )
        self.dataDiscussion.comprehension = result

    # parser
    def parser(self):
        """
            function that cuts the string of characters (question asked to GrandPy)
            into a word list then delete all unnecessary words to keep only
            the keywords for the search
        """

        # list of words to remove in questions
        list_question = self.question.split()
        result = [
            w for w in list_question if w.lower() not in self.UNNECESSARY_LIST
        ]
        message = ' '.join(result)
        return message
        
#------------------------ Response User --------------------------------

    def message(self, check):
        user_response = {
            'civility': self.user_civility,
            'decency': self.user_decency,
            'comprehension': self.user_comprehension,
            'parser': self.parser
        }
        print(f'\nquestion retour user = {user_response[check]()}')
        return user_response[check]()
