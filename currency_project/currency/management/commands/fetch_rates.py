import requests
from typing import Any
from django.core.management.base import BaseCommand, CommandError
from currency.models import Currency, ExchangeRate
from datetime import date, datetime
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Fetches and saves currency exchange rates from CBR'

    def handle(self, *args: Any, **kwargs: Any) -> None:
        url: str = 'https://www.cbr-xml-daily.ru/daily_json.js'
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Error fetching data from {url}: {e}")
            raise CommandError(f"Error fetching data from {url}: {e}")

        try:
            data = response.json()
        except ValueError as e:
            logger.error(f"Error parsing JSON response: {e}")
            raise CommandError(f"Error parsing JSON response: {e}")

        # Получение даты из JSON
        date_str: str = data['Date']
        try:
            date_obj: date = datetime.fromisoformat(date_str).date()
        except ValueError as e:
            logger.error(f"Error parsing date from JSON: {e}")
            raise CommandError(f"Error parsing date from JSON: {e}")

        self.update_exchange_rates(data['Valute'], date_obj)

        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved exchange rates'))

    def update_exchange_rates(self, valutes: dict[str, dict[str, Any]], date_obj: date) -> None:
        for char_code, details in valutes.items():
            currency, created = Currency.objects.get_or_create(
                char_code=details['CharCode'],
                defaults={'name': details['Name']}
            )
            ExchangeRate.objects.update_or_create(
                currency=currency,
                date=date_obj,
                defaults={'value': details['Value']}
            )
            action = 'Created' if created else 'Updated'
            logger.info(f"{action} exchange rate for {currency.name} on {date_obj}")
