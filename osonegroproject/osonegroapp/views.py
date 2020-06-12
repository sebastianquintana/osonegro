from django.shortcuts import render
from .models import ProductType, Product

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'osonegroapp/types.htm' ,{'type_list' : type_list})
# Create your views here.
def index (request):
    return render(request, 'osonegroapp/index.htm')

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'osonegroapp/products.htm', {'products_list': products_list})