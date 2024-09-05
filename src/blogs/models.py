from general.models import BaseModel
from users.models import User
from django.db import models
# Create your models here.

class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to="posts/files", null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class PostComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()


class PostLike(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')