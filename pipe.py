from pico2d import *

import random
import json

class Pipe1:
    image = None;

    def __init__(self):
        self.x, self.y = 425,150
        if Pipe1.image ==None:
            Pipe1.image = load_image('pause1.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)

    def get_bb(self):
        return self.x-50,self.y-80,self.x+45,self.y+60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


