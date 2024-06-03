from django.shortcuts import render
from . models import *
import json
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.



def home(request):
    slider = Slider.objects.all()[:3]
    category = mainCategory.objects.all()
    product = Product.objects.all()[:5]
    context = {
        'slider':slider,
        'category':category,
        'products':product,
    }
    return render(request, "home.html",context)


def shop(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category':category,
        'products':product,
    }
    return render(request, "product.html",context)


def filter_category(request):
    product = Product.objects.all()
    if request.method == "POST":
        jsondata =json.loads(request.body.decode("utf-8"))
        req = jsondata.get('categories')
        product = Product.objects.filter(category__id__in=req).distinct()
        if len(req) == 0:
            product = Product.objects.all()
        context = {
            "products":product,
        }
        data = render_to_string('includes/ajax/product-filter.html',context)
    
    return JsonResponse({"status":"Success",'data':data})    

def product_details(request,slug):
    product = Product.objects.get(slug=slug)
    context = {
            "product":product,
        }
    return render(request, "product-details.html",context)

def user_account(request):
     return render(request, "user-account.html")