from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User

# Create your views here.
def LoginPage(request):
    context ={
        "error":""
    }
    if request.method == "POST":
        print (request.POST)
        user = authenticate(username = request.POST['username'],
                            password = request.POST['password'])
        print(user)
        if user is not None:
            login(request,user)
            return redirect("/order/all/customers/")
        else:
            context={
                "error":"*Invalid username or password"
            }
            return render(request,'login.html',context)
    return render(request,'login.html',context)


def LogoutUser(request):
    logout(request)
    return redirect('/')


def SignupPage(request):
    context = {
        "error": ""
    }

    if request.method == "POST":
        user_check = User.objects.filter(username = request.POST['username'])
        if len(user_check) > 0:
            context ={
                "error":"*username already exists!"
            }
        else:
            new_user = User(username = request.POST['username'],first_name = request.POST['firstname'],last_name = request.POST['lastname'],
            email = request.POST['email_address'],age = request.POST['age'])
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('/')    
    return render(request,'signup.html',context)