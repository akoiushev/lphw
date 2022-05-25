# Импортируем модуль sys
from sys import argv

# Задаем переменные для argv
script, filename = argv

# Текст, который поясняет пользователю что будет происходить на экране.
print(f"Я собираюсь стереть файл {filename}")
print("Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C.")
print("Если вы хотите стереть файл, нажмите ENTER")

# Якобы чего-то ждем от пользователя :))) 
input("?")

# Открываем файл методом open с опцией w
print("Открытие файла...")
target = open(filename, "w")

# Отчишаем содержимое файла. Попробовать закоментить. Будет ли дописывание в файл? 
print("Отчистка файла. До свидания!")
target.truncate()

# Запрашиваем три строки данных
print("Теперь я запрашиваю у вас три строки")

line1 = input("Строка 1: ")
line2 = input("Строка 2: ")
line3 = input("Строка 3: ")

# Говорим пользователю, что именно мы собираемся сделать.
print("Я запишу их в файл.")

# Записывает содержимое переменных в файл + переносим строки
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Закрываем файл
print("И наконец, я закрываю файл")
target.close()