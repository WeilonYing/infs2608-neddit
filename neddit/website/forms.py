from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    content = forms.CharField(
        label="Content", widget=forms.Textarea, required=False)
    file = forms.FileField(label="Upload Notes", required=False)
