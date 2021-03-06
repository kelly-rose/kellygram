from rest_framework import serializers
from kellygram.users import models as user_models
from kellygram.images import models


class FeedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer):
    creator = FeedUserSerializer(read_only=True)
    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        )

class LikeSerializer(serializers.ModelSerializer):
    # image = ImageSerializer()
    class Meta:
        model = models.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True)
    creator = FeedUserSerializer()
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments', #comment_set
            'like_count',  #1-40
            'creator',
        )
