from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.teachers, name='teachers'),
    path('create_quiz/<int:teacher_id>/', views.create_quiz, name='create_quiz'),
    path('test/<int:test_id>/', views.test, name='test'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('add_questions/<int:Test_id>/', views.add_questions, name='add_questions'),
]
