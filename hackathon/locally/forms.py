from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        
        
        
#class CommentForm(forms.ModelForm):
    #class Meta:
      #  model = Comment
      #  fields = ('author','text',)