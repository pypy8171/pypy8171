import random
import json
import os
import game_framework
import easy_stage

from pico2d import *

import game_framework
import easy_stage
import normal_stage




name = "PauseState"

image = None
logo_time = 0.0
counter =0


class Pause:
    def __init__(self):
        self.x1, self.y1 = 400, 200
        self.image = load_image('pause.png')
        self.timer = 0;

    def update(self,frame_time):
        self.timer +=1
        if self.timer % 2 ==1:
            self.x1, self.y1 = 400,250
        elif self.timer%2 ==0:
            self.x1, self.y1 = 0,-300
        delay(0.3)

    def draw(self):
        self.image.draw(  self.x1, self.y1)

    def set_map1(self, bg):
        self.bg = bg
    def set_map2(self,bg):
        self.bg=bg
    def set_map3(self,bg):
        self.bg=bg
    def set_map4(self,bg):
        self.bg=bg

class Title:
    def __init__(self):
        self.image = load_image('easy_mode.png')

    def draw(self):
        self.image.draw(1550, 300)




def enter():
    global cat,pause
    pause =Pause()
    #cat = Cat()
    pass


def exit():
    global  pause#,cat

    #del(cat)
    del(pause)
    pass



def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            #if key is p , return main state
            game_framework.pop_state()


def update(frame_time):
    #pause.update()
    pass
#def update(): global counter counter = (counter+1)%100  깜빡거리는거 구현
#def draw(): global image clear_canvas() if counter<50) image.draw(400,300) update_canvas()
#하나씩 구현 ex) 퍼즈 띄우기 -> 깜박거리게 하기 -> 화면 끼워넣기

def draw(frame_time):
    clear_canvas()
    #title.draw()
    easy_stage.door.draw()
    easy_stage.pipe.draw()
    easy_stage.map1.draw()
    for easy_stage.ground in easy_stage.wall:
        easy_stage.ground.draw()
    #grass.draw 대신 main_state.draw_main_scene
    #easy_stage.map1.image.draw(1550+easy_land.easy_land.x,easy_land.easy_land.y)
    easy_stage.cat.image.clip_draw(easy_stage.cat.frame * 100, easy_stage.cat.state*100, 100, 100, easy_stage.cat.x, easy_stage.cat.y)

    #normal_stage.cat.image.clip_draw(normal_stage.cat.frame * 100, normal_stage.cat.state * 100, 100, 100, normal_stage.cat.x,
    #                                 normal_stage.cat.y)
    pause.draw()
    update_canvas()





