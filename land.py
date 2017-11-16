from pico2d import *

import cat
import random
import json

class Land:
    image = None;

    def __init__(self):
        self.x, self.y = 200,150
        if Land.image ==None:
            Land.image = load_image('pause1.png')

    def set_map1(self, bg):
        self.bg = bg

    def set_map2(self,bg):
        self.bg=bg

    def set_map3(self,bg):
        self.bg =bg

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return 0-self.bg.window_left,0-self.bg.window_bottom,870-self.bg.window_left,70-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


