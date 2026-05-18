from rest_framework import serializers

from .models import (
    Promotion,
    Inscription,
    CoursPlanifie,
    Animer
)


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'


class CoursPlanifieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursPlanifie
        fields = '__all__'


class AnimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animer
        fields = '__all__'