"""
    Serializers for accounts app.
"""
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
import uuid


class UserSerializer(ModelSerializer):
    """
    User model serializer where email is the unique identifier
    for authentication instead of usernames.
    """

    def create(self, validated_data):
        """
        Function to create User.
        """
        image = validated_data.pop('image', None)
        if image:
            image._set_name(str(uuid.uuid4()))
        user = get_user_model().objects.create(**validated_data)
        user.image = image
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email",
                  "password", "dob", "image")
        extra_kwargs = {
            "password": {"write_only": True},
            "image": {"required": False},
            "dob": {"required": False},
        }
