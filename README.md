# ji_parrainage
plateforme de présentation de la cérémonie de parrainage JI 2022

## Installation
### Activer l'environnement virtuel
une fois le projet cloné, renommer-le et ouvrer le dans un terminal <br>
Les environnements virtuels sont les endroits où les dépendances sont stockées, similaires aux node_modules en JavaScript. Chaque fois que vous démarrez votre machine, vous devez activer l'environnement virtuel à l'aide de la commande suivante
##### Mac Os

```bash
source venv/bin/activate
```
##### Windows

```bash
env\Scripts\activate
```
## Installez les dépendences

```bash
pip install -r requirements.txt
```
## Base de Données
###### n'oublier pas de modifier le nom de la base de donnée et le mot de passe de connexion à la bd.
Creer une base de donnée, nommer-le comme vous voulez.
en suite dans le dossier *ji_sponsordhip* ouvrez le fichier *settings.py* reseigner les information de connexion à la base de donnée comme suit :
```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ji_parrainnage', # nom de la bd
        'USER': 'root', # user
        'PASSWORD': '', # mot de passe
        'PORT': '3306',
        'HOST': 'localhost' # le host
    }
}
```
## Faites les migrations
dans votre terminal tapez :

```bash
python manage.py makemigrations

python manage.py migrate
```
## Créez un nouveau superutilisateur pour l'admin

```bash
python manage.py createsuperuser
```
## Vérifications finales
Démarrez le serveur de développement et assurez-vous que tout fonctionne sans erreur.
dans votre terminal tapez

```bash
python manage.py runserver
```
##### dans votre navigateur entrer : http://127.0.0.1:8000/admin/ <br> renseigner les identifiant du superuser creé précédenment