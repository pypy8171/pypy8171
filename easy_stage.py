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
from monster import Easy_Monster
#from pistol import Pistol

# 54M 짜리맵
name = "easy_stage"

cat = None
easybg = None
pipe = None
land = None
door=None
#pistol=None

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

    team_data_file = open('easymonster_data.txt','r')
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


def create_land():

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
    global cat,easybg, pipe,land, wall,door, pistol,monster
    door=Door()
    cat = Cat()
    easybg = Easy_Map()
    pipe = Pipe1()
    #land=Easy_Land()
    wall = create_land()
    pistol = Pistol_Fire()
    monster = create_team()


    for i in wall:
        i.set_easybg(easybg)
    easybg.set_center_object(cat)
    cat.set_easybg(easybg)
    pipe.set_easybg(easybg)
    #land.set_easybg(easybg)
    door.set_easybg(easybg)
    pistol.set_easybg(easybg)
    pistol.set_cat(cat)
    for monsters in monster:
        monsters.set_easybg(easybg)

def destroy_world():
    global cat,easybg,pipe,door,pistol,monster#,land

    del(monster)
    del(door)
    del(cat)
    del(easybg)
    del(pipe)
    #del(land)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        elif cat.x>1700:
            game_framework.change_state(normal_stage)


        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                cat.handle_event(event)
                easybg.handle_event(event)


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
    easybg.update(frame_time)
    pistol.update(frame_time)
    for monsters in monster:
        monsters.update(frame_time)



    for ground in wall:
        if collide(ground,cat):
            cat.stop()
    for monsters in monster:
        if collide(monsters,cat):
            cat.die()

    for monsters in monster:
        if collide(monsters,pistol):
            monsters.die()
            monster.remove(monsters)
            pistol.stop()
        if collide(pipe,pistol):
            pistol.stop()


    if collide(pipe,cat):
        print("collision")
        cat.stop_easypipe()

    if collide(door,cat):
        print("collision")
        cat.die()


def draw(frame_time):
    clear_canvas()

    pipe.draw()
    easybg.draw()
    cat.draw()
    pistol.draw()
    #land.draw()
    door.draw()
    for monsters in monster:
        monsters.draw()
    for ground in wall:
        ground.draw()

    #for monsters in monster:
    #    monsters.draw_bb()
    #pistol.draw_bb()
    #pipe.draw_bb()
    #easybg.draw_bb()
    #cat.draw_bb()
    #land.draw_bb()
    #door.draw_bb()
    #for ground in wall:
    #    ground.draw_bb()
    pass

    update_canvas()






