#coding:utf-8
#!/usr/bin/env python

import os
import redis
import time
import json
import urllib.request, urllib.parse

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

                     #=================
                     # Script function
                     #=================

#================================
# address coordinate calculation
#================================
def map_coordinates(question):
    """
        calculating the coordinates of the question asked to granbpy
        Vars :
            - parser_answer
            - place_id_dict
            - map_status
    """

    my_conversation = DataParameter(question)
    # keyword isolation for question
    parse_answer = my_conversation.parser()
    place_id_dict = my_conversation.get_place_id_list(
        address=" ".join(parse_answer)
    )
    # creation and test public key api google map
    place_id = place_id_dict["candidates"][0]["place_id"]
    # creation of api google map coordinate address display setting
    # and wikipedia address history display setting
    my_conversation.get_address(place_id=place_id)
    my_conversation.get_history(search_history=" ".join(parse_answer))

def user_exchange(question):
    """
        user / grandpy display initialization
    """
    # politeness check
    script.Behaviour().wickedness(question)
    # courtesy check
    script.Behaviour().civility(question)
    # comprehension check
    script.Behaviour().comprehension(question)
    # end of session check
    if setting.DataRedis().readCounter() >= 10:
        setting.DataRedis().writeQuotas(True)
        setting.DataRedis().expiryCounter()
    script.Behaviour().counter_session(question, setting.DataRedis().readCounter())
    script.Behaviour().apiSession(question)

                                #==============
                                # Script class
                                #==============
# Redis server organization
class DataParameter:
    """
        API Private Key and Constants Management :
            local (development) / external (production)
                status_env()
                    - key_data["map"]         ==> KEY_API_MAP / HEROKU_KEY_API_MAP
                    - key_data["staticMap"]   ==> KEY_API_STATIC_MAP / HEROKU_KEY_API_STATIC_MAP
                    - key_data["status_prod"] ==> True / False
            Constants for processing keywords for Google Map APIs and grandpy's behavior
            according to the content of the user question
                - CIVILITY_LIST-----|
                - DECENCY_LIST----|--set()
                - UNNECESSARY_LIST--|
        Management for initializing configuration database Redis
            - redis_connect() ==> connection initialization for the Redis database
            - writing()       ==> writing of data value for the Redis database
            - incrementing()  ==> incrementing the data value for the Redis database
            - expiry()        ==> data value expiration times for the Redis database
            - reading         ==> read data value for the Redis database
    """
    CIVILITY_LIST = set(
        [
        "bonjour", "bonsoir","salut","hello","hi"
        ]
    )
    DECENCY_LIST = set(
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

    def __init__(self, question):
        """
            constructor
            for initializing the API default variables in Redis
                - question         ==> content of the question asked to grandpy
                                       by the user containing the keywords
                                       for the Google Map API
                - key_data         ==> dictionary containing private keys
                                       (environment variables) for Google Map APIs
                - redis_connect()  ==> initialization of the connection method
                                       to the Redis database
                - initial_status() ==> initialization of data values
                                       from the Redis database
        """
        self.question = question
        self.key_data = {}
        # ~ self.constant = {}
        self.redis_connect()
        self.initial_status()

    #==============
    # Server Redis
    #==============
    def redis_connect(self):
        """
            method for connection to the Redis database
                - status_env["status_prod"] = False ==> Redis database in local
                - status_env["status_prod"] = True ==> Redis database in online
        """
        if not self.status_env["status_prod"]:
            self.connect = redis.Redis(
                host="localhost",
                port=6379,
                db=0
            )
        else:
            self.connect = redis.Redis(
                host="grandpy-papy-robot.herokuapp.com/",
                port=6379,
                db=1
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

    # Google API keys
    @property
    def status_env(self):
        """
            management of environment variables
            local and online
                - key_data["map"]         ==> =|
                - key_data["staticMap"]   ==> =|- private keys for Google APIs
                                                 (local or online)
                - key_data["status_prod"] ==> boolean for redis database
                                              connection method

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

    #==================================
    # Initialization status parameters
    #==================================
    def initial_status(self):
        """
            creation and initialization by default of data values
            for the Redis database
                - write_quotas()        ==> default initialization of quota values
                                            for the Redis database
                - write_civility()      ==> default initialization of civility values
                                            for the Redis database
                - write_decency()       ==> default initialization of decency values
                                            for the Redis database
                - write_comprehension() ==> default initialization of comprehension values
                                            for the Redis database
                - write_counter()       ==> default initialization of counter values
                                            for the Redis database

        """
        self.write_quotas(False)
        self.write_civility(False)
        self.write_decency(False)
        self.write_comprehension(False)
        self.write_counter("0")

    #============
    # Quotas_api
    #============
    def write_quotas(self, quotas):
        """
            saving of quotas configuration in Redis database
        """
        self.quotas = quotas
        self.writing("quotas_api", bool_convers(self.quotas))

    @property
    def read_quotas(self):
        """
            reading of quotas configuration in Redis database
        """
        return str_convers(self.reading("quotas_api"))

    #==========
    # Civility
    #==========
    def write_civility(self, civility):
        """
            saving of civility configuration in Redis database
        """
        # ~ self.civility = civility
        self.writing("civility", bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration in Redis database
        """
        return str_convers(self.reading("civility"))

    #=========
    # Decency
    #=========
    def write_decency(self, decency):
        """
            saving of decency configuration in Redis database
        """
        self.writing("decency", bool_convers(decency))

    @property
    def read_decency(self):
        """
            reading of decency configuration in Redis database
        """
        return str_convers(self.reading("decency"))

    #===============
    # comprehension
    #===============
    def write_comprehension(self, comprehension):
        """
            saving of comprehension configuration in Redis database
        """
        self.comprehension = comprehension
        self.writing(
            "comprehension",
            bool_convers(self.comprehension)
        )

    @property
    def read_comprehension(self):
        """
            reading of comprehension configuration in Redis database
        """
        return str_convers(Conversation.reading("comprehension"))

    #=================
    # Counter Request
    #=================
    @property
    def increment_counter(self):
        """
            Counter increment in Redis database
        """
        self.nb_request = self.incrementing("nb_request")

    @property
    def expiry_counter(self):
        """
            Expiration of the key nb_request (counter) in Redis database
        """
        self.expiry("nb_request", 86400)

    @property
    def read_counter(self):
        """
            reading of counter configuration in Redis database
        """
        return self.reading("nb_request")

    def write_counter(self, value):
        """
            modification of the value
            of the request counter in Redis database
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
            w for w in list_question if w.lower() not in self.DECENCY_LIST
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
                in InitData.CIVILITY_LIST and w.lower() in self.DECENCY_LIST
            ]
        )

        self.write_comprehension(result3)

    #===================================
    # place_id search on Google Map API
    #===================================
    def get_place_id_list(self, address):
        """
            Google map API place_id search function
        """
        key = self.status_env["map"] # environment variable
        # replacing space by "% 20" in the string of characters
        address_encode = urllib.parse.quote(str(address))

        place_id = urllib.request.urlopen(
            "https://maps.googleapis.com/maps/api/place/findplacefromtext/"\
            +f"json?input={address_encode}&inputtype=textquery&key={key}"
        )

        result = json.loads(place_id.read().decode("utf8"))

        return result

    #===========================
    # address on Google Map API
    #===========================
    def get_address(self, place_id):
        """
            Google map API address search with place_id function
        """
        key = self.status_env["map"] # environment variable

        address_found= urllib.request.urlopen(
            "https://maps.googleapis.com/maps/api/place/details/"\
            f"json?placeid={place_id}&fields=formatted_address,geometry&key={key}"
        )

        result = json.loads(address_found.read().decode("utf8"))

        return result

    #=================================
    # history search on wikimedia API
    #=================================
    def get_history(self, search_history):
        """
            wikipedia API (Wikimedia) history search
        """
        # replacing space by "% 20" in the string of characters
        history_encode = urllib.parse.quote(search_history)

        history_found = urllib.request.urlopen(
            "https://fr.wikipedia.org/w/api.php?action=opensearch&search="\
            f"{history_encode}&format=json"
        )

        result = json.loads(history_found.read().decode("utf8"))
        return result

    #=========================================
    # map display in the Google Map Satic API
    #=========================================
    def get_map_static(self, location_map):
        """
            function of displaying the geolocation of the address
            asked to grandpy on the map of the Google Map Static API
        """
        key = self.status_env["staticMap"]  # environment variable

        # replacing space by "% 20" in the string of characters
        formatting_address = urllib.parse.quote(location_map["address"])
        # longitude and latitude display
        localization = location_map["location"]
        # display map
        display_map = "https://maps.googleapis.com/maps/api/staticmap?center="\
            +formatting_address+\
            "&zoom=18.5&size=600x300&maptype=roadmap&markers=color:red%7Clabel:A%7C"\
            +str(localization['lat'])+","+str(localization['lng'])+f"&key={key}"

        return display_map

    #===================
    # question analysis
    #===================
    def attribute_analysis(self):
        """
            behavioral analysis of the question asked by the user
                - civility
                - decency
                - comprehension
        """
        if not self.read_civlity:
            arg_civility = False
        else:
            arg_civility = True
        if not self.read_decency:
            arg__decency = False
        else:
            arg_decency = True
        if not read_comprehension:
            arg_comprehension = False
        else:
            arg_comprehension = True



        # ~ self.civlity = self.read_civility
        # ~ self.decency = self.read_decency
        # ~ self.comprehension = self.read_comprehension



# ~ #==========
# ~ # Data API
# ~ #==========
# ~ class Conversation:
    # ~ """
        # ~ data management requested by the user
    # ~ """
    # ~ DATA = DataParameter("bonjour")
    # ~ pass
    # ~ @property
    # ~ def t_decency(self):
        # ~ return setting().writeDecency(True)

    # ~ @property
    # ~ def f_decency(self):
        # ~ return setting().writeDecency(False)

    # ~ @property
    # ~ def r_decency(self):
        # ~ return setting().readDecency()

    # ~ @property
    # ~ def t_civility(self):
        # ~ return setting().writeCivility(True)

    # ~ @property
    # ~ def f_civility(self):
        # ~ return setting().writeCivility(False)

    # ~ @property
    # ~ def r_civility(self):
        # ~ return setting().readCivility()

    # ~ @property
    # ~ def t_comprehension(self):
        # ~ return setting().writeComprehension(True)

    # ~ @property
    # ~ def f_comprehension(self):
        # ~ return setting().writeComprehension(False)

    # ~ @property
    # ~ def r_comprehension(self):
        # ~ return setting().readComprehension()

    # ~ @property
    # ~ def t_quotas(self):
        # ~ return setting().writeQuotas(True)

    # ~ @property
    # ~ def f_quotas(self):
        # ~ return setting().writeQuotas(False)

    # ~ @property
    # ~ def r_quotas(self):
        # ~ return setting().readQuotas()

# ~ class Politeness:
    # ~ """

    # ~ """
    # ~ #===========================
    # ~ # Initialization wickedness
    # ~ #===========================
    # ~ def wickedness(self, question):
        # ~ """
            # ~ Disrespect management function
            # ~ initialization of wickedness
                # ~ - decency
         # ~ """
        # ~ Behaviour().t_decency
        # ~ if question.lower() in config().constant["list_decency"]:
            # ~ Behaviour().f_decency
        # ~ return Behaviour().r_decency
    # ~ #=========================
    # ~ # Initialization Civility
    # ~ #=========================
    # ~ def civility(self, question):
        # ~ """
            # ~ Incivility management function
            # ~ initialization of incivility
                # ~ - civility
        # ~ """
        # ~ Behaviour().t_decency
        # ~ setting.writeComprehension(True)
        # ~ if question.lower() in config().constant["list_civility"]:
            # ~ Behaviour().t_civility
        # ~ return Behaviour().r_civility

    # ~ #==============================
    # ~ # Initialization comprehension
    # ~ #==============================
    # ~ def comprehension(self, question):
        # ~ """
            # ~ Incomprehension management function
            # ~ initialization of incomprehension
                # ~ - comprehension
        # ~ """
        # ~ try:
            # ~ func.map_coordinates(question)
        # ~ except IndexError:
            # ~ Behaviour().f_comprehension
            # ~ return setting().COMPREHENSION
        # ~ Behaviour().t_comprehension
        # ~ return Behaviour().r_comprehension



    #==========================================
    # Initialization session by API parameters
    #==========================================
    # ~ def api_session(self, question, apiParams=False):
        # ~ """
            # ~ Session management function
            # ~ initialization of session
                # ~ - quotas_api
        # ~ """
        # ~ if apiParams:
            # ~ Behaviour().t_quotas

        # ~ try:
            # ~ func.map_coordinates(question)
        # ~ except (TypeError,KeyError):
            # ~ Behaviour().t_quotas

        # ~ return Behaviour().r_quotas

if __name__ == "__main__":
    pass
