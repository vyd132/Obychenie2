import wrap
chocolate = 30
money = 100
print("В супермаркете проходит акция: 3 шоколадки по цене 2х. Т.е. при покупке 2х шоколадок третью дают в подарок.")
print("Каждая шоколадка стоит",chocolate,"рублей")
print("У покупателя есть",money,"рублей")
print("Он сможет купить",money//chocolate,"шоколадок")
buy = money//chocolate
print("Но с акцией он получит",buy+(buy//2),"шоколадок")
print("В итоге у него останется",money%chocolate,"рублей")

