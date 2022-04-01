"""
На экране в любых местах стоят три спрайта.
Если мышь над спрайтом и нажата клавиша вверх или вниз, то его костюм меняется на следующий или предыдущий соответственно.

Если мышь над спрайтом и нажата клавиша вправо или влево, то он начинает вращаться вправо или влево,
  пока нажата клавиша и мышь находится над ним.

Если мышь над спрайтом и вращается колесико мыши, то размер спрайта увеличивается или
  уменьшается на 1 пиксель с сохранением пропорций (исп номер клавиши мыши wrap.BUTTON_WHEELUP, wrap.BUTTON_WHEELDOWN).
"""
import wrap
wrap.world.create_world(600,800,200,200)
p1=wrap.sprite.add("pacman",300,200,"enemy_blue_down1")
p2=wrap.sprite.add("pacman",100,200,"enemy_blue_up2")
p3=wrap.sprite.add("pacman",500,200,"enemy_ill_blue1")
@wrap.on_key_down(wrap.K_DOWN)
def down(pos_x,pos_y):
    if wrap.sprite.is_collide_point(p1,pos_x,pos_y) == True:
        wrap.sprite.set_costume_next(p1)

@wrap.on_key_down(wrap.K_UP)
def up(pos_x,pos_y):
    if wrap.sprite.is_collide_point(p1,pos_x,pos_y) == True:
        wrap.sprite.set_costume_prev(p1)

@wrap.on_key_down(wrap.K_LEFT)
def left(pos_x,pos_y):
    if wrap.sprite.is_collide_point(p2,pos_x,pos_y)== True:
        modif=wrap.sprite.get_angle(p2)
        wrap.sprite.set_angle(p2,modif+7)

@wrap.on_key_down(wrap.K_RIGHT)
def right(pos_x,pos_y):
    if wrap.sprite.is_collide_point(p2,pos_x,pos_y)== True:
        modif=wrap.sprite.get_angle(p2)
        wrap.sprite.set_angle(p2,modif-7)

@wrap.on_mouse_down(wrap.BUTTON_WHEELUP)
def wheelup(pos_x,pos_y):
    if wrap.sprite.is_collide_point(p3,pos_x,pos_y) == True:
        sx=wrap.sprite.get_(p3)
        sy=wrap.sprite.get_size(p3)
        wrap.sprite.set_size(p3,,1)



