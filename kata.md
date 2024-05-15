# Kata Django : Application de Gestion de Tâches (To-Do List)

 

## Objectif

Créer une application Django pour gérer une liste de tâches. L'application doit permettre de :

1. Créer une tâche✔️

2. Mettre à jour une tâche✔️

3. Supprimer une tâche✔️

4. Afficher la liste des tâches✔️

5. Fournir une API REST pour les opérations CRUD sur les tâches✔️

 

## Exigences

 

### Modèle de Données

Créer un modèle `Task` avec les champs suivants :

- `title` (CharField) : Le titre de la tâche✔️

- `description` (TextField) : Une description de la tâche✔️

- `completed` (BooleanField) : Un indicateur pour savoir si la tâche est complétée✔️

 

### Vue et Templates

1. Créer une vue pour afficher la liste des tâches.✔️

2. Créer un formulaire pour ajouter une nouvelle tâche.✔️

3. Créer une vue pour mettre à jour une tâche existante.✔️

4. Créer une vue pour supprimer une tâche.✔️

 

### API REST

Utiliser Django REST Framework pour créer une API permettant de :

1. Récupérer la liste des tâches✔️

2. Récupérer les détails d'une tâche✔️

3. Créer une nouvelle tâche✔️

4. Mettre à jour une tâche existante✔️

5. Supprimer une tâche✔️

 

## Instructions

 

### Installation et Configuration de Base

- Créez un nouveau projet Django.✔️

- Configurez une nouvelle application Django nommée `todo`.✔️

 

### Modèle `Task`

Créez un modèle `Task` dans `models.py` de l'application `todo` avec les champs mentionnés.✔️

 

### Formulaires et Vues

- Créez des vues pour afficher la liste des tâches, ajouter, mettre à jour et supprimer des tâches.✔️

- Utilisez des templates HTML pour les formulaires et les listes de tâches.✔️

 

### API REST

- Installez Django REST Framework et configurez-le dans le projet.✔️

- Créez des serializers pour le modèle `Task`.✔️

- Créez des vues API utilisant les viewsets de DRF pour les opérations CRUD.✔️

 

### Tests

- Écrivez des tests unitaires pour vérifier les fonctionnalités des vues et de l'API.✔️

 

## Livrables

 

1. Le code source du projet Django avec les fonctionnalités demandées.✔️

2. Des instructions claires sur la façon d'installer et de faire fonctionner l'application.✔️

3. Un fichier README décrivant le projet et les étapes pour le configurer et le tester.✔️

 

hicham.maaqoul@gmail.com
hmaaqoul@sqli.com
0662542015