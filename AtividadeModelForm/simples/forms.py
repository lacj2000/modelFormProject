from django.forms import ModelForm
from simples.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'