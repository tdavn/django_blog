from django import forms
from .models import Post, Category


# choices = [('ML', 'ML'), ('Python', 'Python'), ('Django', 'Django'),] 
choices = Category.objects.all().values_list('name', 'name')
# choice_list = []
# for item in choices:
#     choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'author', 'category', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 
            'placeholder': 'Nothing gonna change my love'}),  # class from bootstrap form element
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  # can check website for more
            'author': forms.Select(attrs={'class': 'form-control'}),  # if use own css, can replace here
            'category': forms.Select(choices=list(choices), attrs={'class': 'form-control'}), 
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),  # check attrs can be parsed here
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'title_tag', 'category', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 
            'placeholder': 'This is a title placeholder'}),  # class from bootstrap form element
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),  # can check website for more
            # 'author': forms.Select(attrs={'class': 'form-control'}),  # if use own css, can replace here
            'category': forms.Select(choices=list(choices), attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),  # check attrs can be parsed here
        }