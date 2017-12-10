from pico2d import *

import game_framework
import pause_state

import easy_stage
import hard_stage
import boss_stage

from cat import Cat # import Boy class from boy.py
from normal_map import Normal_Map
from pipe import Pipe2
from normal_land import Normal_Land
from normal_obstacle import Obstacle2
from fake_portal import Flag
from normal_dieblock import Dieblock
from thorn import Normal_Thorn
from pistol_fire import Pistol_Fire
from monster import Easy_Monster
from help_block import Helpblock

#66M 짜리맵
name = "normal_stage"

cat =None
normalbg = None
pipe = None

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

    team_data_file = open('normalmonster_data.txt','r')
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


def create_diethorn():
    thorns=[]
    for i0 in range(0,2):
        thorn = Normal_Thorn()
        thorn.x = 100+GROUND_WIDTH*i0
        thorn.y = 5*GROUND_HEIGHT
        thorns.append(thorn)

    for i in range(0,1):
        thorn = Normal_Thorn()
        thorn.x = 1185 +GROUND_WIDTH*i
        thorn.y = 4.5*GROUND_WIDTH
        thorns.append(thorn)

    for i2 in range(0,1):
        thorn=Normal_Thorn()
        thorn.x = 980+GROUND_WIDTH*i2
        thorn.y=4*GROUND_HEIGHT
        thorns.append(thorn)

    return thorns

def create_dieblock():
    blocks=[]
    for i in range(0,2):
        block=Dieblock()
        block.x=1000+GROUND_WIDTH*i
        block.y = 600
        blocks.append(block)

    return blocks

def create_helpblock():

    return blocks
    pass

def create_obstacle():
    obstacle = []

    for i in range(0,1):
        ob=Obstacle2()
        ob.x = 625+GROUND_WIDTH*i
        ob.y = 87
        obstacle.append(ob)

    for i in range(0,1):
        ob=Obstacle2()
        ob.x = 1359
        ob.y = 87
        obstacle.append(ob)

    for j in range(0,2):
        ob=Obstacle2()
        ob.x = 700
        ob.y = 87+ GROUND_HEIGHT*j
        obstacle.append(ob)

    for j in range(0,2):
        ob=Obstacle2()
        ob.x = 1271
        ob.y = 87+ GROUND_HEIGHT*j
        obstacle.append(ob)

    for k in range(0,3):
        ob=Obstacle2()
        ob.x = 787
        ob.y = 87+(GROUND_HEIGHT+3)*k
        obstacle.append(ob)

    for k in range(0,3):
        ob=Obstacle2()
        ob.x = 1183
        ob.y = 87+(GROUND_HEIGHT+3)*k
        obstacle.append(ob)

    for l in range(0,4):
        ob=Obstacle2()
        ob.x = 877
        ob.y = 87+(GROUND_HEIGHT+3)*l
        obstacle.append(ob)

    for l in range(0,4):
        ob=Obstacle2()
        ob.x = 1097
        ob.y = 87+(GROUND_HEIGHT+3)*l
        obstacle.append(ob)


    return obstacle
def create_land():
    land = []
    for i in range(0, 22):
        ground = Normal_Land()
        ground.x =20+GROUND_WIDTH*i
        ground.y = GROUND_HEIGHT-5
        land.append(ground)

    for k in range(0, 11):
        ground = Normal_Land()
        ground.x =1100+GROUND_WIDTH*k
        ground.y = GROUND_HEIGHT-5
        land.append(ground)

    for j in range(0,7):
        ground = Normal_Land()
        ground.x = 1640+GROUND_WIDTH*j
        ground.y = GROUND_HEIGHT-5
        land.append(ground)

    for k in range(0,4):
        ground=Normal_Land()
        ground.x=2000+GROUND_WIDTH*k
        ground.y=GROUND_HEIGHT-5
        land.append(ground)

    return land

def create_world():
    global cat,normalbg, pipe, wall,obstacle, flag,blocks,thorns,pistol,monster#,land

    blocks = create_dieblock()
    thorns = create_diethorn()
    flag = Flag()
    obstacle=create_obstacle()
    cat = Cat()
    normalbg = Normal_Map()
    pipe = Pipe2()
    #land = Normal_Land()
    wall = create_land()
    pistol = Pistol_Fire()
    monster = create_team()

    for i in wall:
        i.set_normalbg(normalbg)
    for i in obstacle:
        i.set_normalbg(normalbg)
    for i in blocks:
        i.set_normalbg(normalbg)
    for i in thorns:
        i.set_normalbg(normalbg)
    for i in monster:
        i.set_normalbg(normalbg)
    normalbg.set_center_object(cat)
    cat.set_normalbg(normalbg)
    pipe.set_normalbg(normalbg)
    #land.set_normalbg(normalbg)
    flag.set_normalbg(normalbg)
    pistol.set_normalbg(normalbg)
    pistol.set_cat(cat)



def destroy_world():
    global cat,normalbg,pipe,obstacle,flag,blocks,thorns,pistol,monster#,land

    del(monster)
    del(cat)
    del(normalbg)
    del(pipe)
    #del(land)
    del(obstacle)
    del(flag)
    del(blocks)
    del(thorns)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_h:
            game_framework.push_state(hard_stage)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        elif cat.x>2100:
            game_framework.change_state(hard_stage)
            #game_framework.change_state(boss_stage)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                cat.handle_event(event)
                normalbg.handle_event(event)


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
    normalbg.update(frame_time)
    pistol.update(frame_time)
    for monsters in monster:
        monsters.update(frame_time)

    for monsters in monster:
        if collide(monsters,cat):
            cat.die()

    for monsters in monster:
        if collide(monsters,pistol):
            monsters.die()
            monster.remove(monsters)
            pistol.stop()
        if collide(pistol,pipe):
            pistol.stop()

    for ground in wall:
        if collide(ground, cat):
            cat.stop()

    for block in blocks:
        if collide(block,cat):
            Dieblock.image = load_image("normal_tile.png")
            cat.block_stop()

    for thorn in thorns:
        if collide(thorn, cat):
            Normal_Thorn.image = load_image("thorn.png")
            cat.die()

    # 죽었을때 다시 감추는거
    if cat.y>550:
        Dieblock.image = load_image("die_block.png")
        Normal_Thorn.image = load_image("normal_tile.png")


    for ob in obstacle:
        if collide(ob,cat):
            print("collision")
            cat.normal_stop()

    if collide(pipe,cat):
        cat.stop_normalpipe()


    if collide(flag, cat):
        cat.start()

def draw(frame_time):
    clear_canvas()

    pipe.draw()
    normalbg.draw()
    cat.draw()
    pistol.draw()
    #land.draw()
    flag.draw()
    for block in blocks:
        block.draw()
    for thorn in thorns:
        thorn.draw()
    for ground in wall:
        ground.draw()
    for ob in obstacle:
        ob.draw()
    for monsters in monster:
        monsters.draw()


    #pipe.draw_bb()
    #normalbg.draw_bb()
    #cat.draw_bb()
    #flag.draw_bb()
    #for ground in wall:
    #    ground.draw_bb()
    #for ob in obstacle:
    #    ob.draw_bb()
    #for block in blocks:
    #    block.draw_bb()
    #for thorn in thorns:
    #    thorn.draw_bb()



    pass

    update_canvas()


