from asyncio import constants
from django.contrib.auth import get_user_model
from django.db import models
from django.core import validators
from django.shortcuts import get_object_or_404

User = get_user_model()


class Ingridient(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название ингридиента'
    )
    measurement_unit = models.CharField(
        max_length=50,
        verbose_name='Единица измерения'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        constraints = [
            models.UniqueConstraint(fields=['name', 'measurement_unit'],
                                    name='unique_ingridient')
        ]

    def __str__(self):
        return self.name


class Tag(models.Model):
    RED = '#ff0000'
    BLUE = '#0000ff'
    YELLOW = '#ffff00'
    GREEN = '#008000'
    ORANGE = '#ffa500'
    PINK = '#ffc0cb'

    COLOR_CHOICES = [
        (RED, 'Красный'),
        (BLUE, 'Синий'),
        (YELLOW, 'Желтый'),
        (GREEN, 'Зелёный'),
        (ORANGE, 'Оранжевый'),
        (PINK, 'Розовый')
    ]
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название тэга'
    )
    color = models.CharField(
        max_lenght=7,
        unique=True,
        choices=COLOR_CHOICES,
        verbose_name='Цвет тэга'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Уникальный слаг тэга'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэги',
        related_name='recipes',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Создатель рецепта',
        related_name='recipes',
    )
    ingridients = models.ManyToManyField(
        Ingridient,
        through='IngridientAmount',
        verbose_name='Ингридиенты',
        related_name='recipes',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название рецепта',
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='Изображение рецепта',
    )
    text = models.TextField(
        verbose_name='Описание рецепта',
    )
    cooking_time = models.PositiveIntegerField(
        validators=(validators.MinValueValidator(
            1, message='Время приготовление не может быть меньше 1 минуты'
        ),),
        verbose_name='Время приготовления в минутах'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
    

class IngridientAmount(models.Model):
    ingridient = models.ForeignKey(
        Ingridient,
        on_delete=models.CASCADE,
        verbose_name='Ингридиент'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )
    amount = models.PositiveSmallIntegerField(
        validators=(
            validators.MinValueValidator(
                1, message='Количество ингридиентов не может быть меньше 1'
            ),)
            verbose_name='Количество',
        )
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Количество ингридиентов'
        constants = [
            models.UniqueConstraint(fields=['ingridient', 'recipe'],
                                    name='unique ingridients recipe')
        ]


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Избранное'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique favorite recipe')
        ]

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='cart',
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        related_name='cart'
        on_delete=models.CASCADE,
    )