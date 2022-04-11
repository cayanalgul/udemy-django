from django.shortcuts import redirect, render,HttpResponse
from matplotlib.style import context
from .forms import RegsiterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def register(request):

    form = RegsiterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newuser = User(username=username)
        newuser.set_password(password)
        newuser.save()

        login(request,newuser)
        messages.success(request,"Başarıyla Kaydoldunuz...")
        return redirect("index")

    else:
        form = RegsiterForm()
        context={
            "form":form
        }
        
        return render(request,"register.html",context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context={
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)
        if user is None:
            
            messages.warning(request,"Yanlış Kullanıcı Adı veya Parola")
            return render(request,"login.html",context)
        else:
            login(request,user)
            messages.success(request,"Başarıyla Giriş Yaptınız")
            return redirect("index")
    
        
    return render(request,"login.html",context)

def logoutUser(request):

    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")

