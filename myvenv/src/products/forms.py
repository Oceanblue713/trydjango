from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price'
    ]

class RawProductForm(forms.Form):
  #title = forms.CharField(label='')
  title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))
  description = forms.CharField(
                      required=False, 
                      widget=forms.Textarea(
                        attrs={
                          "class": "new-class-name two",
                          "id": "my-original-form",
                          "rows": 30,
                          "cols": 120,
                          "placeholder": "Description"
                        }
                      ))
  price = forms.DecimalField(initial=199.99)
