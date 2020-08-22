from django import forms
from main import models
from django.forms import ModelMultipleChoiceField
from main.models import (Author,Article)
from django.forms import ModelForm


class createarticleform(forms.ModelForm):
    class Meta:
        model=models.Article
        fields ='__all__'
    
    