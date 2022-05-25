# Импорт модуля sys переменной argv
from sys import argv

# задаю аргументы к переменной argv
script, filename = argv

# Открываем файл: применяем метод open c параметром в виде переменной filename (а его мы задаем при запуске этого скрпта при помощи argv).
# Далее команда open возвращает значение переменной txt. В итоге присваиваем переменной значение, которое возвращает команда open.
txt = open(filename)

# Выводим на экран строку с комментарием деййствия скрипта: Содержимое файла... + переменная, заданная через argv  
print(f"Содержимое файла {filename}:")

# В результате функции open я получаю ОБЪЕКТ, к которому можно применить следующую команду. Это команда read(параметры).
# Команда read() применяется, используя точку .read (по аналогии с input() ). 
# Я как бы говорю: Эй, txt!  Примени ка функцию read без параметров.
print(txt.read())

# После выполнения скрипта, скрипт снова выводит строку
# print("Снова введите имя файла:")

# Создаю переменную, запрашивая у пользователя Имя_файла.
# file_again = input(">> ")

# Создаю переменную с ОБЪЕКТОМ, но не вывожу его на экран. Просто переменная, значением которой является открытый файл с таким-то именем. 
# txt_again = open(file_again)

# Применяю команду read без параметров к переменной txt. 
# print(txt_again.read())
