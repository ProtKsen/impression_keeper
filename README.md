# Places Remember

Веб приложение, позволяющее пользователям сохранять впечатления от посещенных мест.

[![Coverage Status](https://coveralls.io/repos/github/ProtKsen/impression_keeper/badge.svg?branch=feature)](https://coveralls.io/github/ProtKsen/impression_keeper?branch=feature)

home page|user profile|edit place
:-:|:-:|:-:
![Alt-текст](https://github.com/ProtKsen/impression_keeper/blob/main/screenshots/home.png?raw=true) | ![Alt-текст](https://github.com/ProtKsen/impression_keeper/blob/main/screenshots/user_profile.png?raw=true) | ![Alt-текст](https://github.com/ProtKsen/impression_keeper/blob/main/screenshots/edit_place.png?raw=true)

* Приложение запущено на yandex cloud и доступно по адресу http://158.160.96.100.nip.io:8000/.

* Приложение реализовано на **Django**, база данных - **PostgreSQL**, для входа в профиль пользователя через Google/VK используется библиотека **django-allauth**, карта - **yandex map**, менеджер зависимостей - **poetry**, стили **Bootstrap**, тестирование - **pytest**.

* Разработка происходит в ветке feature. Ветка main защищена, требует создания pull-request перед слиянием. Перед каждым коммитом выполняется проверка линтерами, для чего применяется git hook pre-commit. Также используется workflow (pre-pull-request.yaml), реализующий проверку линтерами и тестирование при каждом push в ветку feature, в случае успешного прохождения всех проверок создается pull-request в ветку main.

* Для последующего деплоя используется workflow docker-publish.yaml, создающий публичный docker контейнер.

### Использование

#### Установка

```bash
git clone https://github.com/ProtKsen/impression_keeper.git
```

#### Установка poetry, выполняется один раз

```bash
pip install poetry
poetry config virtualenvs.in-project true
```

#### Установка зависимостей

```bash
poetry init
poetry install
```

#### Настройки окружения

Создать файл `.env` на базе `.env.default`.

#### Установка docker, выполняется один раз

См. <https://docs.docker.com/engine/install/>

#### Запуск базы данных

```bash
docker-compose up -d db
```

#### Запуск приложения

```bash
docker-compose up -d app
```

#### Локальный запуск тестов

```bash
poetry run pytest
```
