# 2024-djreact-multivendorecom
Membuat multivendor ecommerce menggunakan Django dan React


## 01. SETUP

#### 1. Create and clone repository

        modified:   .gitignore
        modified:   README.md

#### 2. Install django and other requirements

        > pip install django==4.2.7 djangorestframework==3.14.0 django-cors-headers==3.14.0 djangorestframework-simplejwt==5.2.2 PyJWT==2.6.0
        > pip freeze>requirements.txt

        modified:   .gitignore
        modified:   README.md
        new file:   backend/requirements.txt


## 02. DJANGO PROJECT & APPS

#### 1. Create proyek django 'config'

        modified:   README.md
        new file:   backend/config/__init__.py
        new file:   backend/config/asgi.py
        new file:   backend/config/settings.py
        new file:   backend/config/urls.py
        new file:   backend/config/wsgi.py
        new file:   backend/manage.py

#### 2. Create some django apps

        modified:   README.md
        renamed:    backend/config/__init__.py -> config/__init__.py
        renamed:    backend/config/asgi.py -> config/asgi.py
        renamed:    backend/config/settings.py -> config/settings.py
        renamed:    backend/config/urls.py -> config/urls.py
        renamed:    backend/config/wsgi.py -> config/wsgi.py
        new file:   customer/__init__.py
        new file:   customer/admin.py
        new file:   customer/apps.py
        new file:   customer/migrations/__init__.py
        new file:   customer/models.py
        new file:   customer/tests.py
        new file:   customer/views.py
        renamed:    backend/manage.py -> manage.py
        renamed:    backend/requirements.txt -> requirements.txt
        new file:   store/__init__.py
        new file:   store/admin.py
        new file:   store/apps.py
        new file:   store/migrations/__init__.py
        new file:   store/models.py
        new file:   store/tests.py
        new file:   store/views.py
        new file:   userauths/__init__.py
        new file:   userauths/admin.py
        new file:   userauths/apps.py
        new file:   userauths/migrations/__init__.py
        new file:   userauths/models.py
        new file:   userauths/tests.py
        new file:   userauths/views.py
        new file:   vendor/__init__.py
        new file:   vendor/admin.py
        new file:   vendor/apps.py
        new file:   vendor/migrations/__init__.py
        new file:   vendor/models.py
        new file:   vendor/tests.py
        new file:   vendor/views.py

#### 3. Register the apps to config/settings.py

        modified:   README.md
        modified:   config/settings.py


## 03. DATABASE

#### 1. Create Postgres database and connect it with the project

        modified:   README.md
        modified:   config/settings.py

#### 2. Protecting sensitive file

        modified:   README.md
        modified:   config/settings.py

        :)

#### 3. Create .env.example file

        modified:   README.md

#### 4. Run migrations and createsuperadmin

        (venv312422) λ python manage.py createsuperuser
        Username (leave blank to use 'ing'): superadmin
        Email address: superadmin@mail.com
        Password:superadmin@mail.com
        Password (again):superadmin@mail.com

        modified:   README.md

        Note: superadmin sukses login :)


## 04. DJANGO-JAZZMIN MODULE

#### 1. Install django-jazzmin and configure it

        new file:   .env.example
        modified:   README.md
        modified:   config/settings.py


## 05. STATIC AND MEDIA FILES

#### 1. Configure path for static files

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
