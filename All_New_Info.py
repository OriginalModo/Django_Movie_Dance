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
















































































































































"""