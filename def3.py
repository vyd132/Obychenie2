import wrap
import time



def ball_pass(num,to_num):
    ball_grab(num)
    to_x = wrap.sprite.get_x(to_num)
    to_y =wrap.sprite.get_y(to_num)
    numx = wrap.sprite.get_x(num)
    numy = wrap.sprite.get_y(num)
    if numx>to_x:
        wrap.actions.move_to(ball,numx-30,numy+10)
        wrap.actions.set_angle_to_point(ball,to_x,to_y)
        wrap.actions.move_to(ball,to_x+30,to_y)
    else:
        wrap.actions.move_to(ball, numx + 30, numy + 10)
        wrap.actions.set_angle_to_point(ball, to_x, to_y)
        wrap.actions.move_to(ball, to_x - 30, to_y)


def ball_grab(num):
    ballx = wrap.sprite.get_x(ball)
    bally = wrap.sprite.get_y(ball)
    numx = wrap.sprite.get_x(num)
    if ballx > numx:
        wrap.actions.move_to(num, ballx - 30, bally - 20, 1500)
    else:
        wrap.actions.move_to(num, ballx + 30, bally - 20, 1500)


def ball_kick(num,x,y):
    ball_grab(num)
    ballx = wrap.sprite.get_x(ball)
    bally = wrap.sprite.get_y(ball)
    numx = wrap.sprite.get_x(num)
    wrap.actions.move_to(ball, x, y)



width = 600
height = 600
wrap.world.create_world(width, height)

crab = wrap.sprite.add("mario-enemies",30,30,"crab")
plant = wrap.sprite.add("mario-enemies",30,height- 30,"plant_blue")
cloud = wrap.sprite.add("mario-enemies",width- 30,30,"cloud")
mar = wrap.sprite.add("mario-1-big",width- 30,height- 30,"stand")
ball = wrap.sprite.add("mario-enemies",width/2,height/2,"armadillo_egg")

ball_pass(mar,crab)
ball_pass(crab,mar)
ball_pass(plant,cloud)
ball_grab(mar)
ball_kick(plant,300,500)