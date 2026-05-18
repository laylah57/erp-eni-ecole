from django.db import models


from django.contrib.auth.models import User


class Promotion(models.Model):

    nom = models.CharField(max_length=100)

    date_debut = models.DateField()

    date_fin = models.DateField()

    def __str__(self):

        return self.nom


class Inscription(models.Model):

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    promotion = models.ForeignKey(
        Promotion, on_delete=models.CASCADE, related_name="inscriptions"
    )

    date_inscription = models.DateField()

    forcee = models.BooleanField(default=False)

    def __str__(self):

        return f"{self.utilisateur.username} - {self.promotion.nom}"
