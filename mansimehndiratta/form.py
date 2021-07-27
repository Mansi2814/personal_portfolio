
# forms.py
from django import forms
from .models import *
  
class BlogsForm(forms.ModelForm):
  
    class Meta:
        model = Blogs
        fields = ['id', 'writer', 'read_time', 'content', 'title', 'title_image']