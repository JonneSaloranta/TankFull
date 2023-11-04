from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        'form': form,
    }
    return render(request, "login.html", context)

def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    print(request.POST)
    print(form.errors)
    print(form.is_valid())
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        
        new_user = authenticate(email=user.email, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")
    
    context = {
        'form': form,
    }
    return render(request, "register.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")