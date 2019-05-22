from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CatalogForm
from .models import Catalog


def home(request):
    context = {}

    return render(request, template_name='testapp/home.html', context=context)

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