# projet7
question Réponses avec GrandPy
------------------------------

Le projet se compose d'une page web qui affiche un jeu de question / réponse
les demandes sont faites à un papy robot via un formulaire
les réponses données par le robot utilise plusieurs APIS de google
a savoir l'**API Google Map** et l'**API Google Map Static**

Le serveur local utiliser pour developper le projet est **FLASK**
python est là pour le langage serveur et javascript pour le langage client

Le serveur web pour deployer l'application est le cloud **Heroku** avec la dependance **GUNICORN**
pour gérer le langage python
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

Cela à pour effet de récuperer les variables d'environnements contenant les clé

privés des differentes APIS à chaque activation de l'environnement virtuel

Sauvegarder le script et ça en est finit pour la configuration locale !

### Configuration du projet pour une utilisation en Production avec le cloud **HEROKU**
Ajouter le serveur web **gunicorn** dans python (pip install gunicor)

Créer le fichier requirements.txt (liste des librairie installer dans python)

Créer le fichier Procfile pour utiliser python sur le cloud

Dans les variables d'environement du cloud **HEROKU**,

créer une premiere variable d'environnement  nommée : **HEROKU_KEY_API_MAP**

puis une seconde nommée : **HEROKU_KEY_API_STATIC_MAP**

### Dans une console:

heroku login pour lancer l'application **HEROKU** (projet creer pour l'occasion)

`heroku config:set HEROKU_KEY_API_MAP=<MA PREMIERE CLE API>` pour creer ma premiere variable

`heroku config:set HEROKU_KEY_API_STATIC_MAP=<MA DEUXIEME CLE API>` pour la deuxieme

Ensuite faire un `git push origin master` pour sauvegarder le script sur github

et pour finir `git push heroku master` pour mettre en ligne votre application




