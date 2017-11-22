from pico2d import *

import game_framework
import pause_state

import easy_stage
import normal_stage
import boss_stage

from cat import Cat # import Boy class from boy.py
from map3 import Map3
from fake_portal import Fruit
from land3 import Land3
from normal_dieblock import Dieblock
from help_block import Helpblock
from thorn import Thorn()

name = "hard_stage"

cat = None
map3 = None

def create_diethorn():
    thorns=[]
    for i0 in range(0,2):
        thorn = Thorn()
        thorn.x = 100+40*i0
        thorn.y = 200
        thorns.append(thorn)
    return thorns

def create_dieblock():
    blocks=[]
    for i in range(0,2):
        block=Dieblock()
        block.x=1200+40*i
        block.y = 500
        blocks.append(block)

    return blocks

def create_helpblock():
    hblocks = []
    for i in range(0, 2):
        hblock = Helpblock()
        hblock.x = 1250 + 40 * i
        hblock.y = 180
        hblocks.append(hblock)

    return hblocks

def create_land():
    land = []
    #처음 시작 지점 땅
    #for i in range(0, 7):
    ground = Land3()
    ground.ynum=5
    ground.xnum=10
    ground.x =30+40*ground.xnum/2
    ground.y = 120
    land.append(ground)


    #처음 시작 박스 오른쪽 벽


    #두번째 박스
    ground = Land3()
    ground.xnum=6
    ground.ynum=5
    ground.x = 630+40*ground.xnum/2
    ground.y = 20+40*ground.ynum/2
    land.append(ground)

    #첫뻔째 두번째 사이 박스 하나
    ground = Land3()
    ground.xnum = 1
    ground.ynum = 1
    ground.x = 530 + 40 * ground.xnum / 2
    ground.y = 120 + 40 * ground.ynum / 2
    land.append(ground)

    ground = Land3()
    ground.xnum = 2
    ground.ynum = 1
    ground.x = 990 + 40 * ground.xnum / 2
    ground.y = 267 + 40 * ground.ynum / 2
    land.append(ground)


    ground = Land3()
    ground.xnum = 1
    ground.ynum = 1
    ground.x = 1195+40*ground.xnum/2
    ground.y =310+ 40* ground.ynum/2
    land.append(ground)

    #3개짜리

    ground = Land3()
    ground.xnum=1
    ground.ynum=3
    ground.x = 1380
    ground.y =435-40*ground.ynum/2
    land.append(ground)

    ground = Land3()
    ground.xnum = 2
    ground.ynum = 2
    ground.x = 1440
    ground.y = 100 - 40 * ground.ynum / 2
    land.append(ground)

    ground = Land3()
    ground.xnum = 6
    ground.ynum = 6
    ground.x = 1600
    ground.y = 220 - 40 * ground.ynum / 2
    land.append(ground)

    ground = Land3()
    ground.xnum = 4
    ground.ynum = 6
    ground.x = 1945
    ground.y = 260 - 40 * ground.ynum / 2
    land.append(ground)

    ground = Land3()
    ground.xnum = 20
    ground.ynum = 2
    ground.x = 2565
    ground.y = 90 - 40 * ground.ynum / 2
    land.append(ground)

    return land

def create_world():
    global cat,map3,fruit,wall,blocks,hblocks

    hblocks = create_helpblock()
    blocks = create_dieblock()
    wall=create_land()
    fruit=Fruit()
    cat = Cat()
    map3 = Map3()


    for i in wall:
        i.set_map3(map3)
    for i in blocks:
        i.set_map3(map3)
    for i in hblocks:
        i.set_map3(map3)
    map3.set_center_object(cat)
    cat.set_map3(map3)
    fruit.set_map3(map3)



def destroy_world():
    global cat,map3,fruit,blocks,hblocks

    del(hblocks)
    del(blocks)
    del(cat)
    del(map3)
    del(fruit)


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
        elif cat.x>2650:
            game_framework.change_state(boss_stage)
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
        #if collide(ground, cat) and ground.y-20< cat.y+20 :
        #    cat.stop()
        if collide(ground, cat) :
            cat.stop2()
        if collide(ground, cat) and ground.y<cat.y:
            cat.stop_hard()
        #elif collide(ground,cat) and ground.


    if collide(fruit,cat):
        cat.start()

    for block in blocks:
        if collide(block,cat):
            #print("clollision")
            Dieblock.image = load_image("hard_tile.png")
            cat.block_stop()


#수정 필용ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ
    if cat.y >550:
        Dieblock.image = load_image("die_block2.png")
        Helpblock.image = load_image("die_block2.png")

    for hblock in hblocks:
        if collide(hblock, cat):
            # print("clollision")
            Helpblock.image = load_image("hard_tile.png")
            cat.help_stop()



def draw(frame_time):
    clear_canvas()

    map3.draw()
    cat.draw()
    fruit.draw()
    for ground in wall:
        ground.draw()
    for block in blocks:
        block.draw()
    for hblock in hblocks:
        hblock.draw()


    map3.draw_bb()
    cat.draw_bb()
    fruit.draw_bb()
    for ground in wall:
        ground.draw_bb()
    for block in blocks:
        block.draw_bb()
    for hblock in hblocks:
        hblock.draw_bb()
    pass

    update_canvas()


