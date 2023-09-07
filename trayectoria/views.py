from django.shortcuts import render, get_object_or_404
from .models import Trayectoria, Category
# Create your views here.
def trayectoria(request):
    trayectorias=Trayectoria.objects.all()
    return render(request,"trayectoria/trayectoria.html",{'listTrayectoria':trayectorias})
def category(request,categoryId):
    category=get_object_or_404(Category, id=categoryId)
    trayectorias=Trayectoria.objects.filter(categories=category)
    return render(request, "trayectoria/category.html",{'listTrayectoria':trayectorias})