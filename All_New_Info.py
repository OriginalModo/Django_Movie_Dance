"""

 При запуске  python manage.py runserver
 http://127.0.0.1:8000/ - Означает вашу локальную машину или  localhost
 http://localhost:8000/ - Тоже самое

 # В терминале  вводим  where python
 where python - покажет список всех существующих Интерпретаторов Python.
  Первый в списке тот который запускается. Тот который в списке выше и будет запускатся

 python название_файла.py  - Запуск файла в терминале

 (venv) - Если вначале Терминала стоит строчка  (venv) значит используется Виртуальное Окружение

 Другой кнопкой мышки на проект и выбираем Reload from disk - Обновить папку вручную


 Чтобы выполнять команды нужно Быть в той же папке на том же уровне или используем команду cd

    -- командная строка cmd   Terminal commands --
 dir - Отображение файлов и папок в текущем каталоге
 cd - Изменить каталог, если нажать Tab будет автодополнение
 cd .. - переход на 1 папку назад
 cd ..\.. - переход на 2 папки назад
 cd \ - Переход в корневую директорию
 cd . - Переход в текущую директорию (никаких изменений)


 cd папка\папка\папка   -  Быстрый переход за одну операцию
 cd "имя имя"  - если между именами пробел
 cd "Абсолютный путь" - Сразу перейдем туда куда нужно
 Название_Диска: - чтобы сменить диск  - Примеры C:  D:  Только название диска и двоеточие в терминале(командной строке)

 mkdir - создание папки


  Все команды:    python manage.py --help    или просто  python manage.py
                  django-admin --help        или просто  django-admin
  python manage.py collectstatic -   Проверка статики
  python manage.py makemigrations - Проверка миграции
  python manage.py migrate - Применить миграции
  django-admin startproject - Создание проекта
  python manage.py startapp - Создание приложения
  python manage.py runserver - Запуск сервера для разработки
  python manage.py createsuperuser - Создать аккаунт администратора


 Чтобы запускать несколько серверов прописываем разные порты в  Edit Configurations... runserver 8000   runserver 8001
 или через Django Server  в  Edit Configurations


 --- ПО Поводу добавления приложения в settings.py  INSTALLED_APPS ---
 Ведь автор говорил, что нужно добавлять в settings.py имя добавляемого приложения. Я создал приложение blog и
 НЕ добавил его в INSTALLED_APPS, но всё-равно всё функционирует.

 В большинстве документации просто говорится, что нужно добавить имя каждого приложения в массив INSTALLED_APPS в
 настройках проекта Django. В чем преимущество/цель этого? Какую другую функциональность я получу,
 если создам 2 приложения, но включу в массив INSTALLED_APPS только имя одного?

 Django использует INSTALLED_APPS список всех мест для поиска моделей, команд управления, тестов и других утилит.

 Если вы создали два приложения (скажем, myappи myuninstalledapp), но только одно из них указано в INSTALLED_APPS,
 вы заметите следующее поведение:

 1) Модели, содержащиеся в , myuninstalledapp/models.pyникогда не вызовут изменений миграции (или не сгенерируют
 начальные миграции). Вы также не сможете взаимодействовать с ними на уровне базы данных, поскольку их таблицы никогда не будут созданы.

 2) Статические файлы, перечисленные внутри, myapp/static/будут обнаружены как часть collectstatic или службы
 статических файлов тестового сервера, но myuninstalledapp/staticфайлы не будут обнаружены.

 3) Тесты внутри myapp/tests.pyзапускались, но myuninstalledapp/tests.pyне работали.

 4) Команды управления, перечисленные в, myuninstalledapp/management/commands/не будут обнаружены.

 Так что на самом деле вы можете иметь папки в своем проекте Django, которые не являются установленными приложениями
 (вы даже можете создать их с помощью python manage.py startapp), но просто знайте, что некоторые утилиты
 автоматического обнаружения Django не будут работать для этого приложения.


 Подключить приложение в файле Основного проекта urls.py
  path('horoscope/', include('horoscope.urls')),

 # Весь файл urls.py основного проекта

 from django.contrib import admin
 from django.urls import path, include
 from debug_toolbar.toolbar import debug_toolbar_urls

 admin.site.site_header = 'Наша Админка'
 admin.site.index_title = 'Моя Супер Админка'

 urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('movie_app.urls')),
 ] + debug_toolbar_urls()

 # Весь файл urls.py Приложения
 from django.urls import path
 from .views import *

 urlpatterns = [
     path('', show_all_movie),
     path('movie/<slug:slug_movie>', show_one_movie, name='one_movie'),
 ]


 Конвертеры роутов Расположение важно Обработка роутов идет сверху вниз: Динамические url
 path(r'<str:sign_zodiac>/', get_info_sign_horoscope),            # Тип Строка
 path(r'<int:sign_zodiac>', get_info_sign_horoscope_by_number),   # Тип Число



 Располагаются они в модуле django.urls.converters
 DEFAULT_CONVERTERS = {
     'int': IntConverter(),
     'path': PathConverter(),
     'slug': SlugConverter(),
     'str': StringConverter(),
     'uuid': UUIDConverter(),
 }

 Также можно создавать свои собственные конвертеры
 class MyDateConverter:
     regex = '^(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](19|20)\d\d$'

     def to_python(self, value):
         return datetime.strptime(value, f'%d-%m-%Y')

     def to_url(self, value):
         # return value.strftime(f'%d-%m-%Y')
         return f'{value:%d-%m-%Y}'


 from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, ...

 HttpResponse - возвращает Ответ на Запрос.  статус код - 200
 HttpResponseNotFound - возвращает ошибку 404 и сообщение об ошибке Страница не найдена.  статус код - 404

    try:
        return HttpResponse(f'<h1>{dct[day]}</h1>')
    except:
        return HttpResponseNotFound(f'<h1>{day} не существует</h1>')

 HttpResponseRedirect - Перенаправление пользователя на другую страницу веб-сайта. статус код - 302

 def index(request):
    return HttpResponseRedirect('https://www.python.org')

 Функция redirect - также помогает выполнить перенаправление в Django.  статус код - 302

 from django.shortcuts import redirect

    def index(request):
      return redirect('https://www.python.org')


 Функция reverse - позволяет генерировать URL-адреса на основе имен URL-адресов в вашем приложении.

 from django.urls import reverse        # Тоже самое
 from django.shortcuts import reverse   # Тоже самое

 reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)

 # Передать можно коллекцию
 reverse('my_view', args=[1])
 reverse('my_view', args=(1, ))
 reverse('my_view', kwargs={'slug': 'hello-world'})


 # Имя нашего роута  Имя для URL-адреса
  path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),


 Тестирование unittest в Django

 В Django тесты определяются в специальном модуле tests.py внутри приложения.
 В файлике test пишем тесты

 # Пример
 from django.test import TestCase

 class TestHoroscope(TestCase):

    # Тест на статут кода
    def test_index(self):
        response = self.client.get('/horoscope/')  # client - Замена Браузера
        self.assertEqual(response.status_code, 200)

    # Тест на статут кода и перенаправление
    def test_libra_redirect(self):
        response = self.client.get('/7')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra/')

 # Затем в терминале пишем команду
 python manage.py test название_приложения   Или через   Edit Configurations Django tests   target == Приложение или все

 Типы проверок в классе TestCase
 assertEqual(a, b)          a == b
 assertNotEqual(a, b)       a != b
 assertTrue(x)              bool(x) is True
 assertFalse(x)             bool(x) is False
 assertIs(a, b)             a is b
 assertIsNot(a, b)          a is not b
 assertIsNone(x)            x is None
 assertIsNotNone(x)         x is not None
 assertIn(a, b)             a in b
 assertNotIn(a, b)          a not in b
 assertIsInstance(a, b)     isinstance(a, b)
 assertNotIsInstance(a, b)  not isinstance(a, b)


 BASE_DIR - Абсолютный путь к проекту
 'APP_DIRS': True, - Если установлено True, то Django будет искать в каждои установленном приложении папку  templates

 Коллизия (или конфликт) - это ситуация, когда два или более объекта (файлы, переменные, функции, и т.д.)
 имеют одно и то же имя или идентификатор.
 Чтобы не было коллизий прописываем отдельно для каждого приложения свой templates/имя_приложения

 Django Проверяет INSTALLED_APPS сверху вниз, Расположение приложений тоже имеет значение


 Функция render() возвращает объект HttpResponse, который представляет собой HTTP-ответ, содержащий сгенерированный
 HTML-код, созданный на основе указанного шаблона и переданных данных.

 Функция render принимает следующие аргументы:
 1) request(обязательный): объект HttpRequest, который представляет текущий HTTP-запрос, поступивший на сервер

 2) template_name(обязательный): имя шаблона, который будет использоваться для генерации HTML-страницы.
 Это может быть строка, содержащая имя файла шаблона, или список строк, содержащий несколько имен файлов шаблонов,
 которые будут использоваться в порядке приоритета.

 3) context(необязательный): словарь, содержащий данные, которые будут переданы в шаблон и использоваться для его
 рендеринга. Ключи словаря являются именами переменных в шаблоне, а значения - значениями этих переменных.

 4) content_type (необязательный) - строка, определяющая тип контента HTTP-ответа. По умолчанию content_type
  имеет значение "text/html"

 5) status - целое число, указывающее код состояния HTTP, который будет отправлен в ответ на HTTP-запрос.
 Это значение по умолчанию установлено на 200

 6) using - строка, указывающая имя базы данных, которую нужно использовать для выполнения запросов, если используется
 несколько баз данных. Это параметр может быть полезен, если вы хотите выполнить запрос на определенной базе данных
 вместо использования базы данных по умолчанию.

 # Ключ используется в шаблоне Jinja2 используем  {{ 'ключ' }}
 def get_info_about_sign_zodiac(request, sign_zodiac: str):
     description = zodiac_dict.get(sign_zodiac)
     data = {
         'description': description,
         'sign': sign_zodiac.title(),
         'my_int': 123,
         'my_float': 5.75,
         'my_list': 123,
         'my_tuple': 123,
         'my_dict': {'name': 'Jack', 'age': 40},
         'my_class': zodiac_dict,
     }
     return render(request, 'horoscope/info_zodiac.html', context=data)


 В браузере жмем Просмотреть код и чтобы было выбрано 'все' под словом Фильтр:
 - Элементы - просмотр html
 - Сеть
    - Заголовки - URL Запроса, Метод Запроса, Код Статуса и другие
    - Ответ - что выводит
 - И другие можно самостоятельно изучить

 Если Нет каких-то столбцов нажимаем на Столбец 'Название' и они появяться
 Ctrl + F5 - Обновить в Браузере чтобы Django Подхватил изменения

 Перед столбцом Элементы нажимаем на Стрелочку или Ctrl + Shift + C  можно просмотреть элемент (что влияет на страницу)


 Шаблонизатор Jinja2 в Django в Html
 пишем тег затем нажимаем Tab и тег сам сделаем {% if ...%} {% endif %} или другие операторы
 Теги и ссылка:
    {% for zod in zodiacks %}
        <li><a href="{% url 'horoscope_name' sign_zodiac=zod %}">{{ zod|title }}</a></li>
    {% endfor %}

  в html  Можно li*12 и нажать tab и будет 12 тегов сразу

 Фильтры шаблона:

 {{ variable|filter1|filter2|filter3 }}
 {{ variable|filter_name:param }}

 Использование фильтров вне шаблона:
 from django.template.defaultfilters import slugify

 title = "Some Title With Spaces!"
 slug = slugify(title)

 print(slug)  # -> some-title-with-spaces

 Наследование шаблонов. Теги block и extends

 {% block title %} {% endblock %}      # Блоки в базавом  html
 {{% block content %} {% endblock %}   # Блоки в базавом  html

 # Как можно наследовать базовый шаблоне html  Пишем в начале файла на первой строчке 1
 {% extends 'base.html' %}

 Тег include

 {% include "имя_шаблона.html" %}

 Можно запрещать доступ к контексту основного шаблона, тогда переменные не будут доступны.
 Делается это при помощи параметра only

 {% include "имя_шаблона.html" only %}

 Можно пробрасывать свои собственные переменные в шаблон
 {% include "имя_шаблона.html" with a=100 b=200 %}



 В settings
 на уровне проекта создаем папку static

 # Путь где будет искать Статические файлы: CSS, JavaScript, изображения и другие файлы.    Если его нет, то создаем
 STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

 Для подключения статики в html прописываем в первой строчке 1
 {% load static %}

 # link Обязательно должен быть внутри <head> </head>
<head>
 <link rel="stylesheet" href=" {% static 'имя_приложения/css/имя.css' %}">
</head>
 на уровне проекта создаем папку templates

 В константе TEMPLATES []  должна быть такая строчка она отвечает за, то где Django будет искать html
 'DIRS': [BASE_DIR / 'templates'],



 СУБД - Система управления Базами Данных
 Реляционные базы данных - SQL       - Все данных хранятся в виде Таблиц
 Строго структурированные (Есть привязки к типу донных)

 НЕ Реляционные базы данных - NOSQL  - Данные могут хранится различным способом
 НЕТ Строгой Структуры (НЕТ привязки к типу донных)
  - ключ-значение
  - графовые
  - документно-ориентированные
  - колоночные

 Реляционные (SQL):      Oracle, PostgreSQL, MariaDB, MySQL, SQLite (Из коробки)
 НЕ Реляционные (NOSQL): MongoDB(документо-ориентированная), Elasticsearch(документо-ориентированная), Redis(ключ-значение)
                         ClickHouse(колоночные) -   поддерживает язык запросов на основе SQL немного модифицированный

 ORM
 Таблица - Это Класс
 Записи в таблице - Это экземпляры класса


 # Создание столбцов через терминал
 Movie(name='XXX', rating=75).save()
 имя_модели(name='XXX', rating=75).save() # Сразу сохраняем

 Movie.objects.all()[:2] # Срезы
 Movie.objects.all()[-1] # ValueError: Negative indexing is not supported.   Отрицательные индексы не поддерживает

 # Изменение и удаление записей в таблице
 a = Movie.objects.all()[1]
 a.name           # Обращение к атрибуту
 a.name = 'HEHE'  # Изменение атрибута
 a.name = 'HEHE'  # Изменение атрибута
 a.delete()       # Удаление атрибута

 Movie.objects.create(name='Hehe')       # Без метода save() Сразу
 Movie.objects.filter(id__in=[1, 2, 3])  # Выбираем определенные id

 Фильтры запросов  Lookups
 # https://docs.djangoproject.com/en/5.0/ref/models/querysets/

 Movies.objects.filter(budget=1000)                         фильтр на равенство поля
 Movies.objects.filter(budget__gt=1000)                     фильтр на поле больше значения (great then)
 Movies.objects.filter(budget__lt=1000)                     фильтр на поле меньше значения
 Movies.objects.filter(budget__gte=1000)                    фильтр на поле больше либо равно значения
 Movies.objects.filter(budget__lte=1000)                    фильтр на поле меньше либо равно значения
 Movies.objects.exclude(budget=1000)                        фильтр на поле не равно значению
 Movies.objects.filter(year__isnull=True)                   фильтр на поле пустое (False - не пустое)
 Movies.objects.filter(year__isnull=True, name=’Avatar’)    фильтр на два поля
 Movies.objects.exclude(budget=1000).filter(name=’Avatar’)  фильтр на два поля
 Movies.objects.filter(name__contains=’Avatar’)             поле содержит значение, чувствителен к регистру
 Movies.objects.filter(name__icontains=’Avatar’)            поле содержит значение, не чувствителен к регистру
 Movies.objects.filter(name__startswith=’a’)                поле начинается с “a”
 Movies.objects.filter(name__endswith=’a’)                  поле заканчивается на “a”
 Movies.objects.filter(id__in=[3,5,6]’)                     выбираются все значения из списка


 1. Метод get()- используется когда хотим получить только одну запись
   name_class.objects.get(аргумент=100 или 'Фиеста') Movie.objects.get(rating=80) - найдет первую подходящую запись в БД
    по переданным параметрам

 2. Метод filter()- используется когда хотим получить все подходящие записи
    name_class.objects.filter(аргумент=10000 или 'Фиеста') - Movie.objects.filter(budget=10000) - найдет все подходящие
    записи, которые подходят под условие аргумента

 3. Метод __gt - если хотим найти значение >
    name_class.objects.filter(аргумент__gt=10000) - Movie.objects.filter(budget__gt=10000) - найдет все подходящие
    записи, которые подходят под условие аргумента

 4. Метод __lt- если хотим найти значение <
    name_class.objects.filter(аргумент__lt=10000) - Movie.objects.filter(budget__lt=10000) - найдет все подходящие
    записи, которые подходят под условие аргумента

 5. Метод __gte - если хотим найти значение >=
    name_class.objects.filter(аргумент__gte=10000) - Movie.objects.filter(budget__gte=10000) - найдет все подходящие
    записи, которые подходят под условие аргумента

 6. Метод exclude - если мы хотим исключить запись (типо если не равно значению !=)
    name_class.objects.exclude(аргумент=10000) - Movie.objects.exclude(budget=10000) - найдет все подходящие записи,
    которые подходят под условие аргумента, если не подходит под условие - исключаем

 7. Метод __isnull - если хотим поля где есть null или нет null
    name_class.objects.filter(аргумент__isnull=True или False) - Movie.objects.filter(budget__isnull=True) - выдаст нам
    запись, где есть null(если True) или его нет(если False)

 8. Метод __isnull - с двумя параметрами
    name_class.objects.filter(аргумент__isnull=True или False,name='Аватар') -
    Movie.objects.filter(budget__isnull=True,name = 'Аватар') - если подходит под два условия

 9. Метод create - можно создавать новые табличные значения легче
    name_class.objects.create(аргумент=...,аргумент=...) - Movie.objects.create (name = 'Аватар',rating=88) -
    создаст новую запись в БД

 10. Метод __contains(содержит)(чувствителен к регистру) и __icontains(содержит)(не чувствителен к регистру) - выдаст
   нам все записи, где есть содержимое переданного аргумента

     1. name_class.objects.filter(аргумент__icontains=...) - Movie.objects.filter(name__iconteins='Аватар') - найдет все
        записи, где есть начало 'Аватар'

     2. name_class.objects.filter(аргумент__icontains=...) - Movie.objects.filter(name__iconteins='а') - найдет все
        записи, где есть буква 'а'

 11. Методы __startswith и __endswith - (__startswith) фильтер будет искать по первым буквам или цифрам,
     (__endswith) по крайним символам

     1. name_class.objects.filter(аргумент__startswith=...) - Movie.objects.filter(name__startswith='ава') - если есть
        записи в таблице, которые начинаются на 'ава', нам их выдаст

     2. name_class.objects.filter(аргумент__endswith=...) - Movie.objects.filter(name__endswith='ава') - если есть
        записи в таблице, которые заканчиваются на 'ава', нам их выдаст

 12. Метод __in - выдаст все передаваемые аргументы, которые мы хотим видеть
     name_class.objects.filter(аргумент__in=[.,.,.]) - Movie.objects.filter(id__in=[2,3,4]) - выдаст нам всю информацию
     об этом id(name,rating,year и т.д.)


 Можно использовать регулярные выражения

 # Очень полезные методы   __regex  - чувствительное к регистру       __iregex - нечувствительное к регистру
 # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#regex
 Синтаксис регулярных выражений соответствует синтаксису используемой базы данных.

 # Должны быть выведены первые 3 строки в зависимости от установленного вами порядка.
 Model.objects.filter(adv_images__regex=r'^\d\.')[:3]
 Model.objects.filter(adv_images__regex=r'^\d\.')[:3]


 Entry.objects.get(title__regex=r"^(An?|The) +")

 # Регулярные выражения в SQL
 SQL equivalents:
 SELECT ... WHERE title REGEXP BINARY '^(An?|The) +'; -- MySQL

 SELECT ... WHERE REGEXP_LIKE(title, '^(An?|The) +', 'c'); -- Oracle

 SELECT ... WHERE title ~ '^(An?|The) +'; -- PostgreSQL

 SELECT ... WHERE title REGEXP '^(An?|The) +'; -- SQLite
 Рекомендуется использовать необработанные строки (например, r'foo'вместо 'foo') для передачи синтаксиса регулярных выражений.

 Примечание Еще зависит от БД

 Единственное условие: LIKE быстрее
 Несколько условий: REGEXP быстрее

 # Единственное условие
 SELECT * FROM comments WHERE text LIKE '%\\\\n%'; 🚀 Faster
 SELECT * FROM comments WHERE text REGEXP '\\\\n'; 🐢 Slower

 # Множественные условия
 SELECT * FROM comments
 WHERE text LIKE '%\\\\r\\\n%'
 OR text LIKE '%\\\\n%'
 OR text LIKE '%\\\\r%'; 🐢 Slower

 SELECT * FROM comments
 WHERE text REGEXP '((\\\\r\\\\n)|(\\\\(n|r)))'; 🚀 Faster

 Заключение:
 Используется LIKE для запросов с одним условием и REGEXP для запросов с несколькими условиями.   <----  ВАЖНО


 # Пример функции взаимодействующей с моделью

 def show_all_movie(request):
     movies = Movie.objects.all()
     return render(request, 'movie_app/all_movie.html', context={
         'movies': movies
     })

 # Сортировки -rating - минус перед полем значит в обратном порядке
 def show_all_movie(request):
     movies = Movie.objects.order_by('-rating', 'budget')          # Сначала по -rating(Убыванию) а потом по budget
     return render(request, 'movie_app/all_movie.html', context={
         'movies': movies
     })


 # Обьект F
 def show_all_movie(request):
     movies = Movie.objects.order_by(F('rating').desc(nulls_last=True), 'year')  # Так НЕЛЬЗЯ использовать -rating
     return render(request, 'movie_app/all_movie.html', context={
         'movies': movies
     })

 Объект F в Django используется для операций с полями модели прямо на уровне базы данных, без необходимости сначала
 извлекать данные из БД.

 Использование объекта F позволяет уменьшить количество запросов к базе данных и ускорить операции, так как многие
 действия выполняются прямо на уровне БД, а не в памяти Python. Это особенно полезно при работе с большими объемами
 данных или когда требуется высокая производительность.


 # Мини-инфо
 Movie.objects.order_by('name')             # от первой буквы до последней
 Movie.objects.order_by('-name')            # от последней буквы до первой
 Movie.objects.order_by('rating')[:5]       # срез
 Movie.objects.order_by('rating', 'budget') # сортировка по нескольким параметрам, второй параметр учитывается в случае,
 если у двух объектов одинаковое значение по первому параметру значения null располагаются по умолчанию снизу

 from django.db.models import F
 Movie.objects.order_by(F('year').asc)                             # сортировка по возрастанию
 # nulls_last -- null в конце, nulls_first -- null в начале
 Movie.objects.order_by(F('year').desc(nulls_last=True)            # сортировка по убыванию
 Movie.objects.order_by(F('year').desc(nulls_last=True, 'rating')  # сортировка по нескольким параметрам


 from django.db.models import F, Sum, Max, Min, Avg, Count
 # Функции агрегации
 def show_all_movie(request):
     movies = Movie.objects.order_by(F('rating').desc(nulls_last=True), 'year')
     agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
     return render(request, 'movie_app/all_movie.html', context={
         'movies': movies,
         'agg': agg,
     })


 # В файле models.py
 from django.db import models
 from django.urls import reverse_lazy
 from django.utils.text import slugify

 # Создание полей в Базе Данных
 class Movie(models.Model):
     name = models.CharField(max_length=40)
     rating = models.IntegerField()
     year = models.IntegerField(null=True)
     budget = models.IntegerField(default=1_000_000)
     slug = models.SlugField(default='', null=False, db_index=True)

     def save(self, *args, **kwargs):
         self.slug = slugify(self.name)
         super().save(*args, **kwargs)

     def __str__(self):
         return f'{self.name} - {self.rating}%'

     def get_url(self):
         return reverse_lazy('one_movie', args=(self.slug, ))


  # В файле admin.py

  # Регистрация Модели в Админке
 from django.contrib import admin
 from .models import *
 from django.db.models import QuerySet  # Можно добавлять к аннотациям


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

 # Примерные возможности админки   Поле  ManyToManyField не может быть в list_editable и list_display
 @admin.register(Movie)
 class ModelNameAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug': ('name', )}                             # Авто-заполнение slug в Админке
     fields = ['name', 'rating', 'year', 'slug']                            # Какие поля можно добавлять в Админке
     # exclude = ['name', 'rating']                                         # Тоже самое но исключаем
     # readonly_fields = ['name']                                           # Только для чтения поля
     list_display = ['name', 'rating', 'year', 'budget', 'rating_status']   # Какие поля будут отображатся в Админке
     list_editable = ['rating', 'year', 'budget']                           # Какие поля можно редактировать в Админке
     ordering = ['-rating', 'name']                                         # По Каким полям будет Сортировка в Админке
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


 ListView, DetailView

 # from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView, CreateView

 # Django Находить одну запись и сохраняет её по модели в нижнем регистре
 class DetailFeedback(DetailView):
     template_name = 'feedback/detail_feedback.html'  # По дефолту будет шаблон   имя приложения / имя модели_detail.html
     model = Feedback  # Переписывает для шаблона html в нижний регистр feedback
     context_object_name = 'fee'  # По дефолту будет переменная object


 class ListFeedback(ListView):
     template_name = 'feedback/list_feedback.html'  # По дефолту будет шаблон      имя приложения / имя модели_list.html
     model = Feedback
     context_object_name = 'feedbacks'  # По дефолту будет переменная object_list

     # Фильтрация записей
     def get_queryset(self):
         qs = super().get_queryset()
         filter_qs = qs.filter(rating__gt=2)
         return filter_qs

 Роуты
 urlpatterns = [
    path('list', ListFeedback.as_view()),
    path('detail/<int:pk>', DetailFeedback.as_view()),  # Прописываем pk или slug
]

 # Или Сразу Указываем в Роуте без создание классов во views
 path('list', ListView.as_view(model=Feedback, template_name='feedback/feedback_list.html')),
 path('detail/<int:pk>', DetailView.as_view(model=Feedback, template_name='feedback/feedback_detail.html')),

 # Можно без указание template_name  если правильно назвать html
 path('list', ListView.as_view(model=Feedback)),
 path('detail/<int:pk>', DetailView.as_view(model=Feedback)),


 # Формы прописываются в файле forms
 from django import forms
 from .models import *

 # Класс ModelForm
 class FeedbackForm(forms.ModelForm):
     class Meta:
         model = Feedback
         # fields = ['name', 'surname']
         fields = '__all__'
         # exclude = ['name']
         labels = {
             'name': 'Имя',
             'surname': 'Фамилия',
             'feedback': 'Отзыв',
             'rating': 'Рейтинг',
         }
         error_messages = {
                  'name': {
                      'max_length': 'Слишком много симваолов',
                      'min_length': 'Слишком мало симваолов',
                      'required': 'Хотя бы 1 символ',
                  },
                 'surname': {
                     'max_length': 'Слишком много симваолов',
                     'min_length': 'Слишком мало симваолов',
                     'required': 'Хотя бы 1 символ',
                 },
              }



 # Для СОЗДАНИЯ записей в БД через Форму    CreateView

 # Переменная для шаблона html по дефолту будет  form
 class FeedbackView(CreateView):
     model = Feedback
     form_class = FeedbackForm                      # Лучше использовать form_class
     # fields = '__all__'
     template_name = 'feedback/feedback.html'
     success_url = '/done'                          # Куда перенаправлятся


 # Для ОБНОВЛЕНИЯ записей в БД через Форму    UpdateView
 class FeedbackViewUpdate(UpdateView):
     model = Feedback
     form_class = FeedbackForm
     template_name = 'feedback/feedback.html'
     success_url = '/done'


 # Для УДАЛЕНИЯ записей в БД через Форму    UpdateView
 class FeedbackViewDelete(DeleteView):
     model = Feedback
     success_url = reverse_lazy('/list')
     template_name = 'feedback/feedback_delete.html'

 # Роуты можно прописывать в urls.py  сразу так
 path('delete/<int:pk>', DeleteView.as_view(model=Feedback, template_name='feedback/feedback_delete.html',
                                           success_url='/list')),


 Для загрузки файлов

 class Gallery(models.Model):
    image = models.FileField(upload_to='media')


 В settings для загрузки файлов

 MEDIA_ROOT = BASE_DIR / 'uploads'
 MEDIA_URL = '/my_media/'

 В urls корня проекта для загрузки файлов

 from django.contrib import admin
 from django.urls import path, include
 from django.conf import settings
 from django.conf.urls.static import static

 urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('feedback.urls')),
     path('', include('gallery.urls')),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











































































"""