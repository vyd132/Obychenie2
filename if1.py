import wrap
import random
import math
width = 600
height = 600
wrap.world.create_world(width,height)

x = random.randint(100,500)
y = random.randint(100,500)
pac_x = random.randint(100,500)
pac_y = random.randint(100,500)

dot = wrap.sprite.add("pacman",x,y,"dot")
pac = wrap.sprite.add("pacman",pac_x,pac_y,"enemy_blue_left1")
if x>=pac_x:
    wrap.sprite.set_costume(pac,"enemy_blue_right1" )



wrap.actions.move_to(pac,x,pac_y)
if y<=pac_y:
    wrap.sprite.set_costume(pac,"enemy_blue_up1" )
else:
    wrap.sprite.set_costume(pac,"enemy_blue_down1" )
wrap.actions.move_to(pac,x,y)