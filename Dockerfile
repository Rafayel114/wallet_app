# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    default-mysql-client \
    build-essential \
    # python3-dev \
    # python3-pip \
    # python3-distutils \
    && apt-get clean

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование исходного кода и скрипта ожидания
COPY . .
COPY wait-for-mysql.sh /app/
RUN chmod +x /app/wait-for-mysql.sh

# Копируем проект
COPY . .
