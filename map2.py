import random

from pico2d import *

class Map2:
    def __init__(self):
        self.image= load_image('stage2.png')
        self.speed=0
        self.canvas_width=get_canvas_width()
        self.canvas_height=get_canvas_height()
        self.w=self.image.w
        self.h=self.image.h
        self.bgm = load_music('normal_sound.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def set_center_object(self,cat):
        self.center_object=cat

    def draw(self):
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
      #return 0-self.window_left,0-self.window_bottom,3200-self.window_left,60-self.window_bottom
        pass

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass

    def handle_event(self,event):
        pass
