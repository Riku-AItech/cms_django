# blog/forms.py
from django import forms
from .models import Post, Category, Profile
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'published', 'image']
        widgets = {
            'content': CKEditorWidget(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # プロフィール編集は画像と自己紹介のみ
        fields = ['profile_image', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'rows': 4}),
        }
