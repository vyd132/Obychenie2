import random

print("Это игра 'Угадай число'. Ваша задача угадать число")
chislo = random.randint(50,50)
otv = input("Введите число о ктотором вы подумали")
poput = 1
while otv != chislo:
    if otv == "стоп":
        print("Ах ты слобак а число было равно", chislo)
        break

    isnu = otv.isnumeric()
    if isnu == False:
        otv = input("Нужно вводить число")
        continue

    otv = int(otv)

    if otv < 1 or otv > 100:
        otv = input("Число может быть от 1 до 100")
        continue

    if otv > chislo:
        print("Мое число меньше")
    elif chislo > otv:
        print("Мое число больше")
    else:
        continue

    poput = poput + 1
    kol = "Попытка " + str(poput) + " Вы не угадали попробуйте еще раз"
    otv = input(kol)



else:
    print("Правильно. Вы угадали c",poput,"попытки")