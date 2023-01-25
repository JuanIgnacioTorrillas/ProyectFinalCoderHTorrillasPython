from django.shortcuts import render,redirect
from .models import *
from .forms import *

from django.views.generic import ListView,DetailView

from django.contrib.auth.decorators import login_required


from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from datetime import date

#-----BLOG-----

def obtenerAvatar(request):
    if request.user.is_authenticated:
        lista = Perfil.objects.filter(user=request.user)
        if len(lista)!=0:
            imagen = lista[0].avatar.url
        else:
            imagen = ""
    else:
        imagen = ""
    return imagen

def inicio(request):
    
    return render(request, 'inicio.html' )


def ListaBlogs(request): #Lista de Blogs
    blogs = Blog.objects.all().order_by('-fecha')
    return render(request, 'leermas.html', {'blogs':blogs})



def sobreMi(request): #About Me
    return render(request, "sobremi.html", {})


class ArticleDetailView(DetailView): #Detalles del blog
    model=Blog
    template_name="detalle.html"



@ login_required
def CrearBlog(request): #Añadir Blog
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            datos = form.cleaned_data
            nombre_autor = request.user
            nuevo_blog = Blog(titulo = datos["titulo"], subtitulo = datos["subtitulo"], cuerpo = datos["cuerpo"], imagen = datos["imagen"] , autor = nombre_autor, fecha = date.today())
            nuevo_blog.save()
            return render(request, "inicio.html", {"mensaje": "¡Has agregado un Blog!"})
        else:
            form = BlogForm(initial={})
            return render(request, "crearblog.html", {"form" : form, "mensaje": "Error,No se pudo crear el blog, intentelo denuevo"})
    else:
        form = BlogForm(initial={})
        return render(request, "crearblog.html", {"form" : form})




@login_required
def editBlog(request, idPost): #Editar
    
    blog = Blog.objects.get(id=idPost)   
    form = BlogForm(instance=blog)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            
            return redirect(f'/article/{idPost}')

    context = {
        'form':form,
    }
    
    return render(request, 'actualizarblog.html', context)




@login_required
def deleteBlog(request, id): #Borrar
    if request.method == 'GET':
        articulo = Blog.objects.get(id=id)
        articulo.delete()
        return render(request, 'Inicio.html', {'mensaje':'Articulo Eliminado Correctamente'})
    else:
        return render(request, 'Inicio.html', {'mensaje':'No puede eliminar el articulo'})
    
#-----LOGIN/USUARIO-----




def register(request): #Registrarse
    if request.method == "POST":
        registro = RegistroForm(request.POST)
        if registro.is_valid():
            usuario = registro.cleaned_data.get("username")
            registro.save()     
            return render(request, "inicio.html", {"mensaje":"Usuario  creado correctamente"})
        else:
           return render(request, "Registrarse.html", {"form":registro , "mensaje":"Usuario creado correctamente"}) 
    else:
        registro = RegistroForm()
        return render(request, "Registrarse.html", {"form":registro})

def login_req(request): #Login
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            
            log_user = authenticate(username = usuario, password = clave)
            
            if log_user is not None:    
                login(request, log_user)
                return render(request, 'inicio.html', {'mensaje':f"Bienvenido {usuario}" })
            else:
                form = AuthenticationForm()
                return render(request, 'iniciosesion.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

        else:
            form = AuthenticationForm()
            return render(request, 'iniciosesion.html', {'mensaje':"Usuario o contraseña incorrectos", 'form':form})

    else:
        form = AuthenticationForm()
    return render(request, "iniciosesion.html", {"form":form})
    
@ login_required #LogOut
def logout_req(request):
    logout(request)
    return render(request, "inicio.html", {"mensaje":"LogOut Correcto"})
    
@ login_required #Editar Usuario
def editarUsuario(request):
    
    if request.method == "POST":
        form = EditUserForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return render(request, "inicio.html", {"mensaje":"Informacion editada correctamente"})
        else:
            form = EditUserForm()
            return render(request, "actualizarUser.html", {"form" : form, "mensaje":"Error al editar el perfil"}) 
    else:
        form = EditUserForm()
        return render(request, "actualizarUser.html", {"form":form})
    
@ login_required #Ver Perfil
def perfil(request):
    datos_perfil = Perfil.objects.filter(user = request.user)
    if datos_perfil:
        descripcion = datos_perfil[0].descripcion
        web = datos_perfil[0].web
    else:
        descripcion = ""
        web = ""
    return render(request, "perfil.html", {"user" : request.user, "descripcion" : descripcion, "web": web, "avatar": obtenerAvatar(request)})

@ login_required
def editarPerfil(request): #Editar Perfil
    datos = Perfil.objects.filter(user = request.user)
    if datos:
        form = Form_Perfil(initial={"descripcion": datos[0].descripcion, "web": datos[0].web, "avatar": datos[0].avatar})
    else:
        form = Form_Perfil()
    if request.method == "POST":
        formulario = Form_Perfil(request.POST, request.FILES)
        if formulario.is_valid():
            datos = Perfil.objects.filter(user = request.user)
            if datos != None: 
                datos.delete()
            datos_nuevos = Perfil(user=request.user, descripcion = request.POST["descripcion"], web = request.POST["web"], avatar = request.FILES["avatar"] )
            datos_nuevos.save()
            return render(request, "inicio.html", {"mensaje": "El perfil ha sido editado exitosamente!"})
        else:
            form = Form_Perfil()
            return render(request, "actuaperfil.html", {"form" : form, "mensaje": "Lo siento, ocurrio un error.Webs requieren: https:/www. Vuelva a Intentarlo"})
    else:
        form = Form_Perfil()
        return render(request, "actuaperfil.html", {"form": form})
    
