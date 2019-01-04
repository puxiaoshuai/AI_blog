from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.models import Post

from .forms import CommentForm


def post_comments(request, post_pk):
    # 先查出文章，在绑定到评论
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            ## commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            print(comment.name)
            comment.post = post
            comment.save()
            return redirect('blog:detail' ,pk=post_pk)
        else:
            comment_list = post.comment_set.all()
            content = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/index.html', context=content)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect('blog:detail',pk=post_pk)
