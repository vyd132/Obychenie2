import wrap
import random
import math
import time

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

def boom(x,y):
    sleep = 0.2
    time.sleep(sleep)
    expl = wrap.sprite.add("battle_city_items", x, y, "effect_explosion1")
    time.sleep(sleep)
    wrap.sprite.set_costume(expl, "effect_explosion2")
    time.sleep(sleep)
    wrap.sprite.set_costume(expl, "effect_explosion3")
    time.sleep(sleep)
    wrap.sprite.set_costume(expl, "effect_explosion2")
    time.sleep(sleep)
    wrap.sprite.set_costume(expl, "effect_explosion1")
    time.sleep(sleep)
    wrap.sprite.remove(expl)

def tank_up(dist,num):
    wrap.actions.set_angle(num, 0)
    wrap.actions.move(num, 0, -dist)


def tank_down(dist,num):
    wrap.actions.set_angle(num, 180)
    wrap.actions.move(num, 0, dist)


def tank_fire(numf,nums,dist):
    txf = wrap.sprite.get_x(numf)
    tyf = wrap.sprite.get_y(numf)
    txs = wrap.sprite.get_x(nums)
    tys = wrap.sprite.get_y(nums)
    wrap.actions.set_angle_to_point(numf, txs, tys)
    bullet = wrap.sprite.add("battle_city_items",txf,tyf,"bullet")
    wrap.sprite.set_angle_to_point(bullet, txs, tys)
    wrap.actions.move_at_angle_point(bullet,txs,tys,dist)
    col = wrap.sprite.is_collide_sprite(bullet,nums)
    bx = wrap.sprite.get_x(bullet)
    by = wrap.sprite.get_y(bullet)
    wrap.sprite.remove(bullet)
    boom(bx,by)
    if col == True:
        wrap.sprite.remove(nums)



width = 600
height = 600
wrap.world.create_world(width, height)


tank = spawn(30,30)

tank_right(300,tank)
tank_down(100,tank)
tank_left(30,tank)
tank_up(70,tank)

tank1 = spawn(100,100)



tank_down(50,tank1)
tank_right(100,tank1)
tank_up(30,tank1)
tank_down(10,tank)

tank_fire(tank1,tank,200)
tank_fire(tank,tank1,100)