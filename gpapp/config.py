#coding:utf-8
#!/usr/bin/env python

def env_key(key_api):

    return {
        "Key_API_MAP": key_api[0],
        "Key_API_STATIC_MAP": key_api[1]
    }

class DefaultConf:
    """

    """

    LST_CIVILITY = [
        "bonjour grandpy","bonsoir grandpy","salut grandpy",
        "hello grandpy","bonjour grandPy comment vas tu",
        "comment allez vous grandpy","salut grandpy comment ca va"
        "bonjour", "bonsoir","salut","hello"
    ]
    LST_INDENCY = [
        "salut vieux","salut vieux con","salut vieux poussierieux",
        "salut ancetre demode","salut vieillard senille","salut dinosaure decrepit",
        "salut arriere rococo","salut centenaire senille","salut vieillot archaique",
        "salut vieux","salut vieux gateux","salut vieux croulant","salut antiquite",
        "salut vieille baderne","salut vieux fossile","bonjour vieux",
        "bonjour vieux con","bonjour vieux poussierieux","bonjour ancetre demode",
        "bonjour vieillard senille","bonjour dinosaure decrepit",
        "bonjour arriere rococo","bonjour centenaire senille",
        "bonjour vieillot archaique","bonjour vieux","bonjour vieux gateux",
        "bonjour vieux croulant","bonjour antiquite","bonjour vieille baderne",
        "bonjour vieux fossile","bonsoir vieux poussierieux","bonsoir ancetre demode",
        "bonsoir vieillard senille","bonsoir dinosaure decrepit",
        "bonsoir arriere rococo","bonsoir centenaire senille",
        "bonsoir vieillot archaique","bonsoir vieux","bonsoir vieux gateux",
        "bonsoir vieux croulant","bonsoir antiquite","bonsoir vieille baderne",
        "bonsoir vieux fossile","sale vieux","vieux con","vieux poussierieux",
        "ancetre demode","vieillard senille","dinosaure decrepit","arriere rococo",
        "centenaire senille","vieillot archaique","vieux gateux","vieux croulant",
        "antiquite","vieille baderne","vieux fossile"
    ]
    UNNECESSARY = [
        "a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait",
        "allaient","allo","allons","allô","alors","ancetre","ancetre demode",
        "anterieur","anterieure","anterieures","antiquite","apres","après",
        "arriere rococo","as","assez","attendu","au","aucun","aucune","aujourd",
        "aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi",
        "autre","autrefois","autrement","autres","autrui","aux","auxquelles",
        "auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant",
        "b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","Bonjour",
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
        "situe", "situé","six","sixième","soi","soi-même","soit","soixante","son",
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
    def __init__(self):

        self.over_quotas = False
        self.nb_request = 0
        self.civility = False
        self.decency = True
        self.comprehension = True

    @property
    def params(self):

        return {
            "over_quotas": self.over_quotas,
            "nb_request": self.nb_request,
            "politeness": {
                "civility": self.civility,
                "decency": self.decency
            },
            "comprehension": self.comprehension
        }

class DevConf():
    """

    """
    def __init__(self):
        self.Key_API_MAP = "Key_API_MAP"
        self.Key_API_STATIC_MAP = "Key_API_STATIC_MAP"

    @property
    def env_dev(self):

        return env_key((self.Key_API_MAP, self.Key_API_STATIC_MAP))

class TestingConf():
    """

    """
    def __init__(self):

        self.demand = "ou est situé le restaurant la_nappe_d_or de lyon"
        self.parsed = ["restaurant","la_nappe_d_or","lyon"]
        self.placeId = "ChIJTei4rhlu5kcRPivTUjAg1RU"
        self.geoPlaceId = {
            'candidates': [{
                'place_id': "ChIJTei4rhlu5kcRPivTUjAg1RU"
            }]
        }
        self.address = "16 Rue Étienne Marcel, 75002 Paris, France"
        self.question = "ou se trouve la poste de marseille"
        self.addressPlace = "paris poste"
        self.formatAddress = {
            'result': {
                'formatted_address': "16 Rue Étienne Marcel, 75002 Paris, France"
            }
        }

        self.history = [[
            """
                Riche d'un long passé artistique, ce secteur de Paris (France)
                dominé par la Basilique du Sacré-Cœur a toujours été le symbole
                d'un mode de vie bohème où, de Picasso à Modigliani, de nombreux artistes
                trouvèrent refuge.
            """
        ]]

    @property
    def test_data(self):

        return {
            "demand": self.demand,
            "parsed": self.parsed,
            "placeId": self.placeId,
            "geoPlaceId": self.geoPlaceId,
            "address": self.address,
            "question": self.question,
            "addressPlace": self.addressPlace,
            "formatAddress": self.formatAddress,
            "history": self.history
        }


class ProdConf():
    """

    """
    def __init__(self):

        self.Key_API_MAP = "HEROKU_KEY_API_MAP"
        self.Key_API_STATIC_MAP = "HEROKU_KEY_API_STATIC_MAP"

    @property
    def env_dev(self):

        return env_key((self.Key_API_MAP, self.Key_API_STATIC_MAP))

class parameter :
    """

    """
    def __init__(self):

        self.baseConfig = DefaultConf()
        self.varConfig = DefaultConf
        self.developmentConfig = DevConf()
        self.productionConfig = ProdConf()
        self.testingConfig = TestingConf()

    @property
    def base(self):
        return self.baseConfig

    @property
    def constant(self):
        return self.varConfig

    @property
    def default(self):
        return self.developmentConfig

    @property
    def production(self):
        return self.productionConfig

    @property
    def testing(self):
        return self.testingConfig
