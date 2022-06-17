from django.contrib import admin

from .models import Cart, Favorite, Ingredient, IngredientAmount, Recipe, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color', )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit', )
    search_fields = ['name', 'measurement_unit']


class IngredientsInlineAdmin(admin.TabularInline):
    model = Recipe.ingredients.through


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tags', 'name',
                           'author', 'image', 'text', 'cooking_time']}),
    ]
    inlines = (IngredientsInlineAdmin,)
    list_display = ('name', 'author', 'count_favorites')
    list_filter = ('author', 'name', 'tags', )

    def count_favorites(self, obj):
        return obj.favorites.count()

    count_favorites.short_description = 'Число добавлений в избранное'


admin.site.register(Cart)
admin.site.register(Favorite)
admin.site.register(IngredientAmount)
