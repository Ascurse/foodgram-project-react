import json
import os

from api.models import Ingredient
from django.conf import settings
from django.core.management.base import (BaseCommand, CommandError,
                                         CommandParser)
from django.db.utils import IntegrityError

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    help = 'loading ingredients'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            'filename', default='ingredients.json', nargs='?', type=str)

    def handle(self, *args, **options):
        try:
            with open(os.path.join(
                DATA_ROOT, options['filename']), 'r', encoding='utf-8'
            ) as f:
                data = json.load(f)
                for ingredient in data:
                    try:
                        Ingredient.objects.create(
                            name=ingredient['name'],
                            measurement_unit=ingredient['measurement_unit'])
                    except IntegrityError:
                        print(f'Ингредиент {ingredient["name"]} '
                              f'{ingredient["measurement_unit"]} '
                              f'уже присутствует в базе!')
        except FileNotFoundError:
            raise CommandError('Запрашиваемый файл отсутствует')
