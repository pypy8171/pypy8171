from pico2d import *

import game_framework
import pause_state

import easy_stage
import normal_stage
import boss_stage

from cat import Cat # import Boy class from boy.py
from hard_map import Hard_Map
from fake_portal import Fruit
from hard_land import Hard_Land
from normal_dieblock import Dieblock
from help_block import Helpblock
from thorn import Hard_Thorn
from fireball import Fire_Ball
from pistol_fire import Pistol_Fire
from monster import Easy_Monster

# 84M짜리맵
name = "hard_stage"

cat = None
hardbg = None

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
GROUND_WIDTH_METER = 1.2
GROUND_HEIGHT_METER = 1.2

GROUND_WIDTH = (GROUND_WIDTH_METER * PIXEL_PER_METER)
GROUND_HEIGHT = (GROUND_HEIGHT_METER * PIXEL_PER_METER)


def create_team():

    player_state_table = {
        "LEFT_RUN" : Easy_Monster.LEFT_RUN,
        "RIGHT_RUN" : Easy_Monster.RIGHT_RUN,
    }

    #team_data = json.loads(team_data_text)

    team_data_file = open('hardmonster_data.txt','r')
    team_data = json.load(team_data_file)
    team_data_file.close()

    team = []
    for name in team_data:
        player = Easy_Monster()
        player.name = name
        player.x = team_data[name]['x']
        player.y = team_data[name]['y']
        player.state = player_state_table[team_data[name]['StartState']]
        team.append(player)

    return team


def create_fireball():
    fires = []
    for i in range(0,1):
        fire = Fire_Ball()
        fire.x = GROUND_WIDTH*11
        fire.y = 0
        fires.append(fire)

    return fires

def create_diethorn():
    thorns=[]
    for i0 in range(0,1):
        thorn = Hard_Thorn()
        thorn.x = 530+GROUND_WIDTH*i0
        thorn.y = 130
        thorns.append(thorn)

    for i0 in range(0,2):
        thorn = Hard_Thorn()
        thorn.x = 2320+GROUND_WIDTH*i0
        thorn.y = 53
        thorns.append(thorn)
    return thorns

def create_dieblock():
    blocks=[]
    for i in range(0,2):
        block=Dieblock()
        block.x=1200+GROUND_WIDTH*i
        block.y = 12.5*GROUND_HEIGHT
        blocks.append(block)

    return blocks

def create_helpblock():
    hblocks = []
    for i in range(0, 2):
        hblock = Helpblock()
        hblock.x = 1250 + GROUND_WIDTH * i
        hblock.y = 4.5*GROUND_HEIGHT
        hblocks.append(hblock)

    return hblocks

def create_land():
    land = []
    #처음 시작 지점 땅
    #for i in range(0, 7):
    ground = Hard_Land()
    ground.ynum=5
    ground.xnum=10
    ground.x =30+GROUND_WIDTH*ground.xnum/2
    ground.y = 3*GROUND_HEIGHT
    land.append(ground)


    #처음 시작 박스 오른쪽 벽


    #두번째 박스
    ground = Hard_Land()
    ground.xnum=6
    ground.ynum=5
    ground.x = 630+GROUND_WIDTH*ground.xnum/2
    ground.y = 20+GROUND_HEIGHT*ground.ynum/2
    land.append(ground)

    #첫뻔째 두번째 사이 박스 하나
    ground = Hard_Land()
    ground.xnum = 1
    ground.ynum = 1
    ground.x = 530 + GROUND_WIDTH * ground.xnum / 2
    ground.y = 120 + GROUND_HEIGHT * ground.ynum / 2
    land.append(ground)

    ground = Hard_Land()
    ground.xnum = 2
    ground.ynum = 1
    ground.x = 990 + GROUND_WIDTH * ground.xnum / 2
    ground.y = 267 + GROUND_HEIGHT * ground.ynum / 2
    land.append(ground)


    ground = Hard_Land()
    ground.xnum = 1
    ground.ynum = 1
    ground.x = 1195+GROUND_WIDTH*ground.xnum/2
    ground.y =310+ GROUND_HEIGHT* ground.ynum/2
    land.append(ground)

    #3개짜리

    ground = Hard_Land()
    ground.xnum=1
    ground.ynum=3
    ground.x = 1380
    ground.y =435-GROUND_HEIGHT*ground.ynum/2
    land.append(ground)

    ground = Hard_Land()
    ground.xnum = 2
    ground.ynum = 2
    ground.x = 1440
    ground.y = 100 - GROUND_HEIGHT * ground.ynum / 2
    land.append(ground)

    ground = Hard_Land()
    ground.xnum = 6
    ground.ynum = 6
    ground.x = 1600
    ground.y = 220 - GROUND_HEIGHT * ground.ynum / 2
    land.append(ground)

    ground = Hard_Land()
    ground.xnum = 4
    ground.ynum = 6
    ground.x = 1945
    ground.y = 260 - GROUND_HEIGHT * ground.ynum / 2
    land.append(ground)

    ground = Hard_Land()
    ground.xnum = 20
    ground.ynum = 2
    ground.x = 2565
    ground.y = 90 - GROUND_HEIGHT * ground.ynum / 2
    land.append(ground)

    return land

def create_world():
    global cat,hardbg,fruit,wall,blocks,hblocks,thorns,fires,pistol,monster

    hblocks = create_helpblock()
    blocks = create_dieblock()
    thorns = create_diethorn()
    fires = create_fireball()
    wall = create_land()
    fruit=Fruit()
    cat = Cat()
    hardbg = Hard_Map()
    pistol=Pistol_Fire()
    monster=create_team()


    for i in wall:
        i.set_hardbg(hardbg)
    for i in blocks:
        i.set_hardbg(hardbg)
    for i in hblocks:
        i.set_hardbg(hardbg)
    for i in thorns:
        i.set_hardbg(hardbg)
    for i in fires:
        i.set_hardbg(hardbg)
    for i in monster:
        i.set_hardbg(hardbg)
    hardbg.set_center_object(cat)
    cat.set_hardbg(hardbg)
    fruit.set_hardbg(hardbg)
    pistol.set_hardbg(hardbg)
    pistol.set_cat(cat)



def destroy_world():
    global cat,hardbg,fruit,blocks,hblocks,thorns,fires,pistol,monster

    del(monster)
    del(pistol)
    del(fires)
    del(thorns)
    del(hblocks)
    del(blocks)
    del(cat)
    del(hardbg)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            game_framework.push_state(boss_stage)
        elif cat.x>2650:
            game_framework.change_state(boss_stage)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                cat.handle_event(event)
                hardbg.handle_event(event)


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
    hardbg.update(frame_time)
    pistol.update(frame_time)

    for monsters in monster:
        monsters.update(frame_time)
    for fire in fires:
        fire.update(frame_time)

    if fire.y>600:
        fire.y=0

    for ground in wall:
        if collide(ground, cat) :
            cat.stop2()
        if collide(ground, cat) and ground.y<cat.y:
            cat.stop_hard()

    if collide(fruit,cat):
        cat.start()

    for block in blocks:
        if collide(block,cat):
            #print("clollision")
            Dieblock.image = load_image("hard_tile.png")
            cat.block_stop()

    for thorn in thorns:
        if collide(thorn,cat):
            Hard_Thorn.image = load_image("hard_thorn.png")
            cat.die()

    if collide(fire,cat):
        cat.die()


#수정 필용ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ
    if cat.y >550:
        Dieblock.image = load_image("die_block.png")
        Helpblock.image = load_image("die_block.png")
        Hard_Thorn.image = load_image("hard_tile.png")

    for hblock in hblocks:
        if collide(hblock, cat):
            # print("clollision")
            Helpblock.image = load_image("hard_tile.png")
            cat.help_stop()



def draw(frame_time):
    clear_canvas()

    hardbg.draw()
    cat.draw()
    fruit.draw()
    pistol.draw()
    for ground in wall:
        ground.draw()
    for block in blocks:
        block.draw()
    for hblock in hblocks:
        hblock.draw()
    for thorn in thorns:
        thorn.draw()
    for fire in fires:
        fire.draw()
    for monsters in monster:
        monsters.draw()


    #hardbg.draw_bb()
    #cat.draw_bb()
    #fruit.draw_bb()
    #for ground in wall:
    #    ground.draw_bb()
    #for block in blocks:
    #    block.draw_bb()
    #for hblock in hblocks:
    #    hblock.draw_bb()
    #for thorn2 in thorns:
    #    thorn2.draw_bb()
    pass

    update_canvas()


