#!/bin/bash
set -e

# Ожидание запуска MySQL
echo "Waiting for MySQL to start..."
while ! mysqladmin ping -h"db" --silent; do
  sleep 1
done

echo "MySQL is up - configuring database..."

# Выполнение SQL-команд для настройки базы данных
mysql -h"db" -P3306 -u root -p"$MYSQL_ROOT_PASSWORD" -e "GRANT ALL PRIVILEGES ON *.* TO '$MYSQL_USER'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;"

echo "Database configured successfully!"