from django.db import models

# Create your models here.
PURPOSE_CHOICES = {
    ('get_answer', 'get_answer'),
    ('submit_answer', 'submit_answer')
}


class Account(models.Model):
    email = models.EmailField(default=True)
    name = models.CharField(max_length=100, default=True)
    purpose = models.CharField(
        max_length=30, choices=PURPOSE_CHOICES, default=True)


class Guide(models.Model):
    question = models.TextField()
    answer = models.TextField()
