# FoodGram Project

FoodGram - это социальная сеть для публикации рецептов. Неавторизированные пользователи могут посмотреть рецепты на сайте. Авторизированные пользователи могут добавлять свои рецепты, добавлять рецепты в избранное, подписываться на авторов, добавлять рецепты в корзину и скачать количество нужных игредиентов в формате pdf. Это пригодится при походе в магазин!

## Подготовка и запуск проекта

- Склонировать репозиторий на локальную машину:

```
git clone https://github.com/Ascurse/foodgram-project-react
```

- Перейдите в папку infra и запустите docker-compose

```
sudo docker-compose up -d --build
```

- После успешного завершения сборки выполните команды:
  - Соберите статические файлы:
  ```
  sudo docker-compose exec backend python manage.py collectstatic --noinput
  ```
  - Примените миграции:
  ```
  sudo docker-compose exec backend python manage.py migrate --noinput
  ```
  - Загрузите ингридиенты в базу данных:
  ```
  sudo docker-compose exec backend python manage.py load_ingredients
  ```
  - Создать суперпользователя Django:
  ```
  sudo docker-compose exec backend python manage.py createsuperuser
  ```
  - Проект станет доступен по адресу localhost/recipes

## Деплой на удаленный сервер:

- Выполните вход на удаленный сервер.
- Установите docker на удаленный сервер:

```
sudo apt install docker.io
```

- Установите docker-compose на удаленный сервер:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

- Локально отредактируйте файл infra/nginx/default.conf и в строке server_name впишите свой IP
- Скопируйте файлы docker-compose.yml и nginx/default.conf из директории infra на сервер:

```
scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
```

- Cоздайте .env файл и впишите:

```
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных Postgres>
DB_USER=<имя пользователя Postgres>
DB_PASSWORD=<пароль Postgres>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<секретный ключ django>
```

- Запустите docker-compose

```
sudo docker-compose up -d --build
```

- После успешного завершения сборки выполните команды:

  - Соберите статические файлы:

  ```
  sudo docker-compose exec backend python manage.py collectstatic --noinput
  ```

  - Примените миграции:

  ```
  sudo docker-compose exec backend python manage.py migrate --noinput
  ```

  - Загрузите ингридиенты в базу данных:

  ```
  sudo docker-compose exec backend python manage.py load_ingredients
  ```

  - Создать суперпользователя Django:

  ```
  sudo docker-compose exec backend python manage.py createsuperuser
  ```

  - Проект станет доступен по адресу <ip адрес сервера>/recipes

  ## Данный проект доступен по адресу:

  http://84.201.141.69/recipes

  - Логин: admin
  - Пароль: admin
