## Установка
1. **Клонируйте репозиторий:**
 ```
 git clone https://github.com/your-username/currency_project.git
 cd currency_project
 ```
2. **Клонируйте репозиторий:**
```
python -m venv venv
source venv/bin/activate ## для Windows используйте venv\Scripts\activate
```
3. **Установите зависимости:**
  ```
  pip install -r requirements.txt
```
## Настройка
1. **Создайте и примените миграции:**
```
python manage.py makemigrations
python manage.py migrate
```
2. **Создайте суперпользователя:**
```
python manage.py createsuperuser --email admin@admin.com --username admin
```
3. **Запустите сервер разработки:**
```
python manage.py runserver
```

## Использование
Для обновления списка валют введите команду
```
python manage.py fetch_rates
```
Просмотр курсов валют
Перейдите по адресу:
```
http://127.0.0.1:8000/show_rates?date=YYYY-MM-DD
```
Замените YYYY-MM-DD на нужную дату, например:
```
http://127.0.0.1:8000/show_rates?date=2023-01-01
```





