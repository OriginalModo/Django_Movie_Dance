from django.contrib import admin
from .models import *
from django.db.models import QuerySet  # Можно добавлять к аннотациям


admin.site.register(Director)
admin.site.register(Actor)

# Создание фильтра в Django Admin
class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        return queryset


@admin.register(Movie)
class ModelNameAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name', )}                             # Авто-заполнение slug в Админке
    # fields = ['name', 'rating', 'year', 'slug']                # Какие поля можно добавлять в Админке
    # exclude = ['name', 'rating']                                         # Тоже самое но исключаем
    # readonly_fields = ['name']                                           # Только для чтения поля
    list_display = ['name', 'rating', 'director', 'budget']   # Какие поля будут отображатся в Админке
    list_editable = ['rating', 'director', 'budget']               # Какие поля можно редактировать в Админке
    ordering = ['-rating', '-name']                                         # По Каким полям будет Сортировка в Админке
    search_fields = ['name__startswith', 'rating']     # Создание поисковой панели в Админке Можно использовать lookups
    list_filter = ['name', RatingFilter]                                   # фильтрация Можно добавить самописный класс

    # Можно добавлять методы в list_display
    @admin.display(ordering='rating', description='status')
    def rating_status(self, movie: Movie):
        match movie.rating:
            case x if movie.rating < 50:
                return 'Зачем это смотреть'
            case x if movie.rating < 70:
                return 'Разок можно глянуть'
            case x if movie.rating <= 85:
                return 'Зачет'
            case _:
                return 'Топчик'

