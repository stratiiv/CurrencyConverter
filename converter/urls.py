from django.urls import path
from . import views


urlpatterns = [
    path('', views.CurrencyConversionView.as_view(), name="convert")
]