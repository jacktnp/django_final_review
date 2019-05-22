from django.contrib import admin
from .models import Catalog, Shop
from django.contrib.auth.models import Permission

admin.site.register(Permission)


class CatalogAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']

  fieldsets = [
    ('ประเภทหนังสือ', {'fields': ['name']})
  ]


admin.site.register(Catalog, CatalogAdmin)

class ShopAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'catalog']
  list_per_page = 10
  readonly_fields = ['catalog']
  search_fields = ['title', 'catalog']

  fieldsets = [
    ('สินค้า', {'fields': ['title']}),
    ('แคตาลอก', {'fields': ['catalog']})
  ]

admin.site.register(Shop, ShopAdmin)