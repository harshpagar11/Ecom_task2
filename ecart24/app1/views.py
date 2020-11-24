from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import Registerform
from django.contrib.auth.forms import AuthenticationForm
from app1.models import Product

#homepage
def homepage(request):
    data = Product.objects.all()
    if request.user:
        sun = request.user
        return render(request,"home.html",{"sun":sun,"data":data})
    else:
        return render(request, "home.html",{"data":data})


# signup
def signup(request):
    if request.method == "POST":
        fm = Registerform(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/login/")
    else:
        fm =Registerform()
    return render(request,"signup.html",{'form':fm})

#login view
def userlogin(request):

    if request.method == "POST":

        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
            return render(request, "profile.html", {"name": request.user})
    else:
        if request.user.is_authenticated:
            name = request.user
            print(name)
            return render(request,"profile.html",{"name": name})
        else:
            fm = AuthenticationForm()
            return render(request, "login.html", {'form': fm})



#profile
def profile(request):
    if request.user.is_authenticated:
        name = request.user
        print(name)
        return render(request, "profile.html", {"name": name})
    else:
        return redirect('login')


#logout
def userlogout(request):
    logout(request)
    return redirect('login')


def clothing(request):
    data = Product.objects.filter(Category="clothing")

    if request.user:
        sun = request.user
        return render(request,"clothing.html", {"data": data, "sun": sun})
    return render(request,"clothing.html",{"data":data})

def accessories(request):
    data = Product.objects.filter(Category="accessories")

    if request.user:
        sun = request.user
        return render(request,"accessories.html", {"data": data, "sun": sun})
    return render(request,"accessories.html",{"data":data})

def shoes(request):
    data = Product.objects.filter(Category="shoes")

    if request.user:
        sun = request.user
        return render(request, "shoes.html", {"data": data, "sun": sun})
    return render(request, "shoes.html", {"data": data})


def cart(request):
    return render(request,"cart.html")


