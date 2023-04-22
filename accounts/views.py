from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView, View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, LoginForm


# Create your views here.
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form': form,
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')

            else:
                form.add_error('phone', 'Wrong phone number or password!')

        else:
            form.add_error('phone', 'Invalid Data!!')

        return render(request, 'accounts/login.html', {
            'form': form,
        })



