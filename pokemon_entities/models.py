from django.db import models  # noqa F401


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

    def __str__(self):
        if self.pokemon.title:
            return self.pokemon.title
        return f'{self.pokemon.title} (Не существует)'
