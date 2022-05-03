from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=25
    )
    description = models.TextField()
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner'
    )

    def __str__(self):
        return str(self.id)


class PostImage(models.Model):
    image = models.ImageField()
    user = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_image'
    )

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_like'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_like'
    )

    def __str__(self):
        return str(self.user.username)
