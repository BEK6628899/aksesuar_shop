from django.db import models
from django.contrib.auth.models import User

class AsosiySahifa(models.Model):
    rasm = models.FileField()
    nom = models.CharField(max_length=50)
    narx = models.FloatField()
    malumot = models.CharField(max_length=300, null=True, blank=True)
    rang = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.nom


class Telefonlar(models.Model):
    AsosiySahifa = models.ForeignKey(AsosiySahifa, on_delete=models.CASCADE)
    def __str__(self):
        return self.AsosiySahifa.nom



class Soatlar(models.Model):
    AsosiySahifa = models.ForeignKey(AsosiySahifa, on_delete=models.CASCADE)
    def __str__(self):
        return self.AsosiySahifa.nom



class BoshqaMahsulotlar(models.Model):
    AsosiySahifa = models.ForeignKey(AsosiySahifa, on_delete=models.CASCADE)
    def __str__(self):
        return self.AsosiySahifa.nom



class WebSahifalar(models.Model):
    rasm = models.FileField()
    nom = models.CharField(max_length=30)
    matn = models.CharField(max_length=200)
    def __str__(self):
        return self.nom



class SignUp(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.email




