import os

from Disk import Disk
from FileManager import FileManager


token = ""    # Вставьте свой токен для Яндекс.Диска

# Проверяем корректность названия файла
file_name = FileManager.check_file_name(input("Введите название для json-файла: "))

# Создаем файл формата json c названием города, полученным по IP
FileManager.create_file_with_city(file_name)

# Создаем папку и загружаем файл на диск
Disk.upload_at_disk(file_name, token)

# Удаляем файл с компьютера
os.remove(file_name)