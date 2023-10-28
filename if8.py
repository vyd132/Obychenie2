cher = input("Сколько вишен вы хотите съесть")
cher = int(cher)
if cher % 10 == 11 or cher >= 5 and cher <= 20:
    print("Вы съели", cher, "вишен")
elif cher == 1 or cher%10 == 1:
    print("Вы съели",cher,"вишню")
elif cher >= 2 and cher <= 4:
    print("Вы съели",cher,"вишни")
