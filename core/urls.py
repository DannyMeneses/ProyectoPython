from django.urls import path
from . import views as coreViews
from product import views as productViews
from store import views as storeViews
urlpatterns = [
    path('', coreViews.index, name="index"),
    path('contact/', coreViews.contact, name="contact"),
    path('terminos/', coreViews.terminos, name="terminos"),
]