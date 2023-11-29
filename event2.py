import wrap
import time
import math
import random


width = 600
height = 600
wrap.world.create_world(width, height)

tank = wrap.sprite.add("battle_city_tanks",30,30,"tank_enemy_size1_green1")

@wrap.always(1000)
def t_move():
    t_x = random.randint(10,width-10)
    t_y = random.randint(10,height-10)
    wrap.sprite.move_to(tank,t_x,t_y)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def t_reskin(pos_x,pos_y):
    click = wrap.sprite.is_collide_point(tank,pos_x,pos_y)
    if click == True:
        wrap.sprite.set_costume_next(tank)