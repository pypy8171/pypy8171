import random

from pico2d import *

class Map1:

    def __init__(self):
        self.image= load_image('stage1.png')


    def draw(self):
        self.image.draw(835,300)
    #835 에서 -110 까지 -> 835 ~ -910

    def get_bb(self):
      return 0,0,3200,70


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
