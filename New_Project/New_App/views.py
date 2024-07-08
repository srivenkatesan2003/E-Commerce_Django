from django.shortcuts import render,redirect
from .models import Mytable
from .form import Product

# Create your views here.


def form(request):
    context = {
        "product" : Product()
    }
    if request.method == "POST":
        product= Product(request.POST)
        if product.is_valid():
            product.save()
    return render (request,'forms.html' , context )


def product(request):
    context = {
        "all_product":Mytable.objects.all()
    }
    return render (request,'product.html',context)


def Delete(request,id):
    selected_product=Mytable.objects.get(id=id)
    selected_product.delete()
    return redirect('/hi/product/')


def update(request,id):
    selected_product=Mytable.objects.get(id=id)
    context={
        'product':Product(instance=selected_product)}
    if request.method=='POST':
        product=Product(request.POST,instance=selected_product)
        if product.is_valid():
            product.save()
            return redirect('/hi/product/')
    return render(request,'forms.html',context)


















    # user=Mytable.objects.filter(id=id)
    # if request.method == 'POST':
    #     product_name1=request.POST.get('product_name')
    #     product_code1=request.POST.get('product_code')
    #     price1=request.POST.get('price')
    #     gst1=request.POST.get('gst')
    #     food_product1=request.POST.get('food_product')
    #     user.update(product_name=product_name1,product_code=product_code1,price=price1,gst=gst1,food_product=food_product1)
    #     return redirect("forms.html")
    # return render(request,'product.html')



# def update(request,id):
#     form=Mytable.objects.filter(id=id)
#     if request.method=="POST":
#         user1=request.POST.get('username')
#         password1=request.POST.get('password')
#         email1=request.POST.get('email')
#         form.update(user_name=user1,password=password1,email=email1)
    
#         return redirect('display')
#     return render(request,'login.html')
