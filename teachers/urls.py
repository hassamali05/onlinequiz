from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:test_id>/', views.test, name='test')
]
