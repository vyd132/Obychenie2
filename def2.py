import wrap
import time

from wrap import world, sprite, sprite_text, actions

def say(num,slova):
    text = sprite.add_text(slova, sprite.get_x(num), sprite.get_top(num) - 20)
    time.sleep(0.5)
    sprite.remove(text)

def run(num,angle,dist):
    say(num,"Бежим!")
    actions.set_size_percent(num, 30, 30,500)
    actions.set_angle(num, angle,500)
    actions.move_at_angle_dir(num, dist,600)
    actions.set_size_percent(num, 100, 100,500)

def attack(dist,num):
    say(num,"В погоню!")
    actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), dist, 500)

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

victim = sprite.add("pacman", 300, 100, "player2")
hunter = sprite.add("pacman", 100, 100, "enemy_blue_right1")



run(victim,180,200)

attack(70,hunter)
attack(70,hunter)

run(victim,-135,200)

attack(70,hunter)