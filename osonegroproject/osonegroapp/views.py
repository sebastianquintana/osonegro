from django.shortcuts import render
from .models import RecordType, Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

def gettypes(request):
    type_list=RecordType.objects.all()
    return render(request, 'osonegroapp/types.htm' ,{'type_list' : type_list})
# Create your views here.
def index (request):
    return render(request, 'osonegroapp/index.htm')

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'osonegroapp/products.htm', {'products_list': products_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    discount=prod.memberdiscount
    reviews=Review.object.filter(product=id).count()
    context={
        'prod': prod,
        'discount' : discount,
        'reviews': reviews,
    }
    return render(request,'osonegroapp/productdetails.htm', context=context)

def newRecord(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'osonegroapp/newrecord.htm', {'form': form})

def loginmessage(request):
    return render(request, 'osonegropp/loginmessage.htm')

def logoutmessage(request):
    return render(request, 'osonegroapp/logoutmessage.htm')


@login_required
def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'osonegroapp/newrecord.htm', {'form': form})