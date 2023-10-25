import wrap

width = 200
height = 500
wrap.world.create_world(width,height)

y = 400
x1 = 300
x2 = 600

wrap.sprite.add("mario-items",25,y,"moving_platform1")
wrap.sprite.add("mario-items",width - 25,y,"moving_platform1")
wrap.sprite.add("mario-items",x1,y,"moving_platform1")
wrap.sprite.add("mario-items",x2,y,"moving_platform1")
stand = y -40
wrap.sprite.add("mario-1-big",25,stand,"stand")

jump = (x1-25)/2

wrap.actions.move_to(4,jump + 25,stand-jump)
wrap.actions.move_to(4,x1,stand)
jump = (x2-x1)/2
wrap.actions.move_to(4,jump + x1,stand-jump)
wrap.actions.move_to(4,x2,stand)
last = width - 25
jump = (last-x2)/2
wrap.actions.move_to(4,jump + x2,stand-jump)
wrap.actions.move_to(4,last,stand)
jump = (last-25)/2
wrap.actions.move_to(4,jump + 25,stand-jump)
wrap.actions.move_to(4,25,stand)



