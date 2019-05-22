from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('add/catalog/', views.addcat, name='addcat'),
    path('add/item/', views.addshop, name='addshop'),
    path('login/', views.auth_login, name='auth_login'),
    path('register/', views.auth_register, name='auth_register'),
    path('logout/', views.auth_logout, name='auth_logout'),
]