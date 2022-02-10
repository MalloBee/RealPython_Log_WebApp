from django.urls import path
from .views import all_learning_paths

urlpatterns = [
    path('', all_learning_paths)
]