from rest_framework import status
from rest_framework.test import APITestCase

from .models import Filiere, Cursus, Cours, CursusCours


class PedagogieApiTests(APITestCase):

    def test_create_filiere(self):
        data = {
            "nom": "Développement",
            "description": "Filière liée au développement web et logiciel"
        }

        response = self.client.post("/api/filieres/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Filiere.objects.count(), 1)
        self.assertEqual(Filiere.objects.first().nom, "Développement")

    def test_create_cursus(self):
        filiere = Filiere.objects.create(
            nom="Développement",
            description="Filière liée au développement"
        )

        data = {
            "nom": "DWWM",
            "description": "Développeur Web et Web Mobile",
            "filiere": filiere.id
        }

        response = self.client.post("/api/cursus/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cursus.objects.count(), 1)
        self.assertEqual(Cursus.objects.first().nom, "DWWM")
        self.assertEqual(Cursus.objects.first().filiere, filiere)

    def test_create_cours(self):
        data = {
            "titre": "Algorithmique / Pseudo-Code",
            "technologie": "Algorithmique",
            "description": "Bases de la logique algorithmique"
        }

        response = self.client.post("/api/cours/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cours.objects.count(), 1)
        self.assertEqual(Cours.objects.first().titre, "Algorithmique / Pseudo-Code")

    def test_create_cursus_cours(self):
        filiere = Filiere.objects.create(
            nom="Développement",
            description="Filière liée au développement"
        )

        cursus = Cursus.objects.create(
            nom="DWWM",
            description="Développeur Web et Web Mobile",
            filiere=filiere
        )

        cours = Cours.objects.create(
            titre="Algorithmique / Pseudo-Code",
            technologie="Algorithmique",
            description="Bases de la logique algorithmique"
        )

        data = {
            "cursus": cursus.id,
            "cours": cours.id,
            "ordre": 1,
            "obligatoire": True
        }

        response = self.client.post("/api/cursus-cours/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CursusCours.objects.count(), 1)
        self.assertEqual(CursusCours.objects.first().ordre, 1)
        self.assertEqual(CursusCours.objects.first().cursus, cursus)
        self.assertEqual(CursusCours.objects.first().cours, cours)
