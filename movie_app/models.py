from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.core.validators import MaxLengthValidator, MinValueValidator


# python manage.py shell_plus --print-sql
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxLengthValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1_000_000, blank=True, validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.rating}%'

    def get_url(self):
        return reverse_lazy('one_movie', args=(self.slug, ))



