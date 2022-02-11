from django.urls import path
from .views import all_learning_paths, lp_detail

app_name = "learningpaths"

urlpatterns = [
    path('', all_learning_paths, name="all_learning_paths"),
    path('learningpath/<int:pk>/', lp_detail, name="lp_detail"),
]
