import markdown
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post, Category
from  comments.forms import CommentForm



def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    form=CommentForm()
    comment_list=post.comment_set.all()
    content = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context=content)


def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def categroies(requset, pk):
    # 先查询大到分类，在根据分类来加载文章
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(requset, 'blog/index.html', context={'post_list': post_list})
