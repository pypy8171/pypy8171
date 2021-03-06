import random
import game_framework

from pico2d import *


class Boss:

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    hit_sound = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND,JUMP= 0, 1, 0, 1,1

    def __init__(self):
        self.x, self.y = 750, 120
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.life_time = 0.0
        self.total_frames = 0.0
        self.frame=0
        self.total_frame=0
        self.dir = 0
        self.up = 0
        self.pistolfire=2
        self.updir=0
        self.state = self.LEFT_STAND

        if Boss.image == None:
            Boss.image = load_image('boss_animation.png')
        if Boss.hit_sound==None:
            Boss.hit_sound=load_wav('hit.wav')
            Boss.hit_sound.set_volume(32)

    def set_bossbg(self,bg):
        self.bg=bg
    def set_cat(self,cat):
        self.cat=cat
    def hit(self):
        self.hit_sound.play()



    def update(self, frame_time):
        self.life_time += frame_time
        distance = Boss.RUN_SPEED_PPS * frame_time
        self.frame = int(self.total_frames+1) % 5
        self.total_frames += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME * frame_time
        self.total_frame += Boss.FRAMES_PER_ACTION * Boss.ACTION_PER_TIME*frame_time

        self.x += (self.dir * distance)
        self.y +=(self.up*distance)

        self.x = clamp(0, self.x, self.bg.w+200)
        self.y = clamp(-120,self.y,self.bg.h)

        self.a = self.total_frame
        print("%d" % self.a)



        if self.a%8>7:
            self.up, self.updir=-2,1
#        elif self.updir==1 and self.y<115:
#            self.up, self.updir=0,0

    def Boss_Run(self, cat):
        if self.x>cat:
            self.dir=-0.5
            self.state = self.LEFT_RUN
        if self.x<cat:
            self.dir=0.5
            self.state=self.RIGHT_RUN
        if self.up == -2:
            self.up = 0

    def kill(self):
        if self.cat.y>500:
            self.x, self.y = 750, 120

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.clip_draw(self.frame*130,self.state*100,100,100, sx, sy)

    def remove(self):
        self.dir = 600
        self.hit()


    def get_bb(self):
        return self.x - 10-self.bg.window_left, self.y - 40-self.bg.window_bottom, self.x-self.bg.window_left, self.y+20-self.bg.window_bottom
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN,self.JUMP):
                self.state = self.LEFT_RUN
                self.dir = -1

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN,self.JUMP):
                self.state = self.RIGHT_RUN
                self.dir = 1

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,self.JUMP):
                self.state = self.LEFT_STAND
                self.dir = 0

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,self.JUMP):
                self.state = self.RIGHT_STAND
                self.dir = 0

        elif (event.type, event.key)==(SDL_KEYDOWN,SDLK_UP):
            if self.state in(self.RIGHT_STAND,self.RIGHT_RUN,self.LEFT_STAND, self.LEFT_RUN):
                if self.up<1 and self.up>-1:
                    self.state = self.JUMP
                    self.up = 2
                    self.total_frame=0










