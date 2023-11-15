import wrap
import random
import math
import time
width = 400
height = 800
wrap.world.create_world(width,height)
wrap.world.set_back_color(173,153,255)



turtle = wrap.sprite.add("mario-enemies", 30, 400, "turtle_blue_stand")
mar = wrap.sprite.add("mario-2-big",width-30, 100, "stand")
hammer = wrap.sprite.add("mario-enemies", 30, 30, "turtle_hammer",False)
wrap.sprite.set_reverse_x(turtle, 180)
wrap.sprite.set_reverse_x(mar, 180)
hammY = 1
angle = 10

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
        hammY = y1
        wrap.sprite.move_to(hammer, 30, y)
        wrap.sprite.show(hammer)
        c += 5



    wrap.sprite.move(mar, 0, speedx1)
    y1 = wrap.sprite.get_y(mar)
    if y1 >= 770:
        speedx1 = -random.randint(5, 20)
    elif y1 <= 40:
        speedx1 = random.randint(5, 20)


    wrap.sprite.move_at_angle_point(hammer, width - 30, hammY, 50)
    wrap.sprite.set_angle(hammer,angle)
    angle += 10

    col = wrap.sprite.is_collide_sprite(hammer,mar)

    wrap.sprite_text.set_text(text,b)

    if col == True:
        break

while True:
    speedx1 = 10
    wrap.sprite.set_angle(mar, angle)
    angle += 10
    wrap.sprite.move(mar, 0, speedx1)




