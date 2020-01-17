#coding:utf-8
#!/usr/bin/env python

import os

class VarConf:
    """
        API Private Key and Constants Management class:
            local (development)
                - KEY_API_MAP
                - KEY_API_STATIC_MAP
            external (production)
                - HEROKU_KEY_API_MAP
                - HEROKU_KEY_API_STATIC_MAP
            - USABLE_LST
                - civility list
                - list for indecency
                - word list not necessary
    """
    USABLE_LIST = [
        [ # CIVILITY LIST
            "bonjour grandpy","bonsoir grandpy","salut grandpy",
            "hello grandpy","bonjour grandPy comment vas tu",
            "comment allez vous grandpy","salut grandpy comment ca va"
            "bonjour", "bonsoir","salut","hello"
        ],
        [ # INDECENCY LIST
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
        ],
        [ # UNNECESSARY LIST
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
    ]
    MAP = "KEY_API_MAP"
    STATIC_MAP = "KEY_API_STATIC_MAP"
    HEROKU_MAP = "HEROKU_KEY_API_MAP"
    HEROKU_STATIC_MAP = "HEROKU_KEY_API_STATIC_MAP"

    @classmethod
    def var_env(cls):
        data = {
            "KEY_API_MAP": cls.MAP,
            "KEY_API_STATIC_MAP": cls.STATIC_MAP,
            "HEROKU_KEY_API_MAP": cls.HEROKU_MAP,
            "HEROKU_KEY_API_STATIC_MAP": cls.HEROKU_STATIC_MAP
        }
        return data

class Parameter:
    """
        Parameter Call Management Class:
            - constant ==> call to constants
            - status_env ==> call of private keys (local / external)
    """
    DATACONFIG = VarConf
    VARSCONFIG = VarConf()

    @classmethod
    def constant(cls):
        data = {
            "list_civility": cls.DATACONFIG.USABLE_LIST[0],
            "list_indecency": cls.DATACONFIG.USABLE_LIST[1],
            "list_unnecessary": cls.DATACONFIG.USABLE_LIST[2]
        }
        return data

    @classmethod
    def status_env(cls):
        if os.environ.get("HEROKU_KEY_API_MAP") is None:
            default = {
                "map": os.getenv(cls.VARSCONFIG.var_env()["KEY_API_MAP"]),
                "staticMap": os.getenv(cls.VARSCONFIG.var_env()["KEY_API_STATIC_MAP"]),
                "status_prod": False
            }
            return default
        else:
            prod = {
                "map": os.getenv(cls.VARSCONFIG.var_env()["HEROKU_KEY_API_MAP"]),
                "staticMap": os.getenv(cls.VARSCONFIG.var_env()["HEROKU_KEY_API_STATIC_MAP"]),
                "status_prod": True
            }
            return prod

if __name__ == "__main__":
   pass
