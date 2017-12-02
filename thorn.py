from pico2d import *

import cat
import random
import json


class Normal_Thorn:
    image = None;

    def __init__(self):
        self.x, self.y = 100 ,200
        if Normal_Thorn.image ==None:
            Normal_Thorn.image = load_image('normal_tile.png')

    def set_normalbg(self,bg):
        self.bg=bg

    def set_hardbg(self,bg):
        self.bg =bg

    def set_boss(self,bg):
        self.bg =bg

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x-self.bg.window_left,self.y-self.bg.window_bottom)

    def get_bb(self):
        return self.x - 20 - self.bg.window_left, self.y-20-self.bg.window_bottom,self.x+20-self.bg.window_left,self.y+20--self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def handle_event(self,event):
        pass


class Hard_Thorn:
    image = None;

    def __init__(self):
        self.x, self.y = 100 ,200
        if Hard_Thorn.image ==None:
            Hard_Thorn.image = load_image('hard_tile.png')

    #def set_easybg(self, bg):
    #    self.bg = bg

    def set_normalbg(self,bg):
        self.bg=bg

    def set_hardbg(self,bg):
        self.bg =bg

    #def set_bossbg(self,bg):
    #    self.bg =bg

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x-self.bg.window_left,self.y-self.bg.window_bottom)

    def get_bb(self):
        return self.x - 20 - self.bg.window_left, self.y-20-self.bg.window_bottom,self.x+20-self.bg.window_left,self.y+20--self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def handle_event(self,event):
        pass

