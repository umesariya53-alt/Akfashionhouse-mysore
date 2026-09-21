from django.shortcuts import render
from .models import Product

def home(request):
    cats = [
        {"name": "Mens Suits", "price": "4500", "icon": "🤵"},
        {"name": "Sherwanis", "price": "8500", "icon": "👑"},
        {"name": "Kurta Paijama", "price": "2500", "icon": "🥻"},
        {"name": "Kotis", "price": "1800", "icon": "🦺"},
        {"name": "Jodhpuri", "price": "6500", "icon": "🤴"},
        {"name": "Pant Shirts", "price": "2200", "icon": "👔"},
    ]
    return render(request, 'store/base.html', {'cats': cats})

def category_view(request, cat_name):
    # is category ke products
    products = Product.objects.filter(category=cat_name)
    return render(request, 'store/category.html', {'products': products, 'cat_name': cat_name})
