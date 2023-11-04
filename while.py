password = 123
otv = input("Введите пароль")
otv = int(otv)
while otv != password:
    otv = input("Введите пароль")
    otv = int(otv)
else:
    print("Правильно")