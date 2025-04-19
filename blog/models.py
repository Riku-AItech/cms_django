from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # タイトル（短い文字）
    content = models.TextField()              # 本文（長文）
    published = models.BooleanField(default=True)  # 公開 or 非公開
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時（自動）

    def __str__(self):
        return self.title  # 管理画面でタイトルを表示
