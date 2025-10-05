from django.shortcuts import render
from awareness.models import Tutorial

# Create your views here.

def home(request):
    return render(request, 'home.html')
                


def modules(request):
    modules_list = [
        {
            "title": "Phishing Awareness",
            "description": "Learn how to spot phishing emails and fake websites.",
            "difficulty": "Beginner",
            "link": "https://www.cisa.gov/news-events/news/stop-think-connect-phishing-awareness"
        },
        {
            "title": "Password Security",
            "description": "Best practices for creating and managing secure passwords.",
            "difficulty": "Beginner",
            "link": "https://www.ncsc.gov.uk/collection/top-tips-for-staying-secure-online/passwords"
        },
        {
            "title": "Malware Basics",
            "description": "Understand how malware works and how to defend against it.",
            "difficulty": "Intermediate",
            "link": "https://us.norton.com/blog/malware/what-is-malware"
        },
        {
            "title": "Safe Browsing",
            "description": "Tips for avoiding malicious websites and online scams.",
            "difficulty": "Beginner",
            "link": "https://staysafeonline.org/resources/online-safety-privacy-basics/"
        },
    ]
    return render(request, "modules.html", {"modules": modules_list})



from django.shortcuts import render

def quizzes(request):
    quizzes_list = [
        {
            "question": "Which of the following is the safest way to create a password?",
            "options": ["Use 'password123'", "Use a random combination of letters, numbers, symbols", "Use your birthdate", "Use your pet's name"],
            "answer": 1  # index of the correct option
        },
        {
            "question": "What is phishing?",
            "options": ["A type of malware", "A social engineering attack to steal information", "A firewall setting", "A secure website"],
            "answer": 1
        },
        {
            "question": "Which HTTPS indicates?",
            "options": ["Website is on fire", "Website is using SSL/TLS encryption", "Website is unsafe", "Website is owned by Google"],
            "answer": 1
        },
    ]

    score = None
    total = len(quizzes_list)

    if request.method == "POST":
        score = 0
        for i, quiz in enumerate(quizzes_list):
            selected = request.POST.get(f"q{i}")
            if selected is not None and int(selected) == quiz['answer']:
                score += 1

    return render(request, "quizzes.html", {"quizzes": quizzes_list, "score": score, "total": total})


def resources(request):
    return render(request, 'resources.html')

def feedback(request):
    return render(request, 'feedback.html')

def impact(request):
    return render(request, 'impact.html')          

def tutorial_list(request):
    tutorials = Tutorial.objects.all().order_by('-created_at')
    return render(request, 'awareness/tutorial_list.html', {'tutorials': tutorials})  