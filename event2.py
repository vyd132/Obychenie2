import wrap
import time
import math
import random

click = 0

width = 600
height = 600
wrap.world.create_world(width, height)

tank = wrap.sprite.add("battle_city_tanks",30,30,"tank_enemy_size1_green1")
pric = wrap.sprite.add("pacman",30,30,"player1",False)
wrap.sprite.set_size(pric,1,1)
wrap.sprite.set_angle(pric,0)

@wrap.always(1000)
def t_move():
    t_x = random.randint(10,width-10)
    t_y = random.randint(10,height-10)
    wrap.sprite.move_to(tank,t_x,t_y)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def t_reskin(pos_x,pos_y):
    click = wrap.sprite.is_collide_sprite(pric,tank)
    if click == True:
        wrap.sprite.set_costume_next(tank)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def t_reskin(pos_x,pos_y):
    click = wrap.sprite.is_collide_point(tank,pos_x,pos_y)
    if click == True:
        wrap.sprite.set_costume_next(tank)

@wrap.on_mouse_down(wrap.BUTTON_RIGHT)
def size():
    global click
    wrap.sprite.set_size(pric,30,30)
    wrap.sprite.show(pric)
    click = click+1
    if click == 2:
        wrap.sprite.set_size(pric,45,45)
    elif click == 3:
        wrap.sprite.set_size(pric, 60, 60)
    elif click == 4:
        wrap.sprite.hide(pric)
        wrap.sprite.set_size(pric,1,1)
        click = 0



@wrap.on_mouse_move()
def pric_move(pos_x,pos_y):
    wrap.sprite.move_to(pric, pos_x, pos_y)
    right = wrap.sprite.get_right(pric)
    left = wrap.sprite.get_left(pric)
    top = wrap.sprite.get_top(pric)
    bottom = wrap.sprite.get_bottom(pric)

    if right >= width:
        wrap.sprite.move_right_to(pric, width)
    elif left <= 0:
        wrap.sprite.move_left_to(pric, 0)

    if top <= 0:
        wrap.sprite.move_top_to(pric, 0)
    elif bottom >= height:
        wrap.sprite.move_bottom_to(pric, height)

