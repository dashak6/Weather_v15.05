### Запуск

* #### Создать и активировать виртуальное окружение:
        virualenv venv
        source venv/bin/activate
* #### Установить зависимости:
        pip install -r requirements.txt
* #### Выбрать нужную БД в файле settings.py
        DATABASES = DB_SETTINGS["POSTGRES" or "SQLITE"]  
        По-умолчанию: DATABASES = DB_SETTINGS["POSTGRES"]
* #### Запустить миграции:
        python3 manage.py makemigrations
        python3 manage.py migrate

* #### Создать суперпользователя:
        python3 manage.py createsuperuser

* #### Запустить сервер:
        python3 manage.py runserver
  
### BASIC ENDPOINTS
        127.0.0.1:8000/admin - админка
        127.0.0.1:8000/meteo - главное меню
