from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/login.html', {'error_message': 'Invalid email or password'})
    return render(request, 'user/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})


def logout(request: HttpRequest):
    logout(request)
    redirect1 = reverse_lazy("list")
    return HttpResponseRedirect(redirect1)
