from django.urls import path
from Chat.views import *

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('view/', view_messages, name='view_messages'),
    path('respond/<int:message_id>/', respond_message, name='respond_message'),
    path("envioCorrecto/",envio_correcto,name="envioorrecto"),
]

