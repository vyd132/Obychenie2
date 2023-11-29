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
    wrap.sprite.move_to(ghost, pos_x - 10, pos_y)
    ghostx = wrap.sprite.get_x(ghost)
    ghosty = wrap.sprite.get_y(ghost)
    if ghostx >= width-10:
        wrap.sprite.move_to(ghost,ghostx-15,ghosty)
    elif ghostx <= 10:
        wrap.sprite.move_to(ghost,15,ghosty)

    if ghosty >= height-10:
        wrap.sprite.move_to(ghost,ghostx,ghosty-15)
    elif ghosty <= 10:
        wrap.sprite.move_to(ghost,ghostx,15)


@wrap.always(1000)
def click(pos_x,pos_y):
    print("hi")



@wrap.always(50)
def eat(pos_x,pos_y):
    cost = wrap.sprite.get_costume(ghost)
    ghostx = wrap.sprite.get_x(ghost)
    ghosty = wrap.sprite.get_y(ghost)
    wrap.sprite.set_angle_to_point(pac, ghostx, ghosty)


    if cost == "enemy_ill_blue1":
        wrap.sprite.move_at_angle_point(pac,ghostx,ghosty,5)


    elif cost == "enemy_pink_right1":
        angle = wrap.sprite.get_angle(pac)
        wrap.sprite.set_angle(pac, angle-180)
        wrap.sprite.move_at_angle_point(pac, ghostx, ghosty, -5)

    right = wrap.sprite.get_right(pac)
    left = wrap.sprite.get_left(pac)
    top = wrap.sprite.get_top(pac)
    bottom = wrap.sprite.get_bottom(pac)

    if right >= width:
        wrap.sprite.move_right_to(pac, width)
    elif left <= 0:
        wrap.sprite.move_left_to(pac, 0)

    if top <= 0:
        wrap.sprite.move_top_to(pac, 0)
    elif bottom >= height:
        wrap.sprite.move_bottom_to(pac, height)




    pacx = wrap.sprite.get_x(pac)
    pacy = wrap.sprite.get_y(pac)
    print(pacx,pacy)

