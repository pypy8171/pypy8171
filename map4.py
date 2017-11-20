import random

from pico2d import *

class Map4:
    def __init__(self):
        self.image= load_image('boss_stage.png')
        self.speed=0
        self.canvas_width=get_canvas_width()
        self.canvas_height=get_canvas_height()
        self.w=self.image.w
        self.h=self.image.h

    def set_center_object(self,cat):
        self.center_object=cat

    def draw(self):
        #self.image.draw(835,300)
    #835 에서 -110 까지 -> 835 ~ -910
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width, self.canvas_height,
            0, 0)

    def update(self,frame_time):
        self.window_left=clamp(0,
            int(self.center_object.x) - self.canvas_width//2,
            self.w - self.canvas_width)
        self.window_bottom=clamp(0,
            int(self.center_object.y) - self.canvas_height//2,
            self.h - self.canvas_height)

    def get_bb(self):
        pass
    def draw_bb(self):
        pass
    def handle_event(self,event):
        pass