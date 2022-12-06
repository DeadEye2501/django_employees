### Используемый стек:

- `django`
- `bootstrap`
- `postgresql`

### Для развёртывания приложения необходимо:

- клонировать репозиторий: git clone https://github.com/DeadEye2501/django_employees.git
- установить `postresql` и создать пустую базу данных с именем `django_employees_db`
- прописать в переменных окружения:
  - `SECRET_KEY`: `django-insecure-x*3l8ot%qgwq@nlni+_)oj1zb)bi3@z8e7=yg(1lc64xt+cuzw`
  - `SQL_PASSWORD`: тут нужно указать ваш пароль от базы
  - `SQL_USER`: нужно указать, если имя пользователя отлично от `postgres`
  - возможно вам будет нужно также указать какие-то дополнительные настройки для базы
- создать витуальное окружение и устаносить пакеты из `requirements.txt`
- в корневой папке проекта выполнить команду `python manage.py migrate` для создания структуры базы и заполнения ее данными
- создать суперпользователя командой `python manage.py createsuperuser` для доступа в административной части проекта
- выполнить команду `python manage.py collectstatic`
- для запуска сервера выпнить команду `python manage.py runserver`, после чего сервер должен стать доступен на локальном
хосте на 8000 порте
