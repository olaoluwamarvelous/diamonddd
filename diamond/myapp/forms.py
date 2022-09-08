from django.forms import ModelForm
from .models import ContactModel, Comment
from django import forms

class CONTACTFORM(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'subject', 'cv', 'email', 'messagess')
        exclude = ['created']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

