from django.shortcuts import render,redirect 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product,Order
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
    product=Product.objects.get(pk=pk)   # get the product with the given primary key
    return render(request,'shop/detail.html',{'product':product})   # render the product detail page with the product context



def checkout (request):
    
    
    
    if request.method=='POST':   # if the request method is POST, then save the order details to the database
        
        items=request.POST.get('items','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        Address=request.POST.get('Address','')
        City=request.POST.get('City','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zipcode','')
        total=request.POST.get('total','')
        order=Order(items=items,name=name,email=email,Address=Address,City=City,state=state,zipcode=zipcode,total=total)
        order.save()
        
    return render(request,'shop/checkout.html')   # render the checkout page