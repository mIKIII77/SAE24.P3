from django.forms import ModelForm
from . import models
from django import forms

class SensorForm(ModelForm):
    class Meta:
        model = models.Sensor
        fields = ['emplacement', 'nom']
        label = {
            'nom': 'Nom du capteur',
            'emplacement': 'Emplacement',
        }

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'emplacement': forms.TextInput(attrs={'class': 'form-control'}),

        }