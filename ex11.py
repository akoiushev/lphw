#print("Сколько тебе лет?", end=' ')
#age = input()
#print("Каков твой рост?", end=' ')
#height = input()
#iprint("Сколько ты весишь?", end=' ')
#weight = input()

#print(f"Итак, тебе {age} лет, в тебе {height} см роста и {weight} кг веса.")

print("Теперь вычисли средний возраст всех членов твоей семьи. Введи возраст Романа: ", end = " ") 
rage = int(input())
print("Введи возраст Богдана: ", end = " ") 
bage =  int(input())
print("Введи возраст Екатерины: ", end = " ") 
kage = int(input())
print("Введи свой возраст: ", end = " ") 
my_age = int(input())
avr_age = (rage + bage + kage + my_age)/4
print(f"Средний возраст вашей семьи равен {avr_age} лет")
