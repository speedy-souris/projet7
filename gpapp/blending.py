#coding:utf-8
#!/usr/bin/env python

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

#============================

#============================

                           #==============
                           # Script class
                           #==============
# Redis server organization
class Chat:
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
            - INDECENCY_LIST----|--set()
            - UNNECESSARY_LIST--|

        Management for initializing configuration database Redis
            - redis_connect() ==> connection initialization for the Redis database
            - writing()       ==> writing of data value for the Redis database
            - incrementing()  ==> incrementing the data value for the Redis database
            - expiry()        ==> data value expiration times for the Redis database
            - reading         ==> read data value for the Redis database
    """
    #========================
    # Data for test civility
    #========================
    DONNEE_CIVILITY = set(
        [
        "bonjour", "bonsoir","salut","hello","hi"
        ]
    )

    #=======================
    # Data for test decency
    #=======================
    INDECENCY_LIST = set(
        [
        "vieux","con","poussierieux","ancetre","demoder","vieillard","senille",
        "dinosaure","decrepit","arrierer ","rococo","centenaire","senille",
        "vieillot","archaique","gateux","croulant","antiquite","baderne","fossile",
        "bjr","bsr","slt"
        ]
    )

    #=================================
    # Data for parser (answer's user)
    #=================================
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

    #======================
    # Constructor of class
    #======================
    def __init__(self):
        """
            constructor
            for initializing the API default variables in Redis
                - messages--|       ==> content of the question asked to grandpy
                            |--list    by the user containing the keywords
                            |          for the Google Map API / Grandpy's response
                - chatters--|      ==> speaker for the question / answer (Grandpy / user)
                - civility         ==> initialization of civility attribut
                - quotas           ==> initialisation of quotas attribut
                - indecency        ==> user`s coarseness (value boolean)
                - comprehension    ==> understanding of user question
                - nb_indecency     ==> number of user indecency
                - nb_request       ==> number of user requests
                - redis_connect()  ==> initialization of the connection method
                                       to the Redis database
                - initial_status() ==> initialization of data values
                                       from the Redis database
        """
        self.messages = []
        self.chatters = []
        self.tmp = ""  # temporary variable for civility / indecency wordlist
        self.grandpy = "Grandpy" # user for message
        self.user = "User"  # user for message
        self.civility = False
        self.quotas = False
        self.indecency = False
        self.comprehension = True
        self.nb_indecency = 0
        self.nb_request = 0
        self.redis_connect()
        self.initial_status()

    #=============
    # add message
    #=============
    def add_message(self, message, chatter):
        """
            Add new message with chatter
        """
        self.messages.append(message)
        self.chatters.append(chatter)
        if chatter == "User":
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
            zip(self.chatters, self.messages)
        ):
            print(f"{counter + 1}.{[chatter]} = {message}")

    #========================================
    # reconnection after 24 hours of waiting
    #========================================
    def reconnection(self):
        """
            stop questions and answers for 24 hours
        """
        response = "reviens me voir demain !"
        print(response)
        self.add_message(response, self.grandpy)
        print("-------------------------------")
        self.chat_viewer()
        print("-------------------------------")
        self.init_message()
        # ~ self.expiry_counter()

    #=================
    # attent question
    #=================
    def waiting_question(self):
        """
            waiting for user question
        """
        question = "Que veux tu savoir ... ?\n"
        self.add_message(question, self.grandpy)
        self.response_user(question)
        self.user_indecency()

    #=====================
    # stress of indecency
    #=====================
    def stress_indecency(self):
        """
            stress of Grandpy
        """
        response = "cette grossierete me FATIGUE ..."
        print(response)
        self.add_message(response, self.grandpy)
        self.reconnection()

    #==================
    # response grandpy
    #==================
    def answer_returned(self):
        """
            response returned by grandpy for the courteous user
        """
        response = "Voici Ta Réponse !"
        print(f"{response} : {self.tmp}")
        self.add_message(response, self.grandpy)

    #===============
    # response user
    #===============
    def response_user(self, question):
        """
            added last post from user
        """
        response = input(question)
        self.add_message(response, self.user)
        if self.civility:
            self.nb_request += 1

    #=============
    # rude answer
    #=============
    def rude_user(self):
        """
            rude user
        """
        question = "Si tu es grossier, je ne peux rien pour toi ... : \n"
        self.add_message(question, self.grandpy)
        self.response_user(question)
        self.user_indecency()

    #==============
    # Server Redis
    #==============
    def redis_connect(self):
        """
            connection to the Redis database
        """
        self.connect = redis.Redis(
            host="localhost",
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
                - write_indecency()   ==> default initialization of indecency values
                                          for the Redis database
                - write_counter()     ==> default initialization of counter values
                                          for the Redis database

        """
        self.write_civility(False)
        self.write_quotas(False)
        self.write_indecency(False)
        self.write_comprehension(True)
        self.write_counter(0)

    #==============================================
    # value of data Civility in the Redis database
    #==============================================
    def write_civility(self, civility):
        """
            saving of civility configuration in Redis database
        """
        self.writing("civility", bool_convers(civility))

    @property
    def read_civility(self):
        """
            reading of civility configuration in Redis database
        """
        return str_convers(self.reading("civility"))

    #============================================
    # value of data quotas in the Redis database
    #============================================
    def write_quotas(self, quotas):
        """
            saving of quotas configuration in Redis database
        """
        self.writing("quotas", bool_convers(quotas))

    @property
    def read_quotas(self):
        """
            reading of quotas configuration in Redis database
        """
        return str_convers(self.reading("quotas"))

    #===============================================
    # value of data Indecency in the Redis database
    #===============================================
    def write_indecency(self, indecency):
        """
            saving of indecency configuration in Redis database
        """
        self.writing("indecency", bool_convers(indecency))

    @property
    def read_indecency(self):
        """
            reading of indecency configuration in Redis database
        """
        return str_convers(self.reading("indecency"))

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
    def increment_counter(self):
        """
            Counter increment in Redis database
        """
        self.nb_request = self.incrementing("nb_request")

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

    #=================
    # user's civility
    #=================
    def user_civility(self):
        """
            modification of attributes civility
        """
        # list of words to find in questions
        user_answer = self.tmp.split()
        # search civility
        result = bool(
            [
            w for w in user_answer if w.lower() in self.DONNEE_CIVILITY
            ]
        )
        self.civility = result
        # ~ self.write_civility(self.civility)

    #=================
    # user's decency
    #=================
    def user_indecency(self):
        """
            modification of attributes indecency
        """
        # list of words to find in questions
        user_answer = self.tmp.split()
        # search indecency
        result = bool(
            [
            w for w in user_answer if w.lower() in self.INDECENCY_LIST
            ]
        )
        self.indecency = result
        # ~ self.write_indecency(self.indecency)

    #=========================
    # Grandpy incomprehension
    #=========================
    def comprehension(self):
    """
        modification of attributes decency
    """
        # list of words to find in questions
        list_question = self.question.split()
        # search comprehension
        result = bool(
            [
            w for w in list_question if w.lower() in self.DONNEE_CIVILITY
                                    and w.lower() in self.INDECENCY_LIST
                                    and w.lower() in self.UNNECESSARY_LIST
            ]
        )
        self.comprehension = result
        # ~ self.write_comprehension(self.comprehension)

#==================
# script execution
#==================
def main():
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    #---------------------------------
    # awaits the courtesy of the user
    #---------------------------------
    dialog = Chat()
    question = "Bonjour Mon petit, en quoi puis je t'aider ?\n"
    dialog.add_message(question, dialog.grandpy)
    dialog.response_user(question)
    dialog.user_civility()

    # rudeness of the user
    if not dialog.civility:
        while not dialog.civility and dialog.nb_request < 3:
            question = "Si tu es impoli, je ne peux rien pour toi ... : \n"
            dialog.add_message(question, dialog.grandpy)
            dialog.response_user(question)
            dialog.user_civility()

            if dialog.civility:
                dialog.nb_request -= 1
                if dialog.nb_request < 0:
                    dialog.nb_request = 0
            dialog.nb_request += 1

        # big stress of Grandpy because of incivility ==> back in 24 hours
        if dialog.nb_request >= 3:
            response = "cette impolitesse me FATIGUE ..."
            print(response)
            dialog.quotas = True
            print(dialog.nb_request)
            dialog.add_message(response, dialog.grandpy)
            dialog.reconnection()

    # Waits for user new question
    dialog.nb_request = 0
    while not dialog.quotas:
        # maximum number of responses reached
        if dialog.nb_request >= 10:
            dialog.quotas = True

        # Grandpy starts to tire
        if dialog.nb_request == 5:

            response = "Houla ma mémoire n'est plus ce qu'elle était ... "
            print(response)
            dialog.add_message(response, dialog.grandpy)
        # grandpy's reply
        print(dialog.nb_request)
        dialog.waiting_question()

        # indecency in response
        if dialog.indecency:
            while dialog.indecency and dialog.nb_indecency < 3:
                dialog.nb_indecency += 1
                dialog.indecency = False
                dialog.rude_user()

                if not dialog.indecency:
                    dialog.nb_request -= 1
                    if dialog.nb_request < 0:
                        dialog.nb_request = 0


                # big stress of Grandpy because of indecency ==> back in 24 hours
                if dialog.nb_indecency >= 3:
                    dialog.quotas = True
                    dialog.stress_indecency()
        else:
            dialog.answer_returned()

    if dialog.nb_request >= 10 and dialog.nb_indecency < 3:
        # grandpy exhaustion
        response = "cette séance de recherche me FATIGUE ..."
        print(response)
        dialog.add_message(response, dialog.grandpy)
        dialog.reconnection()

if __name__ == "__main__":
    main()



