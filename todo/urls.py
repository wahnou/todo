from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

html_patterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', include(html_patterns)),
]
