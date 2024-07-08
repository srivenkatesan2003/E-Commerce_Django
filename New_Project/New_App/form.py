from django.forms import ModelForm
from .models import Mytable


class Product(ModelForm):
    class Meta:
        model = Mytable
        fields ="__all__"
        # ['prodect_name','price']

    
