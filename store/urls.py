from django.urls import path
from . import views as storeViews
urlpatterns = [
    path('', storeViews.store, name="store"),
]