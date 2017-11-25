from pico2d import *

import cat
import random
import json


class Easy_Land:
    image = None;

    def __init__(self):
        self.x, self.y = 0,0
        if Easy_Land.image ==None:
            Easy_Land.image = load_image('ground.png')

    def set_map1(self, bg):
        self.bg = bg

    def set_map2(self,bg):
        self.bg=bg

    def set_map3(self,bg):
        self.bg =bg

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x-self.bg.window_left,self.y-self.bg.window_bottom)

    def get_bb(self):
        return self.x - 20 - self.bg.window_left, self.y-35-self.bg.window_bottom,self.x+20-self.bg.window_left,self.y+35-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self,event):
        pass

