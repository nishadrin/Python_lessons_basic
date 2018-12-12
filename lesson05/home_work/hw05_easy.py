# -*- coding: utf-8 -*-
"""
Создание и удаление директорий, отображение текцщей директории, копирование данного скрипта

Использовался import: os, shutil

dir_add(folder) - добавить дирекорию (папку), путь должен быть полным;
dir_remove(folder) - удалить дирекорию (папку), путь должен быть полным;
current_path() - выводит директорию в которой находимся
copy_file(what_file, where_file) - копирует файл; what_file - путь до копируемого файла (путь должен быть полным), where_file путь куда копируем файл (путь должен быть полным)
"""
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

def dir_add(folder):
    os.mkdir(folder)


def dir_remove(folder):
    os.rmdir(folder)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def current_path():
    path = os.getcwd()
    print(path)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(what_file, where_file): #указываем полный путь, в том числе название файла
        shutil.copyfile(what_file, where_file)


if __name__ == '__main__':
    # Задача-1:
    for i in range(10):
        dir_add("dir_" + str(i))

    for i in range(10):
        dir_remove("dir_" + str(i))

    # Задача-2:
    current_path()

    # Задача-3:
    what_file = "/home/nick/Документы/GITHUB/Python_lessons_basic/lesson05/home_work"
    where_file = "/home/nick/Документы/GITHUB/Python_lessons_basic/lesson05/home_work2"

    copy_file(what_file, where_file)
