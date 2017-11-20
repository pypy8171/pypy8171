from pico2d import *

import game_framework
import pause_state

import easy_stage
import hard_stage
import boss_stage

from cat import Cat # import Boy class from boy.py
from map2 import Map2
from pipe import Pipe2
from land2 import Land2
from normal_obstacle import Obstacle2
from fake_portal import Flag
from normal_dieblock import Dieblock


name = "normal_stage"

cat =None
map2 = None
pipe = None

def create_dieblock():
    blocks=[]
    for i in range(0,2):
        block=Dieblock()
        block.x=950+40*i
        block.y = 600
        blocks.append(block)

    return blocks


def create_obstacle():
    obstacle = []

    for i in range(0,1):
        ob=Obstacle2()
        ob.x = 625+40*i
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
        ob.y = 87+ 40*j
        obstacle.append(ob)

    for j in range(0,2):
        ob=Obstacle2()
        ob.x = 1271
        ob.y = 87+ 40*j
        obstacle.append(ob)

    for k in range(0,3):
        ob=Obstacle2()
        ob.x = 787
        ob.y = 87+43*k
        obstacle.append(ob)

    for k in range(0,3):
        ob=Obstacle2()
        ob.x = 1183
        ob.y = 87+43*k
        obstacle.append(ob)

    for l in range(0,4):
        ob=Obstacle2()
        ob.x = 877
        ob.y = 87+43*l
        obstacle.append(ob)

    for l in range(0,4):
        ob=Obstacle2()
        ob.x = 1097
        ob.y = 87+43*l
        obstacle.append(ob)


    return obstacle
def create_land():
    land = []
    for i in range(0, 22):
        ground = Land2()
        ground.x =20+40*i
        ground.y = 35
        land.append(ground)

    for k in range(0, 11):
        ground = Land2()
        ground.x =1100+40*k
        ground.y = 35
        land.append(ground)

    for j in range(0,7):
        ground = Land2()
        ground.x = 1640+40*j
        ground.y = 35
        land.append(ground)

    for k in range(0,4):
        ground=Land2()
        ground.x=2000+40*k
        ground.y=35
        land.append(ground)
    #for j in range(0,21):
     #   ground = Land2()
      #  ground.x = 1000+ 40*j
     #   ground.y = 40
      #  land.append(ground)


    return land

def create_world():
    global cat,map2, pipe, land,wall,obstacle, flag,blocks
    blocks = create_dieblock()
    flag = Flag()
    obstacle=create_obstacle()
    cat = Cat()
    map2 = Map2()
    pipe = Pipe2()
    land = Land2()
    wall = create_land()

    for i in wall:
        i.set_map2(map2)
    for i in obstacle:
        i.set_map2(map2)
    for i in blocks:
        i.set_map2(map2)
    map2.set_center_object(cat)
    cat.set_map2(map2)
    pipe.set_map2(map2)
    land.set_map2(map2)
    flag.set_map2(map2)



def destroy_world():
    global cat,map2,pipe,land,obstacle,flag,blocks


    del(cat)
    del(map2)
    del(pipe)
    del(land)
    del(obstacle)
    del(flag)
    del(blocks)




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
        elif cat.x>2100:
            #game_framework.change_state(hard_stage)
            game_framework.change_state(boss_stage)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                cat.handle_event(event)
                map2.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a>right_b:return False
    if right_a < left_b:return False
    if top_a<bottom_b:return False
    if bottom_a>top_b:return False

    return True


#a=None
def update(frame_time):
    #global a
    cat.update(frame_time)
    map2.update(frame_time)

    for ground in wall:
        if collide(ground, cat):
            #print("collision")
            cat.stop()

    for block in blocks:
        if collide(block,cat):
            #print("clollision")
            Dieblock.image = load_image("hard_tile.png")
            cat.block_stop()

    # 죽었을때 다시 감추는거
    if cat.y>550:
        Dieblock.image = load_image("die_block2.png")




    for ob in obstacle:
        if collide(ob,cat):
            print("collision")
            cat.normal_stop()

    if collide(pipe,cat):
        #print("collision")
        cat.stoppipe2()
        #a=1

    if collide(flag, cat):
        cat.start()




    #if collide(map2,cat):
       # print("collision")

def draw(frame_time):
    clear_canvas()

    pipe.draw()
    map2.draw()
    cat.draw()
    land.draw()
    flag.draw()
    for block in blocks:
        block.draw()
    for ground in wall:
        ground.draw()
    for ob in obstacle:
        ob.draw()

    pipe.draw_bb()
    map2.draw_bb()
    cat.draw_bb()
    flag.draw_bb()
    for ground in wall:
        ground.draw_bb()
    for ob in obstacle:
        ob.draw_bb()
    for block in blocks:
        block.draw_bb()

    pass

    update_canvas()


