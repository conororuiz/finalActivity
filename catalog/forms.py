from django import forms
from catalog.models import Vehicle


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"
