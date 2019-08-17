from django.shortcuts import render
from .models import Product 
# Create your views here.
def productlist(request):
    producutlist = Product.objects.all()

    context ={}
    template_name ='templates/product_list.html'
    return render(request, template_name, context)

def productdetail(request, id):
    print(id)
  