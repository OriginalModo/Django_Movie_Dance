from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    def get_url(self):
        return reverse_lazy('one_director', args=(self.id, ))



class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)


    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер{self.first_name} - {self.last_name}'

        return f'Актриса {self.first_name} - {self.last_name}'

    def get_url(self):
        return reverse_lazy('one_actor', args=(self.id, ))

# python manage.py shell_plus --print-sql
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1_000_000, blank=True, validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actors = models.ManyToManyField(Actor)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.rating}%'

    def get_url(self):
        return reverse_lazy('one_movie', args=(self.slug, ))



