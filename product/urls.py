from django.urls import path
from . import views as productViews
urlpatterns = [
    path('', productViews.product, name="product"),
]