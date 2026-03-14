from django.db import models
from django.contrib.auth.models import User


class Yoga(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")
    level = models.CharField(
        max_length=20,
        choices=[
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced'),
        ],
        default='Beginner'
    )

    image = models.ImageField(upload_to='yoga_images/', blank=True, null=True)

    def __str__(self):
        return self.title



class Meditation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")

    image = models.ImageField(upload_to='meditation_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Mood(models.Model):
    MOOD_CHOICES = [
        ('Happy', 'Happy'),
        ('Calm', 'Calm'),
        ('Stressed', 'Stressed'),
        ('Anxious', 'Anxious'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    note = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood} ({self.date})"
