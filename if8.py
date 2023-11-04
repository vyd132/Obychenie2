# cher = input("Сколько вишен вы хотите съесть")
# cher = int(cher)
for cher in range(0,200):
    print(cher,end=": ")
    if cher % 10 == 0 or (cher % 100 >= 11 and cher % 100 <= 14) or (cher % 10 >= 5 and cher % 10 <= 9):
        print("Вы съели", cher, "вишен")
    elif cher == 1 or cher%10 == 1:
        print("Вы съели",cher,"вишню")
    elif cher % 10 >= 2 and cher % 10 <= 4:
        print("Вы съели",cher,"вишни")
