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

# blog/views.py（末尾に追記）

from .forms import PostForm
from django.shortcuts import redirect

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # 投稿後、一覧に戻る
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 一旦保存せずにインスタンスだけ取得
            post.author = request.user      # ログイン中のユーザーを設定！
            post.save()                     # ここで保存
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
