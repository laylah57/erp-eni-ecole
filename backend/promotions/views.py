from rest_framework import viewsets



from rest_framework.permissions import AllowAny



from .models import Promotion, Inscription, CoursPlanifie, Animer



from .serializers import (



    PromotionSerializer,



    InscriptionSerializer,



    CoursPlanifieSerializer,



    AnimerSerializer,



)



class PromotionViewSet(viewsets.ModelViewSet):



    queryset = Promotion.objects.all()



    serializer_class = PromotionSerializer



    permission_classes = [AllowAny]



class InscriptionViewSet(viewsets.ModelViewSet):



    queryset = Inscription.objects.all()



    serializer_class = InscriptionSerializer



    permission_classes = [AllowAny]



class CoursPlanifieViewSet(viewsets.ModelViewSet):



    queryset = CoursPlanifie.objects.all()



    serializer_class = CoursPlanifieSerializer



    permission_classes = [AllowAny]



class AnimerViewSet(viewsets.ModelViewSet):



    queryset = Animer.objects.all()



    serializer_class = AnimerSerializer



    permission_classes = [AllowAny]
