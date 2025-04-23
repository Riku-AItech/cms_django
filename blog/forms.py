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
    username = forms.CharField(label='ユーザー名', max_length=150)
    class Meta:
        model = Profile
        fields = ['username', 'bio', 'profile_image', 'twitter_url']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg', 'rows': 4}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 初期値としてUser.usernameをセット
        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        profile = super().save(commit=False)
        # Userモデルのusernameを更新
        username = self.cleaned_data.get('username')
        if username and profile.user.username != username:
            profile.user.username = username
            profile.user.save()
        if commit:
            profile.save()
        return profile
