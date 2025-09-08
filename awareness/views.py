from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def modules(request):
    return render(request, 'modules.html')

def quizzes(request):
    return render(request, 'quizzes.html')

def resources(request):
    return render(request, 'resources.html')

def feedback(request):
    return render(request, 'feedback.html')

def impact(request):
    return render(request, 'impact.html')            