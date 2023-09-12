# Проект Yatube. Начало.

![Python](https://img.shields.io/badge/Python-313131?style=flat&logo=Python&logoColor=white&labelColor=306998)
![Django](https://img.shields.io/badge/Django-313131?style=flat&logo=django&labelColor=092e20)
![SQLite](https://img.shields.io/badge/SQLite-313131?style=flat&logo=sqlite&logoColor=ffffff&labelColor=033b55)
![Visual Studio](https://img.shields.io/badge/VS%20Code-313131?style=flat&logo=visualstudiocode&logoColor=ffffff&labelColor=0098FF)

## Проект Yatube — это платформа для публикаций (блог). На данном этапе реализовано отображение постов и их создание через админ-зону.

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/deltabobkov/hw02_community.git

cd hw02_community
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv env

source env/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate
```

5. Создать супер пользователя:

```
python manage.py createsuperuser
```

6. Запустить проект:

```
python manage.py runserver
```
