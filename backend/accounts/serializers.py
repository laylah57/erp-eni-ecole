from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


# This serializer's intent is to find the username from the email received from request, and then use it and the
# password to generate the JWT token pair. We have to use this way around since Django's User model does not enforce
# uniqueness on email addresses, and that by default JWT uses the username and password to generate the tokens.
class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = (
        serializers.EmailField()
    )  # EmailField() checks that the value has an email shape. Otherwise rejects the
    # value as invalid.

    # In the __init__ we are redefining the username field so that is it not required anymore, otherwise JWT
    # recreated is by default and the authentication is saying the username is missing even after reassigning it.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field].required = False

    def validate(self, attrs):
        email = attrs["email"]
        user = User.objects.filter(email=email).first()  # Use first() so an unknown email returns None instead of raising DoesNotExist.

        if not user:
            raise AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        attrs["username"] = user.username
        return super().validate(attrs)
