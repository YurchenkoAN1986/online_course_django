Установи и создай вертуальное окружение 
python -m venv venv
source venv/Scripts/activate  - для Windows
source venv/bin/activate - для Linux

Установи зависимости 
python -m pip install --upgrade pip
pip install -r requirements.txt

Создай Супер пользователя 
python manage.py createsuperuser

Запустите проект 
python manage.py runserver

список продуктов 
http://127.0.0.1:8000/api/v1/products/
Оплата курса
POST http://127.0.0.1:8000/api/v1/products/<id>/pay/

список подписок 
http://127.0.0.1:8000/api/v1/subscriptions/

управление балансом пользовотелей 
http://127.0.0.1:8000/api/v1/balances/
