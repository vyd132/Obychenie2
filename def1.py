import wrap
import time
import random



def spawn(locx,locy):
    color = random.choice(["tank_enemy_size1_yellow1", "tank_enemy_size1_green1", "tank_enemy_size1_purple1"])
    star = wrap.sprite.add("battle_city_items", locx, locy, "effect_appearance1")
    sleep = 0.2
    wrap.sprite.set_costume(star,"effect_appearance2")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance3")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance4")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance3")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance2")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance1")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance2")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance3")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance4")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance3")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance2")
    time.sleep(sleep)
    wrap.sprite.set_costume(star, "effect_appearance1")
    wrap.sprite.remove(star)
    tank = wrap.sprite.add("battle_city_tanks", locx, locy, color)
    return tank

def tank_right(dist,num):
    wrap.actions.set_angle(num, 90)
    wrap.actions.move(num, dist, 0)


def tank_left(dist,num):
    wrap.actions.set_angle(num, 270)
    wrap.actions.move(num, -dist, 0)


def tank_up(dist,num):
    wrap.actions.set_angle(num, 0)
    wrap.actions.move(num, 0, -dist)


def tank_down(dist,num):
    wrap.actions.set_angle(num, 180)
    wrap.actions.move(num, 0, dist)



width = 600
height = 600
wrap.world.create_world(width, height)


tank = spawn(30,30)

tank_right(200,tank)
tank_down(100,tank)
tank_left(30,tank)
tank_up(70,tank)

tank1 = spawn(100,100)

tank_down(50,tank1)
tank_right(100,tank1)
tank_up(30,tank1)
tank_down(10,tank)