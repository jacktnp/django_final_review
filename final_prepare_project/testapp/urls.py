from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('add/catalog/', views.addcat, name='addcat'),
    path('add/item/', views.addshop, name='addshop'),
]