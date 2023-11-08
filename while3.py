import wrap
import random
import math
import time
width = 400
height = 800
wrap.world.create_world(width,height)



turtle = wrap.sprite.add("mario-enemies", 30, 400, "turtle_blue_stand")
mar = wrap.sprite.add("mario-2-big",width-30, 100, "stand")
hammer = wrap.sprite.add("mario-enemies", 30, 30, "turtle_hammer",False)
wrap.sprite.set_reverse_x(turtle, 180)
wrap.sprite.set_reverse_x(mar, 180)

start = time.time()
c = time.time()
speedx1 = random.randint(5, 20)
speedx = random.randint(5, 20)
text = wrap.sprite.add_text("0",200,30,text_color=[255,255,255])
while True:

    a = time.time()
    b = a - start
    b = int(b)
    b = str(b)


    wrap.sprite.move(turtle, 0, speedx)
    y = wrap.sprite.get_y(turtle)
    if y >= 770:
        speedx = -random.randint(5, 20)
    elif y <= 40:
        speedx = random.randint(5, 20)


    d = time.time()
    e = d - c

    if e >= 5:
        wrap.sprite.show(hammer)
        wrap.sprite.move(hammer,30,y)
        c += 5

    wrap.sprite.move(hammer, width-30, y)



    wrap.sprite.move(mar, 0, speedx1)
    y = wrap.sprite.get_y(mar)
    if y >= 770:
        speedx1 = -random.randint(5, 20)
    elif y <= 40:
        speedx1 = random.randint(5, 20)
    wrap.sprite_text.set_text(text,b)






