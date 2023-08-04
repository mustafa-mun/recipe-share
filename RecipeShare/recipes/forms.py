from django.forms import ModelForm
from .models import MainIngredient

class MainIngredientForm(ModelForm):
    class Meta:
        model = MainIngredient
        fields = '__all__'
