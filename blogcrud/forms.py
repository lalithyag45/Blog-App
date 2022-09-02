from django import forms
from .models import Post,Comment
#from .models import Comment

class blogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'My travel memories'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id':'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'My travel memories'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('comment',)

        widgets ={
            'comment': forms.Textarea(attrs={'class':'form-control'}),
        }