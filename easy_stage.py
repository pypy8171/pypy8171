from pico2d import *

import game_framework
import pause_state

import title_state
import normal_stage
import hard_stage


from cat import Cat # import Boy class from boy.py
from easy_map import Easy_Map
from pipe import Pipe1
from easy_land import Easy_Land
from fake_portal import Door
from pistol_fire import Pistol_Fire

#from pistol import Pistol

# 540m 짜리맵
name = "easy_stage"

cat = None
map1 = None
pipe = None
land = None
door=None
#pistol=None

PIXEL_PER_METER = (10.0 / 3)  # 10 pixel 300 cm
GROUND_WIDTH_METER = 12
GROUND_HEIGHT_METER = 12

GROUND_WIDTH = (GROUND_WIDTH_METER * PIXEL_PER_METER)
GROUND_HEIGHT = (GROUND_HEIGHT_METER * PIXEL_PER_METER)

def create_land():
    PIXEL_PER_METER = (10.0 / 3)  # 10 pixel 30 cm
    Easy_Map_Size=10/3 # 10 pixel 3m
    #ground 하나에 12M

    land = []
    for i in range(0, 22):
        ground = Easy_Land()
        ground.x =20+GROUND_WIDTH*i
        ground.y = GROUND_HEIGHT
        land.append(ground)

    for j in range(0,21):
        ground = Easy_Land()
        ground.x = 1000+ GROUND_WIDTH*j
        ground.y = GROUND_HEIGHT
        land.append(ground)


    return land



def create_world():
    global cat,map1, pipe,land, wall,door, pistol
    door=Door()
    cat = Cat()
    map1 = Easy_Map()
    pipe = Pipe1()
    land=Easy_Land()
    wall = create_land()
    pistol = Pistol_Fire()


    for i in wall:
        i.set_map1(map1)
    map1.set_center_object(cat)
    cat.set_map1(map1)
    pipe.set_map1(map1)
    land.set_map1(map1)
    door.set_map1(map1)
    pistol.set_map1(map1)
    pistol.set_cat(cat)

def destroy_world():
    global cat,map1,pipe,land,door,pistol

    del(door)
    del(cat)
    del(map1)
    del(pipe)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_n:
            game_framework.push_state(normal_stage)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_h:
            game_framework.push_state(hard_stage)
        elif cat.x>1700:
            game_framework.change_state(normal_stage)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                cat.handle_event(event)
                map1.handle_event(event)


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
    map1.update(frame_time)
    pistol.update(frame_time)


    for ground in wall:
        if collide(ground,cat):
            cat.stop()
        #elif collide(ground,pistol):
            #pistol.stop()

    if collide(pipe,cat):
        print("collision")
        cat.stoppipe()

    if collide(door,cat):
        print("collision")
        cat.die()

    #if collide(land,cat):
        #print("collision")
        #cat.stop()


    #if collide(map1,cat):
       # print("collision")

def draw(frame_time):
    clear_canvas()

    pipe.draw()
    map1.draw()
    cat.draw()
    pistol.draw()
    land.draw()
    door.draw()
    for ground in wall:
        ground.draw()

    #pistol.draw_bb()
    #pipe.draw_bb()
    #map1.draw_bb()
    #cat.draw_bb()
    land.draw_bb()
    #door.draw_bb()
    #for ground in wall:
    #    ground.draw_bb()
    pass

    update_canvas()






