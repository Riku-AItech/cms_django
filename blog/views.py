from django.shortcuts import render
from .models import Post  # 投稿モデルを読み込む

def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')  # 公開済みの投稿だけ、日付の新しい順
    return render(request, 'blog/post_list.html', {'posts': posts})
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


