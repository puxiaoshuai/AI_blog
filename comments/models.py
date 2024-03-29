from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-create_time']
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __str__(self):
        return self.text[:20]
