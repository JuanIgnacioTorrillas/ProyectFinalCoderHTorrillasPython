from django import forms

class MessageForm(forms.Form):
    sender = forms.CharField(max_length=5000)
    recipient = forms.CharField(max_length=5000)
    message = forms.CharField(widget=forms.Textarea)