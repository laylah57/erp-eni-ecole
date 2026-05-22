from rest_framework import viewsets

from .models import (
    Promotion,
    Inscription,
    CoursPlanifie,
    Animer,
    Filiere,
    Cursus,
    Cours,
    CursusCours,
)

from .serializers import (
    PromotionSerializer,
    InscriptionSerializer,
    CoursPlanifieSerializer,
    AnimerSerializer,
    FiliereSerializer,
    CursusSerializer,
    CoursSerializer,
    CursusCoursSerializer,
)


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer


class CoursPlanifieViewSet(viewsets.ModelViewSet):
    queryset = CoursPlanifie.objects.all()
    serializer_class = CoursPlanifieSerializer


class AnimerViewSet(viewsets.ModelViewSet):
    queryset = Animer.objects.all()
    serializer_class = AnimerSerializer

class FiliereViewSet(viewsets.ModelViewSet):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer


class CursusViewSet(viewsets.ModelViewSet):
    queryset = Cursus.objects.all()
    serializer_class = CursusSerializer


class CoursViewSet(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer


class CursusCoursViewSet(viewsets.ModelViewSet):
    queryset = CursusCours.objects.all()
    serializer_class = CursusCoursSerializer
