from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=300)
    recipient = models.CharField(max_length=300)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)