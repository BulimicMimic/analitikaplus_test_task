## Analitikaplus test task

### Автор: 
Алаткин Александр

### Описание:
Реализация тестового задания от работодателя Аналитика плюс.<br>
Задача выполнена при помощи хеш таблиц с генерацией хеша при помощи библиотеки secrets.<br>
Часть 2.
Ваша компания отправляет СМС с трекинговой ссылкой, но ссылка достаточно длинная и из-за этого СМС выходит за 70 символов (длина 1 СМС). 
Необходимо спроектировать сервис-«укорачиватель ссылок», чтобы сэкономить деньги компании.
Интервьюер при этом выступает заказчиком со стороны бизнеса и ему можно задавать вопросы по сути задачи.
В качестве решения необходимо предоставить описание и программные требования код.

### Использующиеся технологии:
```
Django
Django Rest Framework
PostgreSQL
Gunicorn
Nginx
Docker
```
### Установка. Как развернуть проект локально:

Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:BulimicMimic/analitikaplus_test_task.git
```

Запустить сеть докер контейнеров из корневой директории проекта:
```
docker compose -f docker-compose.yml up
```

Выполнить миграции:
```
docker compose -f docker-compose.yml up
```

Собрать и скопировать статику Django:
```
docker compose -f docker-compose.yml exec backend python manage.py collectstatic
docker compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```

### Примеры запросов API:

```
POST http://localhost:8000/api/shorten_link/
Content-Type: application/json

{
    "link_to_shorten": "https://stackoverflow.com/questions/58044343/how-can-i-generate-a-youtube-style-unique-alphanumeric-id-model-id-in-django/58045210#58045210"
}

Response 200 OK
{
    "short_link": "http://localhost:8000/api/gqWHUor30p3xpRStAa8DDA",
    "link_to_shorten": "https://stackoverflow.com/questions/58044343/how-can-i-generate-a-youtube-style-unique-alphanumeric-id-model-id-in-django/58045210#58045210"
}
```