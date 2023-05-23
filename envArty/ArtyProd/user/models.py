from datetime import date
from django.db import models

from django.contrib.auth.models import User


class Detail(models.Model):
    ficher = models.FileField(upload_to='uploads/', max_length=255)

    def __str__(self):
        return self.ficher.name


class Service(models.Model):
    types = [
        ('DG', 'Design Graphique'),
        ('PA', 'Production Audiovisuelle'),
        ('3D', 'Conception 3D')
    ]
    type = models.CharField(max_length=255, choices=types, default='3D')
    description = models.TextField(null=True)
    details = models.ForeignKey('Detail', on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class Personnel(models.Model):

    nom = models.CharField(max_length=255, null=True)
    ficher_CV = models.FileField(
        upload_to='uploads/', max_length=255, null=True)
    ficher_photo = models.ImageField(
        upload_to='media/', max_length=255, null=True)
    lien_linkedln = models.URLField()

    def __str__(self):
        return " "+self.nom+" "+self.lien_linkedln


class Equipe(models.Model):
    nom = models.CharField(max_length=255, null=True)
    personnels = models.ManyToManyField(Personnel)

    def __str__(self):
        personnel_list = ", ".join(
            personnel.nom for personnel in self.personnels.all())
        i = self.id
        return f"Equipe {i} : ({personnel_list})"


class Projet(models.Model):
    acheve = [
        ('o', 'Oui'),
        ('n', 'Non')
    ]
    libellai = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img_projet = models.ImageField(
        upload_to='media/', max_length=255, null=True)
    date_debut =models.DateField(null=True, default=date.today)

    date_fin = models.DateField()
    acheve = models.CharField(max_length=255, choices=acheve, default='o')
    Service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    equipe = models.OneToOneField(Equipe, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return " "+self.libellai+" "+str(self.date_fin)+" "+str(self.acheve)


class ProjetUtilisateur(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    projet = models.ManyToManyField(Projet)

    def __str__(self):
        return " "+self.libellai+" "+str(self.date_fin)+" "+str(self.utilisateur.username)
