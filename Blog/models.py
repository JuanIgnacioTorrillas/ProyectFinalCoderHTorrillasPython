from django import forms
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.forms import UserCreationForm


class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True) #Opcional, por eso blank=true
    cuerpo = RichTextUploadingField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #Borra posts si el autor/user es borrado
    fecha = models.DateTimeField() #Fecha de Publicacion
    imagen = models.ImageField(upload_to='static/images', blank=True) #Directorio donde se va a guardar

    def __str__(self):
        return self.titulo + " " + str(self.autor)
    
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    first_name =  models.CharField(max_length= 40)
    last_name =  models.CharField(max_length= 40)
    
    def __str__(self):
        return self.first_name + " " + str(self.last_name)

