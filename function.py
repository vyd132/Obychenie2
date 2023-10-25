import random
import wrap

width = 500
height = 500
wrap.world.create_world(width,height)
rand = random.randint(100,500)
rand1 = random.randint(100,500)
rand2 = random.randint(100,400)
rand3 = random.randint(100,500)

dot = wrap.sprite.add("pacman",rand1,rand2,"dot")
pac = wrap.sprite.add("pacman",rand3,rand,"player1")
size = random.randint(50,500)
wrap.sprite.set_size_percent(pac,size,size)
wrap.actions.set_angle_to_point(pac,rand1,rand2)
wrap.actions.move_to(pac,rand1,rand2)
wrap.sprite.remove(dot)

go = wrap.sprite.get_top(pac)
place = random.randint(-50,50)
ghost = wrap.sprite.add("pacman",rand1-place,-100,"enemy_yellow_right1")
wrap.actions.move_to(ghost,rand1-place,go - 30)
x = wrap.sprite.get_x(ghost)
y = wrap.sprite.get_y(ghost)
wrap.actions.set_angle_to_point(pac,rand1-place,go-30)
angle = wrap.sprite.get_angle(pac)
wrap.actions.set_angle(pac,angle+180)
wrap.actions.move_at_angle_dir(pac,100)

