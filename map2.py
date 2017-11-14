import random

from pico2d import *

class Map2:

    def __init__(self):
        self.image= load_image('stage2.png')

    def draw(self):
        self.image.draw(1100,300)

    def get_bb(self):
      return 0,0,3200,60


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
