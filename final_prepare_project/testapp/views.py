from django.shortcuts import render, redirect
from django.http import HttpResponse
#ตัวอย่างโค้ด
def user_home(request):
    context = {}
    return render(request, template_name='testapp/home.html', context=context)