from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"core/index.html")
def contact(request):
    return render(request,"core/contact.html")
def terminos(request):
    return render(request,"core/terminos.html")


