from rest_framework import viewsets

from .models import (
    Promotion,
    Inscription,
    CoursPlanifie,
    Animer
)

from .serializers import (
    PromotionSerializer,
    InscriptionSerializer,
    CoursPlanifieSerializer,
    AnimerSerializer
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