import wrap
import time

def ball_pass(num,to_num):
    ballx = wrap.sprite.get_x(ball)
    bally = wrap.sprite.get_y(ball)
    to_x = wrap.sprite.get_x(to_num)
    to_y =wrap.sprite.get_y(to_num)
    wrap.actions.move_to(num,ballx-30,bally-20,1500)
    wrap.actions.set_angle_to_point(ball,to_x,to_y)
    wrap.actions.move_to(ball,to_x-30,to_y)




width = 600
height = 600
wrap.world.create_world(width, height)

crab = wrap.sprite.add("mario-enemies",30,30,"crab")
plant = wrap.sprite.add("mario-enemies",30,height- 30,"plant_blue")
cloud = wrap.sprite.add("mario-enemies",width- 30,30,"cloud")
mar = wrap.sprite.add("mario-1-big",width- 30,height- 30,"stand")
ball = wrap.sprite.add("mario-enemies",width/2,height/2,"armadillo_egg")

ball_pass(crab,plant)