from pico2d import *

import cat
import random
import json

running = True

class Fire_Ball:
    global running
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    image = None;

    def __init__(self):
        self.x=100
        self.y=100
        self.up=1
        if Fire_Ball.image ==None:
            Fire_Ball.image = load_image('fire.png')

    def set_map1(self, bg):
        self.bg = bg

    def set_map2(self,bg):
        self.bg=bg

    def set_map3(self,bg):
        self.bg =bg

    def update(self, frame_time):
        self.y = self.up*frame_time
        pass

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom)

    def get_bb(self):
        return self.x-50-self.bg.window_left,self.y-80-self.bg.window_bottom,self.x+45-self.bg.window_left,self.y+50-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        if running==True:
            self.up+=3


