from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from litreview import forms

def login_page(request):
    form = forms.LoginForm()
    message = ""

    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                message = "Identifiants incorrects."
    
    context = {
        "form": form,
        "message": message
    }

    return render(request, "litreview/login.html", context=context)


def logout_user(request):
    logout(request)
    return redirect("login")


def home(request):
    return render(request, "litreview/home.html")


def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    
    return render(request, "litreview/signup.html", context={"form": form})
