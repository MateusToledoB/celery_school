from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.name
