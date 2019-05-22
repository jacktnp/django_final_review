from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    context = {}
    return render(request, template_name='testapp/home.html', context=context)