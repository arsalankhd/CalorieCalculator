from django import forms
from .models import *

class foodConsumedForm(forms.ModelForm):
    class Meta:
        model = foodConsumed
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(foodConsumedForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = foodItem.objects.filter(person_of=user)