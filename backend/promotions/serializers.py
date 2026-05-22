from rest_framework import serializers

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


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = "__all__"


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = "__all__"


class CoursPlanifieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursPlanifie
        fields = "__all__"


class AnimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animer
        fields = "__all__"


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = "__all__"


class CursusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursus
        fields = "__all__"


class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = "__all__"


class CursusCoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursusCours
        fields = "__all__"
