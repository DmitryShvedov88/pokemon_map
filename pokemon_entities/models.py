from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name="Name", max_length=200,)
    photo = models.ImageField(upload_to='Photo', null=True)
    def __str__(self):
        if self.title:
            return self.title
        return f'{self.title} (inactive)'