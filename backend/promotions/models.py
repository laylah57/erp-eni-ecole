from django.db import models
from django.contrib.auth.models import User

class Filiere(models.Model):

    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):

        return self.nom

class Cursus(models.Model):

    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    Filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='cursus')

    def __str__(self):

        return self.nom
class Cours(models.Model):

    titre = models.CharField(max_length=255)
    technologie = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):

        return self.nom      

class CursusCours(models.Model):

    cursus = models.ForeignKey(Cursus, on_delete=models.CASCADE, related_name='cursus_cours')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    ordre = models.PositiveIntegerField()
    obligatoire = models.BooleanField(default=True)

    class Meta:

        unique_together = ('cursus', 'cours')
        constraints = [
           models.UniqueConstraint(fields=['cursus', 'ordre'], name='unique_cursus_ordre')
        ]
        ordering = ['ordre']


class Promotion(models.Model):



    nom = models.CharField(max_length=100)



    date_debut = models.DateField()



    date_fin = models.DateField()



    def __str__(self):



        return self.nom



class Inscription(models.Model):



    utilisateur = models.ForeignKey(



        User,



        on_delete=models.CASCADE



    )



    promotion = models.ForeignKey(



        Promotion,



        on_delete=models.CASCADE,



        related_name='inscriptions'



    )



    date_inscription = models.DateField()



    forcee = models.BooleanField(default=False)



    def __str__(self):



        return f"{self.utilisateur.username} - {self.promotion.nom}"

