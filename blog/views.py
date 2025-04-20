from django.shortcuts import render
from .models import Post  # 投稿モデルを読み込む
from django.contrib.auth.decorators import login_required

@login_required
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

from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # ログイン中のユーザーを紐づける！
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    return redirect('login')
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 登録後はログイン画面へ
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
