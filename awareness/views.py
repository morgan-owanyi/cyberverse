from django.shortcuts import render
from awareness.models import modules

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


from django.shortcuts import render

def resources(request):
    resources_list = [
        {
            "title": "TryHackMe",
            "description": "An online platform that teaches cybersecurity through interactive hands-on labs.",
            "link": "https://tryhackme.com",
        },
        {
            "title": "Hack The Box",
            "description": "A penetration testing lab and cybersecurity training platform.",
            "link": "https://www.hackthebox.com",
        },
        {
            "title": "OWASP Top 10",
            "description": "A list of the most critical web application security risks maintained by OWASP.",
            "link": "https://owasp.org/www-project-top-ten/",
        },
        {
            "title": "Cybersecurity & Infrastructure Security Agency (CISA)",
            "description": "Official U.S. government cybersecurity tips and resources.",
            "link": "https://www.cisa.gov/",
        },
        {
            "title": "Google Phishing Quiz",
            "description": "A fun and interactive way to test your ability to spot phishing emails.",
            "link": "https://phishingquiz.withgoogle.com/",
        },
        {
            "title": "PortSwigger Web Security Academy",
            "description": "Free web security learning platform by the creators of Burp Suite.",
            "link": "https://portswigger.net/web-security",
        },
        {
            "title": "Cybrary",
            "description": "Free and paid online cybersecurity courses for all levels.",
            "link": "https://www.cybrary.it/",
        },
    ]

    return render(request, "resources.html", {"resources": resources_list})


from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "feedback.html", {
                "form": FeedbackForm(),
                "success": True
            })
    else:
        form = FeedbackForm()
    return render(request, "feedback.html", {"form": form})


def about(request):
    return render(request, 'about.html')

 