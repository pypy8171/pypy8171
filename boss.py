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

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND,JUMP= 1, 1, 1, 1,1

    def __init__(self):
        self.x, self.y = 600, 120
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.life_time = 0.0
        self.total_frames = 0.0
        self.frame=0
        self.total_frame=0
        self.dir = 0
        self.up = 0
        self.a=0
        self.updir=0

        if Boss.image == None:
            Boss.image = load_image('boss_animation.png')

    def set_map1(self, bg):
        self.bg = bg
    def set_map2(self,bg):
        self.bg=bg
    def set_map3(self,bg):
        self.bg=bg
    def set_map4(self,bg):
        self.bg=bg



    def update(self, frame_time):
        #def clamp(minimum, x, maximum):
        #    return max(minimum, min(x, maximum))
        #def clamp(minimum,y,maximum):
        #    return max(minimum,min(y,maximum))

        self.life_time += frame_time
        distance = Boss.RUN_SPEED_PPS * frame_time
        self.frame = int(self.total_frames+1) % 4
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



    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.clip_draw(self.frame*95,20,85,90, sx, sy)

    def remove(self):
        self.dir = 5
    def stoppipe(self):
        if self.up ==-2:
            self.up =0


        if self.x>430 and self.x<570 and self.y>65 and self.y<233:
            if self.dir==1:
                self.x-=2
            elif self.dir==-1:
                self.x+=2

    def stoppipe2(self):
        if self.up ==-2:
            self.up =0
        if self.x>1670 and self.x<1830 and self.y>65 and self.y<180:
            if self.dir==1:
                self.x-=2
            elif self.dir==-1:
                self.x+=2

    def stop(self):
        if self.up==-2:
            self.up=0

    def normal_stop(self):
        if self.up==-2:
            self.up=0
        if self.dir==1 and self.up==0:
            self.x-=4
        if self.dir==-1 and self.up==0:
            self.x+=4

    def block_stop(self):
        if self.dir==1 and self.up==2:
            self.up=-20
        if self.dir==-1 and self.up==2:
            self.up=-20


    def get_bb(self):
        return self.x - 20-self.bg.window_left, self.y - 40-self.bg.window_bottom, self.x+25-self.bg.window_left, self.y+40-self.bg.window_bottom
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










