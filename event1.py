import wrap
import time
import math


width = 600
height = 600
wrap.world.create_world(width, height)
pac = wrap.sprite.add("pacman",30,30,"player2")
ghost = wrap.sprite.add("pacman",30,height-30,)

@wrap.on_key_down(wrap.K_RIGHT,wrap.K_LEFT)
def angle_move(key):
    if key == wrap.K_RIGHT:
        angle = wrap.sprite.get_angle(pac)
        wrap.sprite.set_angle(pac,angle+30)
    else:
        angle = wrap.sprite.get_angle(pac)
        wrap.sprite.set_angle(pac,angle-30)

@wrap.on_key_always(wrap.K_UP,delay=60)
def move_up():
    wrap.sprite.move_at_angle_dir(pac,10)

@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def click():
    wrap.sprite.set_costume(ghost,"enemy_pink_right1")

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def click():
    wrap.sprite.set_costume(ghost,"enemy_ill_blue1")

@wrap.on_mouse_move()
def click(pos_x,pos_y):
    wrap.sprite.move_to(ghost,pos_x,pos_y)

@wrap.always(1000)
def click(pos_x,pos_y):
    print("hi")


@wrap.always(50)
def eat(pos_x,pos_y):
    cost = wrap.sprite.get_costume(ghost)
    if cost == "enemy_ill_blue1":
        ghostx=wrap.sprite.get_x(ghost)
        ghosty = wrap.sprite.get_y(ghost)
        wrap.sprite.set_angle_to_point(pac, ghostx, ghosty)
        wrap.sprite.move_at_angle_point(pac,ghostx,ghosty,5)
    elif cost == "enemy_pink_right1":
        ghostx = wrap.sprite.get_x(ghost)
        ghosty = wrap.sprite.get_y(ghost)
        wrap.sprite.set_angle_to_point(pac, ghostx, ghosty)
        angle = wrap.sprite.get_angle(pac)
        wrap.sprite.set_angle(pac, angle-180)
        wrap.sprite.move_at_angle_point(pac, ghostx, ghosty, -5)
