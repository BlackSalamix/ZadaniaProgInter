from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='taskboard_index'), 
    path('api/tasks/', views.api_tasks),           
    path('api/tasks/<int:task_id>/', views.api_task_detail), 
]