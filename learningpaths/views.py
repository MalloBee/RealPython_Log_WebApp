from django.shortcuts import render
from .models import LearningPath, Course


# Create your views here.
def all_learning_paths(request):
    lps = LearningPath.objects.values()
    for lp in lps:
        courses = Course.objects.values("complete").filter(learning_path=lp["id"])
        completed = [item['complete'] for item in courses].count(True)
        lp["progression"] = completed / len(courses) * 100
    return render(request,
                  "learningpaths/index.html",
                  {'learning_paths': lps, },
                  )

def lp_detail(request, pk):
    title = LearningPath.objects.get(pk=pk)
    courses = Course.objects.filter(learning_path=pk)
    return render(request,
                  "learningpaths/lp_detail.html",
                  {"title": title,
                  "courses": courses})

