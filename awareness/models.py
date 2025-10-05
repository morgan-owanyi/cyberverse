from django.db import models

# Create your models here.
from django.db import models

class modules(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    difficulty = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Beginner')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
