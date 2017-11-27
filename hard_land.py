from pico2d import *

import cat
import random
import json


class Hard_Land:
    image = None;

    def __init__(self):
        self.x, self.y = 0,30
        self.xnum =0
        self.ynum =0
        if Hard_Land.image ==None:
            Hard_Land.image = load_image('hard_tile.png')

    def set_map1(self, bg):
        self.bg = bg

    def set_map2(self,bg):
        self.bg=bg

    def set_map3(self,bg):
        self.bg =bg

    def update(self, frame_time):
        pass

    def draw(self):
        for i in range(0,self.xnum):
            for j in range(0,self.ynum):
                self.image.draw(self.x+(i*40)-(40*self.xnum/2)-self.bg.window_left,self.y+(j*40)-(40*self.ynum/2)-self.bg.window_bottom)

    def get_bb(self):
        return self.x - 20-(40*self.xnum/2) - self.bg.window_left, self.y-20-(40*self.ynum/2)-self.bg.window_bottom,self.x+20+(40*self.xnum/2-40)-self.bg.window_left,self.y-20+(40*self.ynum/2)-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def handle_event(self,event):
        pass
