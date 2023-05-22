from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def main_page(request):
    redirect = reverse('index')
    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect)

    return render(request, 'task_app/index.html')



def login_user(request):
    context = {
        'forms': AuthenticationForm()
    }
    redirect = reverse('index')
    redirect_lose = reverse('login')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirect)
        else:
            return HttpResponseRedirect(redirect_lose)
    else:
        return render(request, 'profile_app/login.html', context=context)



def register_user(request):
    redirect = reverse('index')
    context = {
        'forms': UserCreationForm()
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(redirect)


    return render(request, 'profile_app/register.html', context=context)





def logout_user(request):
    redirect = reverse('main_page')
    logout(request)
    return HttpResponseRedirect(redirect)



# git push origin https://github.com/Kapitan21oo/task_manager



