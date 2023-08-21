# Проект YaCut — сервис укорачивания ссылок

Проект позволяет ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Стек технологий:

* Python 3.7.9
* Flask

## Как запустить проект:

* Клонировать репозиторий:

```
git clone git@github.com:vikkilat/yacut.git
```

* Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

* Установить зависимости из файла ```requirements.txt```:

```
pip install -r requirements.txt
```

* Выполнить миграции:
```
flask db init
flask db migrate
flask db upgrade
```

* Запустить проект локально:
```
flask run
```

## Автор:
[Латышева Виктория](https://github.com/vikkilat)