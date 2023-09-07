from django.contrib import admin
from .models import Category, Trayectoria
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Category, CategoryAdmin)
class TrayectoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author')
    search_fields=('author__username',)
    list_filter=('categories__name',)
admin.site.register(Trayectoria, TrayectoriaAdmin)