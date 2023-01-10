from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",inicio,name="Inicio"),
    path("leermas",ListaView.as_view(),name="LeerMas"),
    path("article/<int:pk>",ArticleDetailView.as_view(),name="DetalleBlog"),#llama con article key,ver detalles blogs
    path ('crearblog/', CrearBlog, name = "CrearBlog"), #crear blog
    path ('sobremi/', sobreMi, name= "SobreMi"), #AboutMe
    path ('eliminarBlog/<id>', deleteBlog, name = "EliminarBlog"),
    path ('actualizarBlog/<id>', editBlog, name = "ActualizarBlog"),
    path ("Login/",login_req, name = "IniciarSesion"),
    path ("Registrarse/", register, name = "Registrarse"),
    path ("actualizarUsuario/", editarUsuario, name = "Actualizar"),
    path ("CerrarSesion/", logout, name= "CerrarSesion"),
    path ("perfil/", perfil, name= "Perfil"),
    path ("editarPerfil/", editarPerfil, name= "EditarPerfil"),
    path("MisBlogs/",mis_blogs, name="MisBlogs"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
