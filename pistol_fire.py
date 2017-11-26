import random
import game_framework
import normal_stage
from pico2d import *


class Pistol_Fire:
    #pistol = []

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image=None


    def __init__(self):
        self.x, self.y = 100, 600
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.total_frame=0
        self.dir = 0
        self.up = 0
        self.a=0
        self.updir=0
        if Pistol_Fire.image == None:
            Pistol_Fire.image = load_image('pistol.png')

    def set_map1(self, bg):
        self.bg = bg
    def set_map2(self,bg):
        self.bg=bg
    def set_map3(self,bg):
        self.bg=bg
    def set_map4(self,bg):
        self.bg=bg



    def update(self, frame_time):

        pass

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.draw( sx, sy)




    def get_bb(self):
        return self.x - 20-self.bg.window_left, self.y - 20-self.bg.window_bottom, self.x+20-self.bg.window_left, self.y+20-self.bg.window_bottom
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass


