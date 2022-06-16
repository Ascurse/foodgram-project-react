from django.core.exceptions import ValidationError


def validate_cooking_time(value):
    if value < 1:
        raise ValidationError(
            'Время приготовления не может быть меньше 1 минуты')
    else:
        return value


def validate_ingredient_amount(value):
    if value < 1:
        raise ValidationError(
            'Количество ингредиента не может быть меньше 1!'
        )
    else:
        return value
