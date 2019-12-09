#coding:utf-8
#!/usr/bin/env python

import os
import json

import urllib.request, urllib.parse

#==============================
# Word list to parse
#==============================
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

#==============================
# environment variable
#==============================
def var_env():
    """
        call function of the Key_API_MAP / key_API_STATIC_MAP
        environments variables (API key)
    """
    api_key = {
        "map": "",
        "staticMap": ""
        # ~ "map": os.getenv("key_API_MAP"),
        # ~ "staticMap": os.getenv("key_API_STATIC_MAP")
    }
    if ((
            os.environ.get("HEROKU_KEY_API_STATIC_MAP") is None
            ) and (os.environ.get("HEROKU_KEY_API_MAP") is None)):
        api_key["map"] = os.getenv("key_API_MAP")
        api_key["staticMap"] = os.getenv("key_API_STATIC_MAP")
    else:
        vars = os.environ["HEROKU_kEY_API_MAP"]
        vars2 = os.environ["HEROKU_kEY_API_STATIC_MAP"]
        api_key["map"] = vars
        api_key["staticMap"] = vars2

    return api_key

#==============================
# parser
#==============================
def parser(question="ou se trouve la poste de marseille"):
    """
        function that cuts the string of characters (question asked to GrandPy)
        into a word list then delete all unnecessary words to keep only
        the keywords for the search
    """
    global UNNECESSARY
    unnecessary = UNNECESSARY

    # list of words to remove in questions
    list_question = question.split()
    result = [w for w in list_question if w.lower() not in unnecessary]

    return result

#------------------------
# place_id search on Google Map API
def get_place_id_list(address="paris poste"):
    """
        Google map API place_id search function
    """

    key = var_env()["map"] # environment variable

    # replacing space by "% 20" in the string of characters
    address_encode = urllib.parse.quote(address)

    place_id = urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/"\
        +f"json?input={address_encode}&inputtype=textquery&key={key}"
    )

    result = json.loads(place_id.read().decode("utf8"))

    return result

#------------------------
# place_id search on Google Map API
def get_address(place_id="ChIJTei4rhlu5kcRPivTUjAg1RU"):
    """
        Google map API address search with place_id function
    """

    key = var_env()["map"] # environment variable

    address_found= urllib.request.urlopen(
        "https://maps.googleapis.com/maps/api/place/details/"\
        f"json?placeid={place_id}&fields=formatted_address,geometry&key={key}"
    )

    result = json.loads(address_found.read().decode("utf8"))

    return result

#------------------------
# history search on wikimedia API
def get_history(search_history="montmartre"):
    """
        wikipedia API (Wikimedia) history search
    """

    # replacing space by "% 20" in the string of characters
    history_encode = urllib.parse.quote(search_history)

    history_found= urllib.request.urlopen(
        "https://fr.wikipedia.org/w/api.php?"\
        f"action=opensearch&search={history_encode}&format=json"
    )

    result = json.loads(history_found.read().decode("utf8"))

    return result

#------------------------
# map display in the Google Map Satic API
def get_map_static(location_map):
    """
        function of displaying the geolocation of the address
        asked to grandpy on the map of the Google Map Static API
    """
    key = var_env()["staticMap"]  # environment variable

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


if __name__ == "__main__":
    pass
