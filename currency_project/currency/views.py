from django.views.generic import TemplateView
from django.http import Http404
from .models import ExchangeRate
from datetime import datetime


class ShowRatesView(TemplateView):
    template_name = 'show_rates.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_str = self.request.GET.get('date')

        if not date_str:
            raise Http404("Date parameter is missing")

        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise Http404("Invalid date format. Use YYYY-MM-DD format.")

        rates = ExchangeRate.objects.filter(date=date_obj).select_related('currency')

        if not rates.exists():
            context['no_rates'] = True
        else:
            context['rates'] = rates

        context['date'] = date_obj

        return context
