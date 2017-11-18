from pico2d import *

import game_framework
import pause_state

import easy_stage
import normal_stage


from cat import Cat # import Boy class from boy.py
from map3 import Map3
from fake_portal import Fruit
from land3 import Land3







name = "hard_stage"

cat = None
map3 = None

def create_land():
    land = []
    #처음 시작 지점 땅
    for i in range(0, 7):
        ground = Land3()
        ground.x =20+42*i
        ground.y = 200
        land.append(ground)

    #한칸 아래
    for i2 in range(0,3):
        ground=Land3()
        ground.x=308+42*i2
        ground.y = 180
        land.append(ground)

    #처음 시작 박스 오른쪽 벽
    for i3 in range(0,5):
        ground=Land3()
        ground.x = 390
        ground.y=180-42*i3
        land.append(ground)


    #두번째 박스
    for i4 in range(0,5):
        for i5 in range(0,6):
            ground = Land3()
            ground.x = 635+42*i5
            ground.y = 180 - 42 * i4
            land.append(ground)

    #첫뻔째 두번째 사이 박스 하나
    for i6 in range(0,1):
        ground=Land3()
        ground.x=550
        ground.y=133
        land.append(ground)

    for i7 in range(0,2):
        ground=Land3()
        ground.x = 985+42*i7
        ground.y=270
        land.append(ground)

    for i8 in range(0,1):
        ground = Land3()
        ground.x = 1195
        ground.y =310
        land.append(ground)

    #3개짜리
    for i9 in range(0,3):
        ground = Land3()
        ground.x = 1360
        ground.y =400-42*i9
        land.append(ground)

    #ㄴ 지형1
    for j in range(0,2):
        ground = Land3()
        ground.x = 1487
        ground.y =300+42*j
        land.append(ground)

    #ㄴ 지형2
    for j2 in range(0,5):
        ground = Land3()
        ground.x = 1487+43*j2
        ground.y =265
        land.append(ground)

    #ㄴ 다음 박스
    for j3 in range(0,6):
        for j4 in range(0,5):
            ground = Land3()
            ground.x = 1850+43*j4
            ground.y= 225-43*j3
            land.append(ground)

    #마지막 지면
    for j5 in range(0,20):
        for j6 in range(0,2):
            ground = Land3()
            ground.x = 2158+42*j5
            ground.y = 52-42*j6
            land.append(ground)



    return land

def create_world():
    global cat,map3,fruit,wall
    wall=create_land()
    fruit=Fruit()
    cat = Cat()
    map3 = Map3()


    for i in wall:
        i.set_map3(map3)
    map3.set_center_object(cat)
    cat.set_map3(map3)
    fruit.set_map3(map3)



def destroy_world():
    global cat,map3,fruit

    del(cat)
    del(map3)
    del(fruit)





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

    for ground in wall:
        if collide(ground, cat):
            cat.stop()



    if collide(fruit,cat):
        cat.start()





    #if collide(map3,cat):
       # print("collision")

def draw(frame_time):
    clear_canvas()

    map3.draw()
    cat.draw()
    fruit.draw()
    for ground in wall:
        ground.draw()

    map3.draw_bb()
    cat.draw_bb()
    fruit.draw_bb()
    for ground in wall:
        ground.draw_bb()
    pass

    update_canvas()


