from django.db import models  # noqa F401
from datetime import datetime

class Pokemon(models.Model):
    """Пукемон"""
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200, verbose_name="Name", blank=True, null=True)
    title_en = models.CharField(max_length=150, verbose_name="Name_en", blank=True, null=True)
    title_jp = models.CharField(max_length=150, verbose_name="Name_jp", blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Описание покемона")
    evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Текущая эволюция", related_name="next_evolution")

    def __str__(self):
        if self.title:
            return self.title
        return f'{self.title} (Не существует)'

class PokemonEntity(models.Model):
    """Характеристика покемона"""
    pokemon = models.ForeignKey(Pokemon, verbose_name="Покемон", on_delete=models.CASCADE, related_name="entities")
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    appeared_at = models.DateTimeField("Время появления")
    disappeared_at = models.DateTimeField("Время исчезновения")
    level = models.IntegerField("Уровень", null=True, blank=True)
    health = models.IntegerField("Здоровье", null=True, blank=True)
    attack = models.IntegerField("Атака", null=True, blank=True)
    protection = models.IntegerField("Защита", null=True, blank=True)
    endurance = models.IntegerField("Выносливость", null=True, blank=True)

    def __str__(self):
        if self.pokemon.title:
            return self.pokemon.title
        return f'{self.pokemon.title} (Не существует)'



# python manage.py shell
# from pokemon_entities.models import Pokemon, PokemonEntity
#pokemons = Pokemon.objects.all()  

# print(pokemons[0].photo.url)