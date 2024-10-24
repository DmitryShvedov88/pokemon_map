from django.db import models  # noqa F401
from datetime import datetime

class Pokemon(models.Model):
    """Пукемон"""
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200, verbose_name="Имя", blank=True, null=True)
    title_en = models.CharField(max_length=150, verbose_name="Имя_англ", blank=True, null=True)
    title_jp = models.CharField(max_length=150, verbose_name="Имя_япон", blank=True, null=True)
    photo = models.ImageField(verbose_name="Фото", blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Описание покемона")
    evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Текущая эволюция", related_name="next_evolutions")

    def __str__(self):
        if self.title:
            return self.title
        return f'{self.title} (Не существует)'

class PokemonEntity(models.Model):
    """Характеристика покемона"""
    pokemon = models.ForeignKey(Pokemon, verbose_name="Покемон", on_delete=models.CASCADE, related_name="entities")
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Время появления")
    disappeared_at = models.DateTimeField(verbose_name="Время исчезновения")
    level = models.IntegerField(verbose_name="Уровень", null=True, blank=True)
    health = models.IntegerField(verbose_name="Здоровье", null=True, blank=True)
    attack = models.IntegerField(verbose_name="Атака", null=True, blank=True)
    protection = models.IntegerField(verbose_name="Защита", null=True, blank=True)
    endurance = models.IntegerField(verbose_name="Выносливость", null=True, blank=True)

    def __str__(self):
        if self.pokemon.title:
            return self.pokemon.title
        return f'{self.pokemon.title} (Не существует)'



# python manage.py shell
# from pokemon_entities.models import Pokemon, PokemonEntity
#pokemons = Pokemon.objects.all()  

# print(pokemons[0].photo.url)