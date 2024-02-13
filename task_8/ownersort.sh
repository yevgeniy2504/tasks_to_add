#!/bin/bash

# Проверяем, передан ли аргумент
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Проверяем существование директории
if [ ! -d "$1" ]; then
    echo "Error: Directory $1 does not exist."
    exit 1
fi

# Создаем директории для каждого владельца файла
find "$1" -type f -printf "%u\n" | sort -u | while read -r owner; do
    mkdir -p "$owner"
done

# Копируем файлы в соответствующие директории
find "$1" -type f -exec bash -c '
    for file; do
        owner=$(stat -c "%U" "$file")
        cp "$file" "$owner/"
    done
' bash {} +
