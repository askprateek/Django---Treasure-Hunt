from django import forms
from .models import Question

class Check_question(forms.Form):
    answer = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)))
