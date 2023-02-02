from django import forms

from main.models import Pen


class PenForm(forms.ModelForm):

    class Meta:
        model = Pen
        fields = '__all__'