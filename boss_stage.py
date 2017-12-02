from pico2d import *

import game_framework
import pause_state

import title_state
import normal_stage
import hard_stage


from cat import Cat # import Boy class from boy.py
from boss_land import Boss_Land
from pistol_fire import Pistol_Fire
from boss_map import Boss_Map
from boss import Boss


name = "easy_stage"

cat = None
map1 = None
pipe = None
land = None
pistol=None

#24M짜리맵

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
GROUND_WIDTH_METER = 1.2
GROUND_HEIGHT_METER = 1.2

GROUND_WIDTH = (GROUND_WIDTH_METER * PIXEL_PER_METER)
GROUND_HEIGHT = (GROUND_HEIGHT_METER * PIXEL_PER_METER)

def create_land():
    land = []
    for i in range(0, 22):
        ground = Boss_Land()
        ground.x =20+GROUND_WIDTH*i
        ground.y = GROUND_HEIGHT
        land.append(ground)


    return land



def create_world():
    global cat,map4,land, wall,door, pistol,boss


    boss = Boss()
    cat = Cat()
    pistol=Pistol_Fire()
    map4=Boss_Map()
    land=Boss_Land()
    wall = create_land()



    for i in wall:
        i.set_map4(map4)
    map4.set_center_object(cat)
    cat.set_map4(map4)
    land.set_map4(map4)
    pistol.set_map4(map4)
    boss.set_map4(map4)
    pistol.set_cat(cat)

def destroy_world():
    global cat,map4,land,pistol


    del(cat)
    del(map4)
    del(land)
    del(pistol)





def enter():
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif boss.x>800:
            game_framework.push_state(title_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                cat.handle_event(event)
                map4.handle_event(event)
                pistol.handle_event(event)
                #land.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a>right_b:return False
    if right_a < left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False

    return True


def update(frame_time):

    cat.update(frame_time)
    map4.update(frame_time)
    land.update(frame_time)
    pistol.update(frame_time)
    boss.update(frame_time)

    for ground in wall:
        if collide(ground,boss):
            boss.Boss_Run(cat.Cat_Dir())

    if collide(boss,pistol):
        print("collistion")
        pistol.stop()
        boss.remove()

    for ground in wall:
        if collide(ground,cat):
            cat.stop()

    if collide(boss,cat):
        cat.die()


def draw(frame_time):
    clear_canvas()



    map4.draw()
    pistol.draw()
    cat.draw()
    land.draw()
    for ground in wall:
        ground.draw()
    boss.draw()


    map4.draw_bb()
    pistol.draw_bb()
    cat.draw_bb()
    land.draw_bb()
    boss.draw_bb()
    for ground in wall:
        ground.draw_bb()
    pass

    update_canvas()






