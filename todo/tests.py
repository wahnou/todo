from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskViewsTestCase(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(title='Tâche 1', description='Description Tâche 1', completed=False)
        self.task2 = Task.objects.create(title='Tâche 2', description='Description Tâche 2', completed=True)

    def test_task_list_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.task1.title)
        self.assertContains(response, self.task2.title)

    def test_task_detail_view(self):
        response = self.client.get(reverse('task-detail', kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Tâche 1')

    def test_task_create_view(self):
        data = {'title': 'Nouvelle tâche', 'description': 'Description de la Nouvelle tâche', 'completed': False}
        response = self.client.post(reverse('task-create'), data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertTrue(Task.objects.filter(title='Nouvelle tâche').exists())

    def test_task_update_view(self):
        data = {'title': 'Tâche modifiée', 'description': 'Description de la Nouvelle tâche', 'completed': True}
        response = self.client.post(reverse('task-update', kwargs={'pk': self.task1.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Task.objects.get(pk=self.task1.pk).title, 'Tâche modifiée')

    def test_task_delete_view(self):
        response = self.client.delete(reverse('task-delete', kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertFalse(Task.objects.filter(pk=self.task1.pk).exists())

class TaskAPITestCase(TestCase):
    # Création de données de test
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(title='Tâche 1', description='Description Tâche 1', completed=False)
        self.task2 = Task.objects.create(title='Tâche 2', description='Description Tâche 2', completed=True)

    # Vérfier le nombre de tâche
    def test_task_list_api(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Vérfier l'existance d'une tâche
    def test_task_detail_api(self):
        response = self.client.get('/api/v1/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Tâche 1')

    # Vérfier la création d'une tâche
    def test_task_create_api(self):
        data = {'title': 'Nouvelle tâche', 'description': 'Description de la Nouvelle tâche', 'completed': False}
        response = self.client.post('/api/v1/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Task.objects.filter(title='Nouvelle tâche').exists())
    
    # Vérfier la modification d'une tâche
    def test_task_update_api(self):
        data = {'title': 'Tâche modifiée', 'description': 'Description de la Nouvelle tâche', 'completed': True}
        response = self.client.put('/api/v1/tasks/2/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Task.objects.filter(title='Tâche modifiée').exists())
    
    # Vérfier la supression d'une tâche
    def test_task_delete_api(self):
        response = self.client.delete('/api/v1/tasks/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Task.objects.filter(pk=self.task2.pk).exists())