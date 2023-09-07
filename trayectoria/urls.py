from django.urls import path
from . import views as coreViews

urlpatterns = [
    path('', coreViews.trayectoria, name="trayectoria"),
    path('category/<int:categoryId>/', coreViews.category, name="category"),
]