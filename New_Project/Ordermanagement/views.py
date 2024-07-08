from django.shortcuts import render,redirect
from .models import Customer,Orders
from .form import customer_form,Orders_Form
from New_App.models import Mytable

# Create your views here.


def customerlist(request):
    context = {
        "customer_details" : Customer.objects.all()
    }

    return render (request,'customer.html', context )


def customeradd(request):
    context = {
        "customer_Form":customer_form()
    }
    if request.method=="POST":
        customer_add=customer_form(request.POST)
        if  customer_add.is_valid():
             customer_add.save()
    return render(request,'customer_add.html',context)



def customer_delete(request,id):
    customer_remove=Customer.objects.get(id=id)
    customer_remove.delete()
    return redirect('/order/all/customers/')


def customer_update(request,id):
    customer_upd=Customer.objects.get(id=id)
    context={
        'customer_Form':customer_form(instance=customer_upd)}
    if request.method=='POST':
        product_form=customer_form(request.POST,instance=customer_upd)
        if product_form.is_valid():
            product_form.save()
            return redirect('/order/all/customers/')
    return render(request,'customer_add.html',context)






def OrdersAdd(request):
    context = {
        "order_form": Orders_Form()
    }
    if request.method == 'POST':
        selected_product = Mytable.objects.get(id= request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount= (amount * selected_product.gst )/100
        bill_amount = amount+gst_amount


        new_order = Orders(Customer_reference_id = request.POST['Customer_reference'], 
        product_reference_id = request.POST['product_reference'], order_number = request.POST['order_number'],
        order_date = request.POST['order_date'],quantity = request.POST['quantity'],amount = amount,gst_amount=gst_amount,bill_amount=bill_amount)
        
        new_order.save()
        return redirect('/order/orders')
    return render(request,'orders_add.html',context)

def OrdersList(request):
    context ={
        'all_orders': Orders.objects.all()
                }
    return render(request,'orders.html',context)


def OrderDelete(request,id):
    order = Orders.objects.get(id=id)
    order.delete()
    return redirect('/order/orders/')


def OrderUpdate(request,id):
    order = Orders.objects.get(id=id)
    context = {
        'order_form': Orders_Form(instance=order)

    }
    if request.method == 'POST':
        selected_product = Mytable.objects.get(id= request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount= (amount * selected_product.gst )/100
        bill_amount = amount+gst_amount
        order_filter = Orders.objects.filter(id=id)
        order_filter.update(Customer_reference_id = request.POST['Customer_reference'], 
        product_reference_id = request.POST['product_reference'], order_number = request.POST['order_number'],
        order_date = request.POST['order_date'],quantity = request.POST['quantity'],amount = amount,gst_amount=gst_amount,bill_amount=bill_amount)
        return redirect('/order/orders')

    return render(request, 'orders_add.html', context)











































































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
