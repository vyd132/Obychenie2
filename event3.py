import wrap
import time
import math
import random

click = 0

width = 600
height = 600
wrap.world.create_world(width, height)



tank = wrap.sprite.add("battle_city_tanks",width/2,height/2,"tank_enemy_size4_purple1")
princ = wrap.sprite.add("mario-princess",width/2,height/2,"princess")
ghost = wrap.sprite.add("pacman",width/2,height/2,"enemy_blue_left1")

def mouse(pos_x,pos_y):
    colid_tank = wrap.sprite.is_collide_point(tank, pos_x, pos_y)
    colid_princ = wrap.sprite.is_collide_point(princ, pos_x, pos_y)
    colid_ghost = wrap.sprite.is_collide_point(ghost, pos_x, pos_y)
    id = None

    if colid_tank == True:
        id = tank

    if colid_ghost == True:
        id = ghost

    if colid_princ == True:
        id = princ


    return id


@wrap.on_key_always(wrap.K_RIGHT,wrap.K_LEFT)
def angle(pos_x,pos_y,keys):
    id = mouse(pos_x,pos_y)
    if id == None:
        return
    if wrap.K_RIGHT in keys:
        a = 10
    else:
        a = -10
    angle = wrap.sprite.get_angle(id)
    wrap.sprite.set_angle(id, angle + a)


@wrap.on_key_always(wrap.K_UP,wrap.K_DOWN)
def sprite(pos_x,pos_y,keys):
    id = mouse(pos_x, pos_y)
    if id == None:
        return
    if wrap.K_UP in keys:
        wrap.sprite.set_costume_next(id)
    elif wrap.K_DOWN in keys:
        wrap.sprite.set_costume_prev(id)

@wrap.on_mouse_down(wrap.BUTTON_WHEELUP,wrap.BUTTON_WHEELDOWN)
def size(pos_x,pos_y,button):
    id = mouse(pos_x, pos_y)
    if id == None:
        return
    if button == wrap.BUTTON_WHEELUP:
        sprite_width = wrap.sprite.get_width_percent(id)
        sprite_height = wrap.sprite.get_height_percent(id)
        wrap.sprite.set_size_percent(id,sprite_width+5,sprite_height+5)
    elif button == wrap.BUTTON_WHEELDOWN:
        sprite_width = wrap.sprite.get_width_percent(id)
        sprite_height = wrap.sprite.get_height_percent(id)
        wrap.sprite.set_size_percent(id, sprite_width - 5, sprite_height - 5)





