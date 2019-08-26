from django.db import models


class Student(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class Contact(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)
    subject = models.TextField(max_length=300)

    def __str__(self):
        return self.name
