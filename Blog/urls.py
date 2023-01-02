from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",inicio,name="Inicio"),
    path("leermas",ListaView.as_view(),name="LeerMas"),
    path("article/<int:pk>",ArticleDetailView.as_view(),name="DetalleBlog"),#llama con article key,ver detalles blogs
    path ('crearblog/', CrearBlog.as_view(), name = "CrearBlog"), #crear blog
    path ('sobremi/', sobreMi, name= "SobreMi"),
    path ('eliminarBlog/<int:pk>/', DeleteBlog.as_view(), name = "EliminarBlog"),
    path ('actualizarBlog/<int:pk>/', UpdateBlog.as_view(), name = "ActualizarBlog"),
    path ('busqueda/',  busqueda_blog , name="Busqueda"),
    path ("Iniciar-sesion/", LogInUser.as_view(), name = "IniciarSesion"),
    path ("Registrarse/", SignUpUser.as_view(), name = "Registrarse"),
    path ("actualizar/<int:pk>/", UpdateUser.as_view(), name = "Actualizar"),
    path ("Cerrar-Sesion/", LogOutUser.as_view(), name= "CerrarSesion"),
    path ("perfil/<int:pk>/", Perfil.as_view(), name= "Perfil"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
