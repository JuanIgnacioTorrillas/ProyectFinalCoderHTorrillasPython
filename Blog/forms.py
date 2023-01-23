from django import forms
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

#Blog
class BlogForm(forms.ModelForm):
   
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo','autor','fecha','imagen']


#Usuario  
class RegistroForm(UserCreationForm): #Registro Usuario
    first_name = forms.CharField(label="Ingrese nombre")
    last_name = forms.CharField(label="Ingrese apellido")
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        help_texts = {x:"" for x in fields} #Valores Vacios
        
class EditUserForm(UserChangeForm): #Editar Usuario
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        help_texts = {x:"" for x in fields}
        
class Form_Perfil(ModelForm):
    class Meta:
        model = Perfil
        fields = ['descripcion', 'web', 'avatar']
        
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")