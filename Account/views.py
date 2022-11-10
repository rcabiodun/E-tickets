from django.shortcuts import render,redirect
from .forms import Createuserform
from django.contrib import messages
from django.contrib.auth import authenticate,login
from Home.decorators import authenticatedusers
from .forms import ProfileForm
from .models import Profile
# Create your views here.
@authenticatedusers
def Signin (request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"Username or password is found to be incorrect :(")

    return render(request,"Account/sign-in.html")



@authenticatedusers
def Signup(request):
    form = Createuserform()
    if request.method == "POST":
        form = Createuserform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")

            messages.success(request, "Account was created for  " + username)
            return redirect(Signin)

    context = {
        "form": form,

    }
    return render(request, "Account/sign-up.html", context)

def Profile_reg(request):
    try:
        pro=request.user.profile
    except Profile.DoesNotExist:
        pro=Profile(user=request.user)

    form=ProfileForm(instance=pro)


    if request.method =="POST":
        form=ProfileForm(request.POST,instance=pro)
        if form.is_valid():
            form.save()
            return redirect(Profile_reg)

    return render(request, "Account/profile registration.html", {"form":form})
