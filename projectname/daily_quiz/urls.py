from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_index, name='daily_index'),
    path('add-question/', views.add_question, name='add_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
]