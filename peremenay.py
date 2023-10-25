import wrap
width = 700
height = 700
x1 = 100
y1 = 100
x2 = 300
y2 = 200
x3 = 500
y3 = 70
wrap.world.create_world(width,height)
wrap.sprite.add("pacman",x1,y1,"dot")
wrap.sprite.add("pacman",x2,y2,"dot")
wrap.sprite.add("pacman",x3,y3,"dot")
wrap.sprite.add_text("Точка 1",x1 + 10, y1 - 20, text_color=[255,255,255])
wrap.sprite.add_text("Точка 2",x2 + 10, y2 - 20, text_color=[255,255,255])
wrap.sprite.add_text("Точка 3",x3 + 10, y3 - 20, text_color=[255,255,255])
wrap.sprite.add("pacman", width / 2, height / 2,"player1")
wrap.sprite.add("pacman",30,height / 2,"enemy_blue_left1")
wrap.sprite.add("pacman",width - 30,height / 2,"enemy_yellow_left1")
wrap.sprite.add("pacman",width / 2, 30,"enemy_pink_left1")
wrap.sprite.add("pacman",width / 2,height - 30,"enemy_red_left1")
wrap.actions.move_to(6,x1,height / 2)
wrap.actions.move_to(6,x1,y1)
wrap.actions.move_to(6,x2,y1)
wrap.actions.move_to(6,x2,y2)
wrap.actions.move_to(6,x3,y2)
wrap.actions.move_to(6,x3,y3)
wrap.actions.move_to(7,width / 2, height / 2)
wrap.actions.move_to(9,30, 30)
wrap.actions.move_to(9,30,height / 2)
wrap.actions.move_to(8,width - 30,30)
wrap.actions.move_to(8,width / 2, 30)
wrap.actions.move_to(10,width - 30,height - 30)
wrap.actions.move_to(10,width - 30,height / 2)
wrap.actions.move_to(6,x3,height - 30)
wrap.actions.move_to(6,width / 2,height - 30)






