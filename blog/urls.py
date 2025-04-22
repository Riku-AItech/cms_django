from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),  # URL「/posts/」にアクセスしたらpost_list関数を実行
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # ← 追加！
    path('posts/new/', views.post_create, name='post_create'),  # ← 追加！
    path('posts/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('', views.home_redirect, name='home'),
     # 投稿関連
    path('posts/', views.post_list, name='post_list'),
    path('new/', views.post_create, name='post_create'),
    path('posts/drafts/', views.draft_list, name='draft_list'),
    # …など


]
