# Wallet Project

Этот проект представляет собой приложение для управления кошельками и транзакциями, построенное с использованием Django и Django REST Framework.

## Требования

- Docker
- Docker Compose

## Клонирование репозитория

1. Склонируйте репозиторий на вашу локальную машину:

    ```bash
    git clone https://github.com/USERNAME/REPOSITORY_NAME.git
    ```

   Замените `USERNAME` и `REPOSITORY_NAME` на ваше имя пользователя GitHub и имя репозитория соответственно.

2. Перейдите в директорию проекта:

    ```bash
    cd REPOSITORY_NAME
    ```

## Настройка

Перед запуском приложения убедитесь, что у вас установлены Docker и Docker Compose. Затем выполните следующие шаги:

1. Создайте файл `.env` в корневой директории проекта и добавьте в него необходимые переменные окружения. Пример содержания `.env`:

    ```env
    MYSQL_DATABASE=your_database_name
    MYSQL_USER=your_database_user
    MYSQL_PASSWORD=your_database_password
    MYSQL_ROOT_PASSWORD=your_root_password
    ```

## Запуск приложения

1. Постройте и запустите контейнеры с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

2. После запуска, приложение будет доступно по адресу `http://localhost:8008/`.

## Выполнение тестов

Чтобы выполнить тесты, используйте следующую команду:

```bash
docker-compose run web python manage.py test
