from django.shortcuts import render,redirect 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
# Create your views here.



def index (request):
    products=Product.objects.all()
    item_name=request.GET.get('item_name')
    
    if item_name!='' and item_name is not None:  # to avoid empty search
        products=Product.objects.filter(title__icontains=item_name)   # icontains is used to ignore case sensitivity
    
    
    # Pagination
    paginator=Paginator(products,3)  # Show 6 products per page
    page= request.GET.get('page')   # get the page number from the request
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        products = paginator.page(paginator.num_pages)    
    
    
    return render(request,'shop/index.html',{'products':products})


def detail (request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'shop/detail.html',{'product':product})
