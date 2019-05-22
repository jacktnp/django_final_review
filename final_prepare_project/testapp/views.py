from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group, User

from .forms import CatalogForm, ShopForm, SignupForm
from .models import Catalog


def is_manager(user):
    return user.groups.filter(name='manager').exists()

def home(request):
    context = {}

    return render(request, template_name='testapp/home.html', context=context)

@login_required
@permission_required('catalog.change_catalog')
def catalog(request):
    catalog = Catalog.objects.all()

    context = {
        'catalog_num': len(Catalog.objects.all()),
        'catalog': catalog
    }

    return render(request, template_name='testapp/home.html', context=context)

def addcat(request):
    context = {}
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            add_cat = form.save(commit=False)
            add_cat.save()
            return redirect('catalog')
    else:
        form = CatalogForm()

    context['form'] = form
    return render(request, 'testapp/add-catalog.html', context=context)


def addshop(request):
    context = {}
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            add_shop = form.save(commit=False)
            add_shop.save()
            return redirect('catalog')
    else:
        form = ShopForm()

    context['form'] = form
    return render(request, 'testapp/add-shop.html', context=context)



def auth_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                if request.user.is_staff:
                    return redirect('/admin')
                elif is_manager(user):
                    return redirect('addcat')
                else:
                    return redirect('catalog')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='testapp/login.html', context=context)

def auth_logout(request):
	logout(request)
	return redirect('auth_login')

#สมัครสมาชิก
def auth_register(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='manager')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            raw_pass = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_pass)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('catalog')
    else:
        form = SignupForm()

    context['form'] = form
    return render(request, template_name='testapp/register.html', context=context)
