from django import forms

from .models import Character, CharacterModel, JOBS, GENDER


class CreateCharacter(forms.ModelForm):
    class Meta:
        model = CharacterModel
        fields = ['job','gender']