# projet7
question Réponses avec GrandPy
------------------------------

### Configuration du projet pour une utilisation locale

#### pour utiliser la clé privé de l'API de Google Map de maniére sécurisé

créer une premiere variable d'environnement  nommée : **key_API_MAP** ,

puis une seconde nommée : **key_API_STATIC_MAP** dans l'environnement virtuel

avec votre editeur de texte préféré ouvrez le script **activate** qui dans le repertoire  **<venv>/bin/**

situé à la racine du projet dans le cas ou votre systeme soit sur une **base UNIX (linux / MAC)**

ou ouvrez le script **activate.bat** dans le repertoire **c:\venv\Scripts\** pour un systeme basé sur windows

inserez les lignes : `export <key_API>="<CLE_PRIVE_DE_L'API>"`

entre la ligne `VIRTUAL_ENV ="/.../..."`

et la ligne `export VIRTUAL_ENV`

comme indique ci dessous :

`VIRTUAL_ENV="/.../..."`

`export key_API_MAP="<VOTRE_CLE_PRIVE>"`

`export key_API_STATIC_MAP="<VOTRE_CLE_PRIVE>"`

`export VIRTUAL_ENV`


#### pour utiliser correctement le module du projet pendant les tests (pytest)

Ajouter le module gpapp dans PYTHONPATH

inserez la ligne : `export PYTHONPATH=${PYTHONPATH}:${HOME/..../}/<NOM DU MODULE DU PROJET>`

entre la ligne `PATH="$VIRTUAL_ENV/bin:$PATH"`

et la ligne `export PATH`

comme indique ci dessous :

`PATH="$VIRTUAL_ENV/bin:$PATH"`

`export PYTHONPATH=${PYTHONPATH}:${HOME/...<REPERTOIRE DU PROJET>.../}/<NOM DU MODULE DU PROJET>`

`export PATH`

Sauvegarder le script et ça en est finit pour la configuration locale !

Cela à pour effet de récuperer les variables d'environnements contenant les clé

privés des differentes APIS à chaque activation de l'environnement virtuel
