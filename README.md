# FoodGram Project

FoodGram - это социальная сеть для публикации рецептов. Неавторизированные пользователи могут посмотреть рецепты на сайте. Авторизированные пользователи могут добавлять свои рецепты, добавлять рецепты в избранное, подписываться на авторов, добавлять рецепты в корзину и скачать количество нужных игредиентов в формате pdf. Это пригодится при походе в магазин!

## Подготовка и запуск проекта

### Склонировать репозиторий на локальную машину:

```
git clone https://github.com/Ascurse/foodgram-project-react
```

## Перейдите в папку infra и запустите docker-compose

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
