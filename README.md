### **API для Yatube**

> Проект предоставляет доступ к публикациям на платформе для блогов Yatube. Он дает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

### **Cтек использованных технологий:**
- Python 3.9
- Django 3.2.16
- Django Rest Framework 3.12.4
- SQLite3

### **Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Anastasiia-Barkhatova/api_final_yatube/
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source venv/Scripts/activate
```

Обновить pip

```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Перейти в репозиторий yatube_api

```bash
cd yatube_api
```

Выполнить миграции:

```bash
python manage.py migrate
```

Запустить проект на сервере:

```bash
python manage.py runserver
```

### **Примеры запросов к API:**

* Пример GET-запроса для получения всех публикаций:
```
.../api/v1/posts/
```
* Пример ответа:
```
[
    {
        "id": 1,
        "author": "Anastasiia",
        "text": "string",
        "pub_date": "2024-06-17T04:35:59.911362Z",
        "image": null,
        "group": 2
    },
    {
        "id": 2,
        "author": "Anastasiia",
        "text": "string",
        "pub_date": "2024-06-17T04:51:26.944106Z",
        "image": null,
        "group": 1
    }
]
```
* Пример POST-запроса для добавления публикации:
```
.../api/v1/posts/
```
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
* Пример ответа:
```
{
    "id": 7,
    "author": "Anastasiia",
    "text": "string",
    "pub_date": "2024-06-17T13:34:21.474678Z",
    "image": null,
    "group": 2
}
```
* Пример GET-запроса для получения конкретной публикаций:
```
...api/v1/posts/{id}/)
```
* Пример ответа:
```
{
    "id": 4,
    "author": "Anastasiia",
    "text": "abcd",
    "pub_date": "2024-06-17T04:51:50.839933Z",
    "image": null,
    "group": 2
}
```
* Пример GET-запроса для получения комментариев к конкретной публикаций:
```
...api/v1/posts/{post_id}/comments/)
```
* Пример ответа:
```
{
    "id": 0,
    "author": "Anastasiia",
    "text": "@@@@@",
    "created": "2024-06-17T04:51:50.839933Z",
    "post": 0
}
```

* Пример POST-запроса для добавления комментария к конкретной публикаций:
```
...api/v1/posts/{post_id}/comments/)
```
```
{
    "text": "string"
}
```
* Пример ответа:
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```

[Посмотреть примеры других запросов](http://127.0.0.1:8000/redoc/)

Авторы: [команда Яндекс.Практикума](https://github.com/yandex-praktikum), [Бархатова Анастасия](https://github.com/Anastasiia-Barkhatova)
