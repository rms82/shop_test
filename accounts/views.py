from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.views.generic import CreateView, TemplateView, View
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string
from .models import OTP, CustomUser
from .forms import CustomUserCreationForm, LoginForm, RegisterForm, OTPForm
import ghasedakpack
from random import randint


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
                form.add_error('phone', _('Wrong phone number or password!'))

        return render(request, 'accounts/login.html', {
            'form': form,
        })


class SignUpView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {
            'form': form,
        })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if CustomUser.objects.filter(phone=phone).exists():
                form.add_error('phone',
                               _('User with this number already exists!!')
                               )

            else:
                code = randint(1111, 9999)
                token = get_random_string(10)

                SMS = ghasedakpack.Ghasedak("55fb92ff6575008a7ce1e94355fecacc1aba3bfcfe8939e54cf7adb49bcdd0af")
                # SMS.verification(
                #     {'receptor': phone, 'type': '1', 'template': 'testshop', 'param1': code})

                OTP.objects.create(phone=phone, otp=code, token=token)
                return redirect('checkcode', token=token)

        return render(request, 'accounts/register.html', {
            'form': form,
        })


class CheckCodeView(View):
    def get(self, request, token):
        otp = get_object_or_404(OTP, token=token)
        form = OTPForm()

        return render(request, 'accounts/check_code.html', {
            'form': form
        })

    def post(self, request, token):
        form = OTPForm(request.POST)
        if form.is_valid():
            otp = get_object_or_404(OTP, otp=form.cleaned_data['code'], token=token)
            CustomUser.objects.create_user(phone=otp.phone, password=form.cleaned_data['password'])
            otp.delete()

            return redirect('home')

        return render(request, 'accounts/check_code.html', {
            'form': form,
        })


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)

        return redirect('home')
