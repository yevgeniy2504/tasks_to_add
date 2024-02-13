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

# Очищаем директорию от файлов с расширениями .bak, .tmp, .backup
find "$1" -type f \( -name "*.bak" -o -name "*.tmp" -o -name "*.backup" \) -delete

echo "Directory $1 has been cleaned."
