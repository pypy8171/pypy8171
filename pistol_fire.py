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
        self.dir = 0
        self.a=0
        if Pistol_Fire.image == None:
            Pistol_Fire.image = load_image('pistol.png')

    def set_easybg(self, bg):
        self.bg = bg
    def set_normalbg(self,bg):
        self.bg=bg
    def set_hardbg(self,bg):
        self.bg=bg
    def set_bossbg(self,bg):
        self.bg=bg
    def set_cat(self,cat):
        self.cat=cat


    def update(self, frame_time):
        distance = Pistol_Fire.RUN_SPEED_PPS * frame_time
        self.x += (self.dir * distance)
        self.y = self.cat.y
        if self.cat.pistolfire !=1:
            self.x =self.cat.x+30

        if self.cat.pistolfire == 1:
            if self.cat.dir==1 or self.cat.dir==0:
                self.dir=4
            elif self.cat.dir==-1 or self.cat.dir==0:
                self.dir=-4

        if self.x>800:
            if  self.cat.pistolfire==0:
                self.x=self.cat.x
        if self.x<0:
            if self.cat.pistolfire==0:
                self.x=self.cat.x


        pass

    def stop(self):
        self.cat.pistolfire==0
        self.x=self.cat.x

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        if self.cat.pistolfire==1:
            self.image.draw( sx, sy)

    def get_bb(self):
        return self.x - 20-self.bg.window_left, self.y - 20-self.bg.window_bottom, self.x+20-self.bg.window_left, self.y+20-self.bg.window_bottom
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass


