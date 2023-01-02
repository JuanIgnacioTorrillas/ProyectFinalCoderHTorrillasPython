from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

#-----BLOG-----

def inicio(request):
    
    return render(request, 'inicio.html',{})


class ListaView(ListView): #Lista de Blogs
    model= Blog
    template_name="leermas.html"


def sobreMi(request): #About Me
    return render(request, "sobremi.html", {})


class ArticleDetailView(DetailView): #Detalles del blog
    model=Blog
    template_name="detalle.html"


class CrearBlog(LoginRequiredMixin, CreateView): #Añadir Blog

    model = Blog
    success_url = reverse_lazy("LeerMas")
    fields = ['titulo', 'subtitulo', 'cuerpo','autor','fecha','imagen']

class UpdateBlog(LoginRequiredMixin, UpdateView): #Editar Blog
    model = Blog
    template_name = 'actualizarblog.html'
    fields = ['titulo', 'subtitulo', 'cuerpo','autor','fecha','imagen']
    success_url = reverse_lazy("LeerMas")

class DeleteBlog(LoginRequiredMixin,DeleteView): #Borrar Blog
    model = Blog
    template_name ='eliminarblog.html'
    success_url = reverse_lazy("Blogs")
    
def busqueda_blog(request): #Buscar un Blog
    
    busqueda_blog = BusquedaBlogs()

    if request.GET.get("gusto"): #o tambien if "gusto" in request.GET

        autor=request.GET["autor"]
        
        resultado = Blog.objects.filter(autor = autor)
    
    else:
        resultado = "No existe Blog de ese Autor"
    
    return render(request, "busqueda.html", {"busqueda_blog": busqueda_blog, "resultado": resultado})
    
    
    
#-----LOGIN-----

class SignUpUser(CreateView,SuccessMessageMixin):  #Registrarse
    model = Usuario
    template_name = 'Registrarse.html'
    success_url = reverse_lazy("IniciarSesion") 
    form_class = User_Form 
    
class LogInUser(LoginView): #LogIn
    
    template_name = 'iniciosesion.html'
    
    def get_success_url(self):

        return reverse_lazy("Perfil", kwargs={"pk": self.request.user.usuario.id})
    
class LogOutUser(LogoutView): #LogOut
    template_name = "cerrarsesion.html"
    
class UpdateUser(UpdateView,LoginRequiredMixin,UserPassesTestMixin): #Actualizar Datos
    
    model = Usuario
    template_name = 'actualizarUser.html'
    fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def test(self):
        return self.request.user.usuario.id == int(self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy("Perfil", kwargs={"pk": self.request.user.usuario.id})

class Perfil(LoginRequiredMixin,UserPassesTestMixin, DetailView): #Ver Perfil

    model = Usuario
    template_name = "perfil.html"

    def test(self):
        return self.request.user.usuario.id == int(self.kwargs['pk'])