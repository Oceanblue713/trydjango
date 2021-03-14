from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
  title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title"}))
  email = forms.EmailField()
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
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price'
    ]

  def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get("title")
    if not "CFE" in title:
      raise forms.ValidationError("This is not valid title")
    if not "news" in title:
      raise forms.ValidationError("This is not valid title")
    else: 
      return title

  def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get("email")
    if not email.endswith("edu"):
      raise forms.ValidationError("This is not valid email")

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
