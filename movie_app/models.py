from django.db import models

# python manage.py shell_plus --print-sql
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1_000_000)


    def __str__(self):
        return f'{self.name} - {self.rating}%'




