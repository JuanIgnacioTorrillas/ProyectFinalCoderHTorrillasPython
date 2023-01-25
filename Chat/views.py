from django.shortcuts import render, redirect
from Chat.models import *
from Chat.forms import *
from django.contrib.auth.models import User

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            recipient = form.cleaned_data['recipient']
            message = form.cleaned_data['message']
            Message.objects.create(sender=sender, recipient=recipient, message=message)
            return redirect("envioorrecto")
    else:
        form = MessageForm()
    return render(request, 'enviar.html', {'form': form})

def view_messages(request):
    user = request.user
    sent_messages = Message.objects.filter(sender=user)
    received_messages = Message.objects.filter(recipient=user)
    return render(request, 'lectura.html', {'sent_messages': sent_messages, 'received_messages': received_messages})

def respond_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            recipient = form.cleaned_data['recipient']
            message = form.cleaned_data['message']
            Message.objects.create(sender=sender, recipient=recipient, message=message)
            return redirect("envioorrecto")
    else:
        form = MessageForm(initial={'recipient': message.sender, 'sender': message.recipient})
    return render(request, 'responder.html', {'form': form, 'message': message})

def envio_correcto(request):
    return render(request, 'enviado.html' )