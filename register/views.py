from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,logout, login  as dj_login
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():  
                data = form.cleaned_data
                user = authenticate(request,
                username = data['username'],
                password = data['password']
                )
                if user is not None:
                    if user.is_active:
                        dj_login(request,user)
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        return HttpResponse("<h2>Sizning akkauntingiz faol emas</h2>")
                else:
                    
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])           
        else:
            form = LoginForm()
            context = {
                'form' : form,    
            }
        return render(request, 'register/login.html',context)
    else:
        return HttpResponseRedirect(reverse('index'))
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UserRegistrationForm(data=request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(
                    user_form.cleaned_data['password']
                )
                new_user.save()
                return HttpResponseRedirect(reverse('login'))
        else:
            user_form = UserRegistrationForm()
        context = {'user_form': user_form}
        return render(request, 'register/register.html',context)
    else:
        return HttpResponseRedirect(reverse('profile'))
def logout_reply(request):
    logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

