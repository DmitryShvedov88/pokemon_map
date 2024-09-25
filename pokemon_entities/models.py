from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name="Name", max_length=200,)
