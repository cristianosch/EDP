from django import forms
from .models import Counter
#from django.contrib.auth.models import User


class CounterCreateForm(forms.ModelForm):
    class Meta:
        model = Counter
        fields = ['quantities']



     




