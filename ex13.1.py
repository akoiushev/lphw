from sys import argv
# Прочитайте раздел "Результат выполнения" результат выполнения, что бы понять, 
# как запустить этот скрипт.

# Далее по тексту вчтреается несколько одинаковых строк. Это попытки разобраться в логике совмещения 
# работы модуля sys.argv и input(). Пытаюсь понять везде ли работает. 

# Переменная fifth отработала, как ожидалось
# fifth = int(input("Введите пятый аргумент: "))

script, first, second, third, fourth = argv

# Расположенная после agrv тоже отработала. 
# fifth = int(input("Введите пятый аргумент: "))


print("Этот сценарий называется:", script)
print("Моя первая переменная называется:", first)
print("Моя вторая переменная называется:", second)
print("Моя третья переменная называется:", third)
print("Моя четвертая переменная называется:", fourth)

# расположенная input после полностью отработавшей argv тоже работает.
fifth = int(input("Введите пятый аргумент: "))
print("Моя пятая переменная называется: ", fifth)
