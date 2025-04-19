from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),  # URL「/posts/」にアクセスしたらpost_list関数を実行
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # ← 追加！
]
