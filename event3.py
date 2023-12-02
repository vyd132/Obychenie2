import wrap
import time
import math
import random

click = 0

width = 600
height = 600
wrap.world.create_world(width, height)


tank = wrap.sprite.add("battle_city_tanks",45,45,"tank_enemy_size4_purple1")
princ = wrap.sprite.add("mario-princess",width/2,height/2,"princess")
ghost = wrap.sprite.add("pacman",width-45,height-45,"enemy_blue_left1")

@wrap.on_key_always(wrap.K_RIGHT,wrap.K_LEFT)
def angle(pos_x,pos_y,keys):
    colid_tank = wrap.sprite.is_collide_point(tank,pos_x,pos_y)
    colid_princ = wrap.sprite.is_collide_point(princ, pos_x, pos_y)
    colid_ghost = wrap.sprite.is_collide_point(ghost, pos_x, pos_y)

    if colid_tank == True:
        id= tank

    if colid_princ == True:
        id= princ

    if colid_ghost == True:
        id = ghost

    if wrap.K_RIGHT in keys:
        a = 10
    else:
        a = -10
    angle = wrap.sprite.get_angle(id)
    wrap.sprite.set_angle(id, angle + a)





