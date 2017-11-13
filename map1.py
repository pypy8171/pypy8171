import random

from pico2d import *

class Map1:
    def __init__(self):
        self.image= load_image('easy_mode.png')

    def draw(self):
        self.image.draw(1600,300)

    def get_bb(self):
      return 0,0,3200,80

    def draw_bb(self):
        draw_rectangle(*self.get_bb())