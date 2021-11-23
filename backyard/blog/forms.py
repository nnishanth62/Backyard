from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')  # add additional categories from admin
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):  # Model Form allows us to create post fields
    class Meta:
        model = Post
        # fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')
        fields = ('title', 'location', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs = {'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


class EditForm(forms.ModelForm):  # Model Form allows us to create post fields
    class Meta:
        model = Post
        #fields = ('title', 'title_tag', 'body', 'snippet')
        fields = ('title', 'location', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }

class CommentForm(forms.ModelForm):  # Model Form allows us to create post fields
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }