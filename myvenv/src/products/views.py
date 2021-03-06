from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product

def product_list_view(request):
  queryset = Product.objects.all()
  context = {
    "object_list": queryset
  }
  return render(request, "products/product_list.html", context)

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


def product_delete_view(request, id):
  obj = get_object_or_404(Product, id=id)
  if request.method == "POST":
    obj.delete()
    return redirect('../')
  context = {
    "object":obj
  }

  return render(request, "products/product_delete.html", context)