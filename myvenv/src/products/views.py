from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, RawProductForm
from .models import Product

def dynamic_lookup_view(request, id):
  #obj = Product.objects.get(id=id)
  #obj = get_object_or_404(Product, id = id)
  try:
    obj = Product.objects.get(id=id)
  except Product.DoesNotExist:
    raise Http404
  context = {
    "object": obj
  }
  return render(request, "products/product_detail.html", context)