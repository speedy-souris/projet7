#coding:utf-8
#!/usr/bin/env python

import inspect
import redis


                           #========================
                           # class setting function
                           #========================

#==================================
# converting data values for Redis
#==================================
# boolean ==> string
def bool_convers(value):
    """
        conversion from boolean to string
    """
    if value :
        return '1'
    else:
        return '0'


# string ==> boolean
def str_convers(value):
    """
        conversion from string to boolean
    """
    value = value.decode('utf8')
    if value == '0':
        return False
    elif value == '':
        return False
    else:
        return True


                           #==============
                           # Script class
                           #==============
# user question parameter
class QuestionParameter:
    """
        API Private Key and Constants Management :
            local (development) / external (production)
                status_env()
                    - key_data['map']         ==> KEY_API_MAP / HEROKU_KEY_API_MAP
                    - key_data['staticMap']   ==> KEY_API_STATIC_MAP / HEROKU_KEY_API_STATIC_MAP
                    - key_data['status_prod'] ==> True / False

        Management for initializing configuration database Redis
            - redis_connect() ==> connection initialization for the Redis database
            - writing()       ==> writing of data value for the Redis database
            - incrementing()  ==> incrementing the data value for the Redis database
            - expiry()        ==> data value expiration times for the Redis database
            - reading         ==> read data value for the Redis database

        the content of the user question for the analyzer script
            - messages--|            content of the question asked to grandpy
                        |-- list ==> by the user containing the keywords
                        |            for the Google Map API / Grandpy's response
            - chatters--|----------- speaker for the question / answer (Grandpy / user)
            - tmp ---------      ==> temporary variable for for the question parser
            - grandpy -----      ==> grandpa robot
            - user --------      ==> user asking questions

        default variables in Redis
            - quotas           ==> initialisation of quotas attribut
            - nb_indecency     ==> number of user indecency
            - nb_request       ==> number of user requests
            - redis_connect()  ==> initialization of the connection method
                                   to the Redis database
            - initial_status() ==> initialization of data values
                                   from the Redis database
            - civility
            - decency
            - comprehension
    """
    #========================
    # Data for test civility
    #========================
    DONNEE_CIVILITY = set(
        [
        'bonjour', 'bonsoir','salut','hello','hi'
        ]
    )

    #=======================
    # Data for test decency
    #=======================
    INDECENCY_LIST = set(
        [
        'vieux','con','poussierieux','ancetre','demoder','vieillard','senille',
        'dinosaure','decrepit','arrierer ','rococo','centenaire','senille',
        'vieillot','archaique','gateux','croulant','antiquite','baderne','fossile',
        'bjr','bsr','slt'
        ]
    )

    #=================================
    # Data for parser (answer's user)
    #=================================
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
        ';','.','?','!'
        ]
    )

    # constructor
    def __init__(self, debug):
        """
            contructor of parameter
                - messages, tmp, grandpy, user
                - civility, decency, comprehension, quotas
                - nb_incivility, nb_indecency, nb_incomprehension, nb_request
        """
        self.debug = debug
        self.messages = []
        self.chatters = []
        self.tmp = ''  # temporary variable for civility / decency wordlist
        self.grandpy = 'Grandpy' # user for message
        self.user = 'User'  # user for message
        self.civility = False
        self.decency = False
        self.comprehension = False
        self.quotas = False
        self.nb_incivility = 1
        self.nb_indecency = 1
        self.nb_incomprehension = 1
        self.nb_request = 1
        self.redis_connect()
        self.initial_status()


    #==============
    # Server Redis
    #==============
    def redis_connect(self):
        """
            connection to the Redis database
        """
        self.connect = redis.Redis(
            host='localhost',
            port=6379,
            db=0
        )


    # writing
    def writing(self, data, value):
        """
            writing data to Redis database
        """
        self.connect.set(data, value)


    # increment
    def incrementing(self, data):
        """
            incrementing the request counter in Redis database
        """
        self.connect.incr(data)


    # expiration time
    def expiry(self, data, value):
        """
            expiration
            of the counter variable in Redis database
            (after 24 hours)
        """
        self.connect.expire(data, value)


    # reading
    def reading(self, data):
        """
            reading data in Redis database
        """
        return self.connect.get(data)


    #==================================
    # Initialization status parameters
    #==================================
    def initial_status(self):
        """
            creation and initialization by default of data values
            for the Redis database

                - write_ civility()   ==> default initialization of civility values
                                          for the Redis database
                - write_quotas()      ==> default initialization of quotas values
                                          for the Redis database
                - write_decency()   ==> default initialization of decency values
                                          for the Redis database
                - write_counter()     ==> default initialization of counter values
                                          for the Redis database

        """
        self.write_civility(False)
        self.write_quotas(False)
        self.write_decency(False)
        self.write_comprehension(False)
        self.write_counter(1)

    def reset_status(self):
        """
            resetting the counters:
               - nb_incomprehension  --|
               - nb_incivility  -------|
               - nb_indecency  --------| ==> 1
               - nb_request  ----------|

            initialisation parameters:
                - comprehension --|
                - civility -------| ==> False
                - decency --------|
                - quotas  --------|
        """
        self.nb_incomprehension = 1
        self.nb_incivility = 1
        self.nb_indecency = 1
        self.nb_request = 1
        self.comprehension = False
        self.decency = False
        self.civility = False
        self.quotas = False

    #==========================
    # status parameter display
    #==========================
    def display_status(self):
        """
            display of data values in the question

                - nb_incivility      ==> number of civility
                - nb_indecency       ==> number of decency
                - nb_incomprehension ==> number of comprehension
        """
        print(f'\nquestion = {self.tmp}\n')
        print(f'Valeur de quotas = {self.quotas}')
        print(f'Valeur de civility = {self.civility}')
        print(f'valeur de decency = {self.decency}')
        print(f'valeur de comprehension = {self.comprehension}')
        print(f"Nombre d'incivility = {self.nb_incivility}")
        print(f"Nombre d'indecency = {self.nb_indecency}")
        print(f"Nombre d'incomprehension = {self.nb_incomprehension}")


    #==============================================
    # value of data Civility in the Redis database
    #==============================================
    def write_civility(self, civility):
        """
            saving of civility configuration in Redis database
        """
        self.writing('civility', bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration in Redis database
        """
        return str_convers(self.reading('civility'))


    #============================================
    # value of data quotas in the Redis database
    #============================================
    def write_quotas(self, quotas):
        """
            saving of quotas configuration in Redis database
        """
        self.writing('quotas', bool_convers(quotas))


    @property
    def read_quotas(self):
        """
            reading of quotas configuration in Redis database
        """
        return str_convers(self.reading('quotas'))


    #===============================================
    # value of data decency in the Redis database
    #===============================================
    def write_decency(self, decency):
        """
            saving of decency configuration in Redis database
        """
        self.writing('decency', bool_convers(decency))


    @property
    def read_decency(self):
        """
            reading of decency configuration in Redis database
        """
        return str_convers(self.reading('decency'))


    #===============
    # comprehension
    #===============
    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration in Redis database
        """
        self.comprehension = comprehension
        self.writing(
            'comprehension',
            bool_convers(self.comprehension)
        )


    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration in Redis database
        """
        return str_convers(self.reading('comprehension'))


    #=================
    # Counter Request
    #=================
    def increment_counter(self):
        """
            Counter increment in Redis database
        """
        self.nb_request = self.incrementing('nb_request')


    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter) in Redis database
        """
        self.expiry('nb_request', 86400)


    @property
    def read_counter(self):
        """
            reading of counter configuration in Redis database
        """
        return self.reading('nb_request')


    def write_counter(self, value):
        """
            modification of the value
            of the request counter in Redis database
        """
        self.writing('nb_request', value)

    #=============
    # add message
    #=============
    def add_message(self, message, chatter):
        """
            Add new message with chatter
        """
        # start
        print(self.debug.name('add_message'))
        print(self.debug.nb_line(inspect.currentframe().f_lineno+1), end=' ==> ')
        print(self.debug.historical(f'{message}','add_message'))
        print(self.debug.nb_line(inspect.currentframe().f_lineno+1), end=' ==> ')
        print(self.debug.historical(f'{chatter}','add_message'))
        # end
        self.messages.append(message)
        self.chatters.append(chatter)
        if chatter == 'User':
            self.tmp = message


    #========================
    # message initialization
    #========================
    def init_message(self):
        """
            resetting the message list
        """
        self.messages[:] = []
        self.chatters[:] = []


    #====================
    # Read list messages
    #====================
    def chat_viewer(self):
        """
            Read full list of messages
        """
        for (counter, (chatter, message)) in enumerate(
            zip(self.chatters, self.messages)):
            print(f'{counter + 1}.{[chatter]} = {message}')

