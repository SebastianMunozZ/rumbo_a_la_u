#!/bin/bash
set -e

host="$1"
port="$2"
timeout="${3:-30}"

echo "Esperando hasta que MYSQL -> $host:$port este arriba..."
while ! nc -z $host $port; do
  timeout=$((timeout - 1))
  if [ $timeout -eq 0 ]; then
    >&2 echo "esperando a $host:$port"
    exit 1
  fi
  sleep 1
done

echo "MYSQL -> $host:$port esta arriba"



python manage.py runserver 0.0.0.0:8000