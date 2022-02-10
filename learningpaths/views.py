from django.shortcuts import render
from .models import LearningPath

# Create your views here.
def all_learning_paths(request):
    lps = LearningPath.objects.all()
    return render(request,
                  "learningpaths/index.html",
                  {'learning_paths': lps},
                  )