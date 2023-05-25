from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = 'home/index.html'


def change_view(request):
    language_code = request.path[1:3]
    redirect_path = request.get_full_path()[3:]
    print(redirect_path)
    if language_code == 'fa':
        return redirect('/en/')

    return redirect('/fa/')

