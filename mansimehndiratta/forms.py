from django import forms
from .models import *
  
class Title_img_uploadForm(forms.ModelForm):
  
    class Meta:
        model = Title_img_upload
        fields = ['img_upload']