import wrap
iron = 45
instrument = 10
gvozd = 1.1
print("На фабрике жили поживали",iron,"килограмм железа. Из них захотели сделать инструменты")
print("На 1 инструмент уходило",instrument,"килограмм железа. Получилось",iron // instrument,"инструментов")
inst = iron // instrument
print("Но осталось одинокое не использованное железо в количетсве",iron % instrument,"килограммов")
ost = iron % instrument
print("Работники пожалели их и использовали на гвозди. Получилось",ost // gvozd,"гвоздей. По",gvozd,"килограмм на гвоздь")
print("Но все равно осталось целых",ost % gvozd,"несчастных килограмов железа")


