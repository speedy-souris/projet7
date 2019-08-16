# projet7
question Réponses avec GrandPy
------------------------------

### Configuration du projet pour une utilisation locale
#### pour utiliser la clé privé de l'API de Google Map de maniére sécurisé

créer une variable d'environnement  nommée : **key_API_MAP** dans l'environnement virtuel

avec votre editeur de texte préféré ouvrez le script **activate** qui dans le repertoire  **venv/bin/**

situé à la racine du projet dans le cas ou votre systeme soit sur une **base UNIX (linux / MAC)**

ou ouvrez le script **activate.bat** dans le repertoire **c:\venv\Scripts\** pour un systeme basé sur windows

inserez la ligne : `export key_API_MAP="<CLE_PRIVE_DE_L'API>"`

entre la ligne `VIRTUAL_ENV ="/.../..."`

et la ligne `export VIRTUAL_ENV`

comme indique ci dessous :

`VIRTUAL_ENV="/.../..."`

`export key_API_MAP="<VOTRE_CLE_PRIVE>"`

`export VIRTUAL_ENV`

Sauvegarder le script et ça en est finit pour la configuration locale !

Cela à pour effet de récuperer la variable d'environnement contenant la clé

privé de l'API Google Map à chaque activation de l'environnement virtuel


