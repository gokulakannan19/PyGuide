from django.db import models


class Account(models.Model):
    email = models.EmailField(null=True)
    name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now=True)


class Guide(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return self.question
