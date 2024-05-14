from django.urls import path
from .views import ShowRatesView

urlpatterns = [
    path('show_rates', ShowRatesView.as_view(), name='show_rates'),
]
