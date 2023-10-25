import wrap
import random
import math
width = 600
height = 600
wrap.world.create_world(width,height)
wrap.world.set_back_color(104,238,255)

x = random.randint(30,570)
y =  random.randint(230,570)

mar = wrap.sprite.add("mario-1-big",50,50,"stand")
klad = wrap.sprite.add("mario-items",x,y,"star")
dot = wrap.sprite.add("pacman",50,50,"dot")
wrap.sprite.hide(klad)
go = math.dist([50,50],[x,y])
go = int(go)
wrap.sprite.add_text("Осталось идти "+str(go)+" px",150,40)
wrap.actions.set_angle_to_point(mar,x,y)

x1 = input("Напишите x")
y1 = input("Напишите y")
x1 = int(x1)
y1 = int(y1)

wrap.actions.move_to(mar,x1,y1)

go = math.dist([x1,y1],[x,y])
go = int(go)

wrap.sprite.add_text("Осталось идти "+str(go)+" px",x1,y1)

wrap.actions.set_angle_to_point(mar,x,y)

x2 = input("Напишите x")
y2 = input("Напишите y")
x2 = int(x2)
y2 = int(y2)

wrap.actions.move_to(mar,x2,y2)

go = math.dist([x2,y2],[x,y])
go = int(go)

wrap.sprite.add_text("Осталось идти "+str(go)+" px",x2,y2)

wrap.actions.set_angle_to_point(mar,x,y)

x3 = input("Напишите x")
y3 = input("Напишите y")
x3 = int(x3)
y3 = int(y3)

wrap.actions.move_to(mar,x3,y3)

go = math.dist([x3,y3],[x,y])
go = int(go)

wrap.sprite.add_text("Осталось идти "+str(go)+" px",x3,y3)

wrap.actions.set_angle_to_point(mar,x,y)

klad = wrap.sprite.add("mario-items",x,y,"star")