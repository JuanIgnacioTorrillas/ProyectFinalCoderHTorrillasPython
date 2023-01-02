from django import forms
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo','autor','fecha','imagen']
    
class User_Form(UserCreationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name']
        
class BusquedaBlogs(forms.Form):
    search = forms.CharField()