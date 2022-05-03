from rest_framework import serializers

from apps.post.models import Post, PostImage, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = (
            'id',
            'user'
        )

    def validate(self, attrs):
        validate_max_like_per_user = Like.objects.filter(
            user=attrs['user']
        )
        print(len(validate_max_like_per_user))
        if validate_max_like_per_user.count() + len(attrs) > 101:
            raise serializers.ValidationError({'hey': 'limit of likes'})

        return attrs


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"
        read_only_fields = (
            'id',
            'user'
        )


class PostSerializer(serializers.ModelSerializer):
    post_like = LikeSerializer
    post_image = PostImageSerializer

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = (
            'id',
            'create_at',
            'owner'
        )

    def validate(self, attrs):
        validate_to_max_per_user = Post.objects.filter(
            owner=attrs['owner'],
        )
        print(len(validate_to_max_per_user))
        if validate_to_max_per_user.count() + len(attrs) > 27:
            raise serializers.ValidationError({'hey': 'you need new account or delete old posts'})

        return attrs
