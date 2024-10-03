from django.db import models  # noqa F401
from datetime import datetime

class Pokemon(models.Model):
    """Пукемон"""
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(verbose_name="Name", max_length=200,)
    photo = models.ImageField(upload_to='Photo', null=True)

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
