from pico2d import *

import game_framework
import pause_state

import easy_stage
import normal_stage


from cat import Cat # import Boy class from boy.py
from map3 import Map3
from pipe import Pipe1






name = "hard_stage"

cat = None
map3 = None
pipe = None


def create_world():
    global cat,map3, pipe
    cat = Cat()
    map3 = Map3()
    pipe = Pipe1()

    map3.set_center_object(cat)
    cat.set_map3(map3)



def destroy_world():
    global cat,map3,pipe

    del(cat)
    del(map3)
    del(pipe)




def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                cat.handle_event(event)
                map3.handle_event(event)


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
    map3.update(frame_time)
    if collide(map3,cat):
        print("collision")
        cat.stop()
    if collide(pipe,cat):
        print("collision")
        cat.stop()




    #if collide(map3,cat):
       # print("collision")

def draw(frame_time):
    clear_canvas()

    pipe.draw()
    map3.draw()
    cat.draw()

    pipe.draw_bb()
    map3.draw_bb()
    cat.draw_bb()
    pass

    update_canvas()

