from rest_framework import serializers
from kellygram.users import models


class ExploreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'profile_image',
            'username',
            'name',
        )
