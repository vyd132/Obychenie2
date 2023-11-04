import wrap
import random
import math
import time
width = 400
height = 800
wrap.world.create_world(width,height)



turtle = wrap.sprite.add("mario-enemies", 30, 400, "turtle_blue_stand")
mar = wrap.sprite.add("mario-2-big",width-30, 100, "stand")
wrap.sprite.set_reverse_x(turtle, 180)
wrap.sprite.set_reverse_x(mar, 180)



speedx1 = random.randint(5, 20)
speedx = random.randint(5, 20)
while True:
    a = time.time()
    print(a)
    wrap.sprite.move(turtle, 0, speedx)
    y = wrap.sprite.get_y(turtle)
    if y >= 770:
        speedx = -random.randint(5, 20)
    elif y <= 40:
        speedx = random.randint(5, 20)

    wrap.sprite.move(mar, 0, speedx1)
    y = wrap.sprite.get_y(mar)
    if y >= 770:
        speedx1 = -random.randint(5, 20)
    elif y <= 40:
        speedx1 = random.randint(5, 20)






