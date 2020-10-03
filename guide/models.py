from django.db import models


class Account(models.Model):
    email = models.EmailField(null=True)
    name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now=True)


class Question(models.Model):
    s_no = models.PositiveIntegerField(null=True)
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Answer(models.Model):
    s_no = models.PositiveIntegerField(null=True)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer
