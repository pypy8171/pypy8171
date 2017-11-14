import random

from pico2d import *

class Map3:

    def __init__(self):
        self.image= load_image('stage3.png')

    def draw(self):
        self.image.draw(1300,300)

    def get_bb(self):
      pass


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
