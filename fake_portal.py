from pico2d import *

import cat
import random
import json


class Door:
    image = None;

    def __init__(self):
        self.x, self.y = 1543,110
        if Door.image ==None:
            Door.image = load_image('easy_portal.png')

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
        return self.x - 20 - self.bg.window_left, self.y-35-self.bg.window_bottom,self.x-self.bg.window_left,self.y+30-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def handle_event(self,event):
        pass

class Flag:
    image = None;

    def __init__(self):
        self.x, self.y = 2033,90
        if Flag.image ==None:
            Flag.image = load_image('easy_portal.png')

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
        return self.x - 20 - self.bg.window_left, self.y-20-self.bg.window_bottom,self.x-self.bg.window_left,self.y+50-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def handle_event(self,event):
        pass

class Fruit:
    image = None;

    def __init__(self):
        self.x, self.y = 2563,105
        if Fruit.image ==None:
            Fruit.image = load_image('easy_portal.png')

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
        return self.x - 20 - self.bg.window_left, self.y-30-self.bg.window_bottom,self.x-self.bg.window_left,self.y+25-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def handle_event(self,event):
        pass



