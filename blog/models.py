from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    # null=True，则仅表示在数据库中该字段可以为空，但使用后台管理添加数据时仍然要需要输入值，因为Django自动做了数据验证不允许字段为空
    # 如果想要在Django中也可以将字段保存为空值，则需要添加另一个参数：blank=True
    excerpt = models.CharField(max_length=200, blank=True)
    # 一对多的关联关系,CASCADE分类删除，分类下的文章也删除
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 多对多关系，DO_NOTHING 删除一个标签，文章不动
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-create_time']
        verbose_name = '文章'
        verbose_name_plural = '文章'
# super
# puhao123
