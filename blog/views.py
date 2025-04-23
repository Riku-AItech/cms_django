from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

from .models import Post, Category, Profile
from .forms import PostForm, ProfileForm

# 投稿一覧（公開済み）
@login_required
def post_list(request):
    # 検索機能: GETパラメータ 'q' によるタイトル部分一致
    q = request.GET.get('q', '').strip()
    # ソート機能: GETパラメータ 'sort' による並び替え
    sort = request.GET.get('sort', '')
    # カテゴリフィルタ: GETパラメータ 'category'
    category_id = request.GET.get('category')
    posts = Post.objects.filter(published=True, author__isnull=False)
    if q:
        posts = posts.filter(title__icontains=q)
    if category_id:
        posts = posts.filter(category_id=category_id)
    # 並び替えロジック
    if sort == 'created_asc':
        posts = posts.order_by('created')
    elif sort == 'created_desc':
        posts = posts.order_by('-created')
    elif sort == 'title_asc':
        posts = posts.order_by('title')
    elif sort == 'title_desc':
        posts = posts.order_by('-title')
    elif sort == 'author_asc':
        posts = posts.order_by('author__username')
    elif sort == 'author_desc':
        posts = posts.order_by('-author__username')
    else:
        posts = posts.order_by('-created')
    # カテゴリ一覧を取得
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'q': q,
        'sort': sort,
        'category_id': category_id,
        'categories': categories,
    })

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
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return render(request, "403.html", status=403)
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
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return render(request, "403.html", status=403)
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

@login_required
def profile(request, username):
    # ユーザーのプロフィールページ
    user_obj = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user_obj, published=True).order_by('-created')
    profile = getattr(user_obj, 'profile', None)
    return render(request, 'blog/profile.html', {
        'profile_user': user_obj,
        'profile': profile,
        'posts': posts,
    })

@login_required
def profile_edit(request):
    # プロフィールがない場合は作成
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/profile_edit.html', {
        'form': form,
    })
