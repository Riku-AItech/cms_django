"""
URL configuration for cms_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  # ← include を追加！
from django.shortcuts import redirect  # ← 追加
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blog.views import signup_view  # ← サインアップビューをインポート
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', lambda request: redirect('post_list')),  # ← トップを投稿一覧にリダイレクト
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # ← これで blog/urls.py を読み込む！
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # ✅ ログイン
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # ログイン画面に遷移するよう修正
    path('accounts/signup/', signup_view, name='signup'),  # ✅ サインアップ
    path('accounts/', include('django.contrib.auth.urls')),  # ← これ追加！
]
# DEBUG設定に関わらず、MEDIA_URLでメディアファイルを配信
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
