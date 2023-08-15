# Application web - Développé en utilisant Django
Projet n°9 - Développez une application Web en utilisant Django

Auteur : Ciran GÜRBÜZ

Date : Août 2023

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Présentation du programme

Cette application est un site web de revues littéraires (articles ou livres).
Un utilisateur peut demander une critique (ticket) à propos d'une revue ou écrire une critique sur le ticket d'un autre utilisateur.
L'application présente également un système d'abonnements entre utilisateurs.


Après avoir téléchargé le contenu du repository, veuillez l'extraire dans un dossier spécifique sur votre ordinateur. 
Ensuite, suivez ces étapes dans l'ordre afin de faire fonctionner le programme.

## 1 - Installation des logiciels requis

### 1.1 - Python

Cette application a été développée en utilisant la version 3.11 de Python que vous pourrez retrouver sur le site officiel de Python : https://www.python.org/downloads/


### 1.2 - Création et activation de l'environnement virtuel

#### a) Ouvrir un terminal de commande et se placer dans le dossier contenant les fichiers du repository.
#### b) Créer l'environnement virtuel avec la ligne de commande suivante : 
```python -m venv "env"```
#### c) Activer l'environnement virtuel avec la ligne de commande suivante : 
```env/Scripts/activate```


### 1.3 - Installation des packages

#### a) Une fois l'environnement virtuel activé, installer les packages avec la commande suivante : 
```pip install -r requirements.txt```


## 2 - Lancement du serveur

#### Toujours dans le dossier contenant les fichiers du repository, veuillez démarrer le serveur avec la commande suivante :
```python manage.py runserver```


## 3 - Accès au site web

#### Une fois le serveur démarré, vous pourrez accéder au site via l'adresse suivante : ```http://127.0.0.1:8000/```


## 4 - Comptes pré-existants

#### Voici une liste d'utilisateurs créés à titre d'illustration : 
```
Login : Maxime50 - MDP : maxoumaxou << Compte principal
Login : Julie_best - MDP : bestoubest
Login : Bob-éponge - MDP : bobbybob
Login : patrick-létoile - MDP : etoiledufutur
```


## 5 - Compte administrateur

#### Vous pouvez accéder à l'interface administrateur de Django à l'adresse et avec les identifiants suivants : 
```
http://127.0.0.1:8000/admin
Login : admin - MDP : admin
```



Bonne visite !

