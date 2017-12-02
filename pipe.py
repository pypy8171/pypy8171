from pico2d import *

import cat
import random
import json

class Pipe1:
    image = None;

    def __init__(self):
        self.x, self.y = 505,150
        if Pipe1.image ==None:
            Pipe1.image = load_image('pipe.png')

    def set_easybg(self, bg):
        self.bg = bg

    #def set_normalbg(self,bg):
    #    self.bg=bg

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x-50-self.bg.window_left,self.y-80-self.bg.window_bottom,self.x+45-self.bg.window_left,self.y+50-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Pipe2:
    image = None;

    def __init__(self):
        self.x, self.y = 1760,150
        if Pipe2.image ==None:
            Pipe2.image = load_image('pipe.png')

    #def set_easybg(self, bg):
    #    self.bg = bg

    def set_normalbg(self,bg):
        self.bg=bg

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x-50-self.bg.window_left,self.y-85-self.bg.window_bottom,self.x+45-self.bg.window_left,self.y+5-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())




