# Application de Gestion de Tâches (To-Do List)

## Configuration

Accédez au dossier de l'application via votre terminal et suivez les étapes suivantes:
1. Commencez par installer les dépendances nécessaires:
```
pip install -r requirements.txt
```

2. Lancez les migrations:
```
python manage.py makemigrations
python manage.py migrate
```

3. Lancer l'application:
```
python manage.py runserver
```

## Fonctionnement

L'application devrait être accessible via votre navigateur (souvent à l'address: http://127.0.0.1:8000/).

Cliquez sur le bouton "ajouter", pour ajouter votre première tâche

## API
Les endpoints de l'API sont les suivants:

| Fonction              | Méthode       | URL                       |
| -------------         | ------------- | -------------             |
| Liste des tache       | GET           | /api/v1/tasks/            |
| Detail d'un tache     | GET           | /api/v1/tasks/{id_tache}/ |
| Ajouter une tache     | POST          | /api/v1/tasks/            |
| Supprimer une tache   | DELETE        | /api/v1/tasks/{id_tache}/ |
| Modifier une tache    | UPDATE        | /api/v1/tasks/{id_tache}/ |


## Tests
Pour lancer les tests unitaires des vues et de l'API, executez:
```
pip install -r .\requirements.txt
```