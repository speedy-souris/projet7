#coding:utf-8
#!/usr/bin/env python

import redis
# ~ from .dataInitial import InitData

# Redis server organization
class DataParameter:
    """
        API Private Key and Constants Management class:
            local (development) / external (production)
                - MAP ==> KEY_API_MAP / HEROKU_KEY_API_MAP
                - STATIC_MAP ==> KEY_API_STATIC_MAP / HEROKU_KEY_API_STATIC_MAP
            - status_prod (True / False)
        Constants for dealing with the issue at Grandpy
            - CIVILITY_LIST....               .list_civility....
            - INDECENCY_LIST... ==> set() ==> .list_indecency... ==> dict()
            - UNNECESSARY_LIST.               .list_unnecessary.
        Initialization of Redis connection parameters
            - CONNECT
        Management class for initializing configuration data
            - quotas
            - civility
            - decency
            - comprehension
            - nb_request
    """
    CIVILITY_LIST = set(
        [
        "bonjour", "bonsoir","salut","hello","hi"
        ]
    )
    INDECENCY_LIST = set(
        [
        "vieux","con","poussierieux","ancetre","demoder","vieillard","senille",
        "dinosaure","decrepit","arrierer ","rococo","centenaire","senille",
        "vieillot","archaique","gateux","croulant","antiquite","baderne","fossile",
        "bjr","bsr","slt"
        ]
    )
    UNNECESSARY_LIST = set(
        [
        "a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait",
        "allaient","allo","allons","allô","alors","ancetre","ancetre demode",
        "anterieur","anterieure","anterieures","antiquite","apres","après",
        "arriere rococo","as","assez","attendu","au","aucun","aucune","aujourd",
        "aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi",
        "autre","autrefois","autrement","autres","autrui","aux","auxquelles",
        "auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant",
        "b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","bonjour",
        "bonjour grandpy","bonjour grandPy\, comment vas tu","bonsoir grandpy","boum",
        "bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là",
        "celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent",
        "centenaire senille","cependant","certain","certaine","certaines","certains",
        "certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune",
        "chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq",
        "cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien",
        "comme","comment","comment allez vous, grandpy","comparable","comparables",
        "compris","concernant","contre","couic","crac","d","da","dans","de","debout",
        "dedans","dehors","deja","delà","depuis","dernier","derniere","derriere",
        "derrière","des","desormais","desquelles","desquels","dessous","dessus","deux",
        "deuxième","deuxièmement","devant","devers","devra","different","differentes",
        "differents","différent","différente","différentes","différents",
        "dinosaure decrepit","dire","directe","directement","dit","dite","dits",
        "divers","diverse","diverses","dix","e","effet","egale","egalement","egales",
        "eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre",
        "envers","environ","es","est","et","etant","etc","etre","eu","euh","eux",
        "eux-mêmes","exactement","excepté","extenso","exterieur","f","fais",
        "faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g",
        "gens","grandpy","h","ha","hello grandpy","hein","hem","hep","hey","hi","ho",
        "holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum",
        "hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque",
        "juste","k","l","la","laisser","laquelle","las","le","lequel","les",
        "lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui",
        "lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre",
        "malgré","maximale","me","meme","memes","merci","mes","mien","m'indiquer",
        "m'orienter","mienne","miennes","miens","mille","mince","minimale","moi",
        "moi-meme","moi-même","moindres","moins","mon","moyennant","multiple",
        "multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne",
        "neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses",
        "nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul",
        "néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze",
        "onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte",
        "ouverts","o|","où","p","paf","pan","papi","papy","par","parce","parfois",
        "parle","parlent","parler","parmi", "parseme","partant","particulier",
        "particulière","particulièrement","pas","passé","pendant","pense","permet",
        "personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire",
        "plein","plouf","plus","plusieurs","plutôt","possessif","possessifs",
        "possible","possibles","pouah","pour","pourquoi","pourrais","pourrait",
        "pouvait","prealable","precisement","premier","première","premièrement","pres",
        "probable","probante","procedant","proche","près","psitt","pu","puis",
        "puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta",
        "quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement",
        "que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques",
        "quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement",
        "rares","relative","relativement","remarquable","rend","rendre","restant",
        "reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa",
        "sacrebleu","sait","salut","salut grandpy, comment ca va","sans","sapristi",
        "sauf","se","sein","seize","selon","semblable","semblaient","semble",
        "semblent","sent","sept","septième","sera","seraient","serait","seront","ses",
        "seul","seule","seulement","si","sien","sienne","siennes","siens","sinon",
        "situe","situé","six","sixième","soi","soi-même","soit","soixante","son",
        "sont","sous","souvent","specifique","specifiques","speculatif","stop",
        "strictement","subtiles","suffisant","suffisante","suffit","suis","suit",
        "suivant","suivante","suivantes","suivants","suivre","superpose","sur",
        "surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement",
        "telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne",
        "tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous",
        "tout","toute","toutefois","toutes","treize","trente","tres","trois",
        "troisième","troisièmement","trop","trouve","très","tsoin","tsouin","tu","té",
        "u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais",
        "vas","vers","via","vieillard senille","vieille baderne","vieillot archaique",
        "vieux","vieux croulant","vieux fossile","vieux gateux","vieux poussierieux",
        "vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont",
        "vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z",
        "zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô",",",
        ";",".","?","!"
        ]
    )

                    #==============
                    # Server Redis
                    #==============
    if not self.status_env["status_prod"]:
        CONNECT = redis.Redis(
            host="localhost",
            port=6379,
            db=0
        )
    else:
        CONNECT = redis.Redis(
            host="grandpy-papy-robot.herokuapp.com/",
            port=6379,
            db=1
        )

    def __init__(self, question):
        """
            constructor
            for initializing the API default variables in Redis
        """
        self.question = question
        self.key_data = {}
        self.constant = {}
        self.initial_status()

    @classmethod
    def writing(cls, data, value):
        """
            writing data to Redis
        """
        cls.CONNECT.set(data, value)

    @classmethod
    def incrementing(cls, data):
        """
            incrementing the request counter in Redis
        """
        cls.CONNECT.incr(data)

    @classmethod
    def expiry(cls, data, value):
        """
            expiration
            of the counter variable in Redis
            (after 24 hours)
        """
        cls.CONNECT.expire(data, value)

    @classmethod
    def reading(cls, data):
        """
            reading data in Redis
        """
        return cls.CONNECT.get(data)

    @property
    def status_env(self):
        """
            management of environment variables
            local and online
                - map
                - static_map
                - heroku_map
                - heroku_static_map
        """
        if os.environ.get("HEROKU_KEY_API_MAP") is None:

            self.key_data["map"] = os.getenv("KEY_API_MAP")
            self.key_data["staticMap"] = os.getenv("KEY_API_STATIC_MAP")
            self.key_data["status_prod"] = False
        else:
            self.key_data["map"] = os.getenv("HEROKU_KEY_API_MAP")
            self.key_data["staticMap"] = os.getenv("HEROKU_KEY_API_STATIC_MAP")
            self.key_data["status_prod"] = True

        return self.key_data

                        #=================
                        # Initialization
                        # Data of setting
                        #=================

    #==================================
    # Initialization status parameters
    #==================================
    def initial_status(self):
        """
            creation and initialization of parameters for REDIS
        """
        self.write_quotas(False)
        self.write_civility(False)
        self.write_decency(True)
        self.write_comprehension(True)
        self.write_counter("0")

    #============
    # Quotas_api
    #============
    def write_quotas(self, quotas):
        """
            saving of quotas configuration
        """
        self.quotas = quotas
        self.writing("quotas_api", bool_convers(self.quotas))

    @property
    def read_quotas(self):
        """
            reading of quotas configuration
        """
        return str_convers(self.reading("quotas_api"))

    #==========
    # Civility
    #==========
    def write_civility(self, civility):
        """
            saving of civility configuration
        """
        # ~ self.civility = civility
        self.writing("civility", bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration
        """
        return str_convers(self.reading("civility"))

    #=========
    # Decency
    #=========
    def write_decency(self, decency):
        """
            saving of decency configuration
        """
        self.writing("decency", bool_convers(decency))

    @property
    def read_decency(self):
        """
            reading of decency configuration
        """
        return str_convers(self.reading("decency"))

    #===============
    # comprehension
    #===============
    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration
        """
        self.comprehension = comprehension
        self.writing(
            "comprehension",
            bool_convers(self.comprehension)
        )

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration
        """
        return str_convers(Conversation.reading("comprehension"))

    #=================
    # Counter Request
    #=================
    @property
    def increment_counter(self):
        """
            Counter increment
        """
        self.nb_request = self.incrementing("nb_request")

    @property
    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter)
        """
        self.expiry("nb_request", 86400)

    @property
    def read_counter(self):
        """
            reading of counter configuration
        """
        return self.reading("nb_request")

    def write_counter(self, value):
        """
            modification of the value
            of the request counter in Redis
        """
        self.writing("nb_request", value)
        # ~ try:
            # ~ self.writing("nb_request", value)
        # ~ except TypeError:
            # ~ self.writing("nb_request", 0)
    #========
    # parser
    #========
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

        return result

    #==========
    # civility
    #==========
    def civility(self):
        """
            modification of attributes civility
        """
        # list of words to find in questions
        list_question = self.question.split()
        # search civility
        result1 = bool(
            [
            w for w in list_question if w.lower() in self.CIVILITY_LIST
            ]
        )
        self.write_civility(result1)

    #=========
    # decency
    #=========
    def decency(self):
        """
            modification of attributes decency
        """
        # list of words to find in questions
        list_question = self.question.split()
        # search decency
        result2 = bool(
            [
            w for w in list_question if w.lower() not in self.INDECENCY_LIST
            ]
        )

        self.write_decency(result2)

    def comprehension(self):
        """
            modification of attributes decency
        """
        # list of words to find in questions
        list_question = self.question.split()
        # search comprehension
        result3 = bool(
            [
            w for w in list_question if w.lower()\
                in InitData.CIVILITY_LIST and w.lower() in self.INDECENCY_LIST
            ]
        )

        self.write_comprehension(result3)

                    #==================================
                    # converting data values for Redis
                    #==================================
# boolean ==> string
def bool_convers(value):
    """
        conversion from boolean to string
    """
    if value :
        return "1"
    else:
        return "0"

 # string ==> boolean
def str_convers(value):
    """
        conversion from string to boolean
    """
    value = value.decode("utf8")
    if value == "0":
        return False
    elif value == "":
        return False
    else:
        return True


if __name__ == "__main__":
    pass

