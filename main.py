import os

from Ipify import Ipify
from Disk import Disk


token = ""    # Вставьте свой токен для Яндекс.Диска
file_name = input("Введите название для json-файла: ")


# Создаем файл формата json c названием города по местоположению
Ipify.create_file(file_name)

# Создаем папку и загружаем файл на диск
Disk.upload_at_disk(file_name, token)

# Удаляем файл с компьютера
os.remove(file_name)