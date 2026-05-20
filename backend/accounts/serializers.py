from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()

    def get_groups(self, obj):
        all_groups = obj.groups.all()
        groups_array = []
        for group in all_groups:
            groups_array.append(group.name)
        return groups_array

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "groups"]
