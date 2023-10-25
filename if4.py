import random
player1 = random.choice(["Камень","Ножницы","Бумага"])
player2 = random.choice(["Камень","Ножницы","Бумага"])
print("Игроку 1 выпало",player1)
print("Игроку 2 выпало",player2)

if player1=="Бумага" and player2 == "Ножницы":
    print("Ножницы режут бумагу 2 игрок выиграл")

if player1=="Бумага" and player2 == "Камень":
    print("Бумага накрывает камень 1 игрок выиграл", )

if player2=="Бумага"and player1 == "Ножницы":
    print("Ножницы режут бумагу 1 игрок выиграл")

if player2 == "Бумага" and player1 == "Камень":
    print("Бумага накрывает камень 2 игрок выиграл",)

if player2=="Камень" and player1=="Ножницы":
    print("Камень ломает ножницы 2 игрок выиграл")

if player1=="Камень" and player2=="Ножницы":
    print("Камень ломает ножницы 1 игрок выиграл")


if player1 == player2:
    print("Игрокам выпало одно и тоже. Ничья")