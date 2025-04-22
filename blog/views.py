from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Post
from .forms import PostForm

# 投稿一覧（公開済み）
@login_required
def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created')
    return render(request, 'blog/post_list.html', {'posts': posts})

# 下書き一覧
@login_required
def draft_list(request):
    drafts = Post.objects.filter(author=request.user, published=False).order_by('-created')
    return render(request, 'blog/draft_list.html', {'drafts': drafts})

# 投稿詳細
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 投稿作成／下書き保存
@login_required
def post_create(request):
    # GETパラメータから指定された下書きを読み込み（新規投稿時は読み込まない）
    draft_id = request.GET.get('from_draft')
    if draft_id:
        draft = get_object_or_404(
            Post,
            pk=draft_id,
            author=request.user,
            published=False
        )
    else:
        draft = None

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=draft if draft else None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # ボタンで公開 or 下書き制御
            if 'save_as_draft' in request.POST:
                post.published = False
            else:
                post.published = True
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=draft if draft else None)

    return render(request, 'blog/post_form.html', {
        'form': form,
        'draft': draft,
    })

# 投稿編集
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # 編集時も公開/下書き切り替え可能
            if 'save_as_draft' in request.POST:
                post.published = False
            else:
                post.published = True
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'draft': None})

# 投稿削除
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

# ログイン後リダイレクト
def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    return redirect('login')

# ユーザー登録
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
