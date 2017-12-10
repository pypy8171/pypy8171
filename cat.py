import random
import game_framework
import normal_stage
from pico2d import *





class Cat:

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image=None
    jump_sound=None
    pistol_sound=None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND,LEFT_JUMP,RIGHT_JUMP= 0, 1, 0, 1,2,3

    def __init__(self):
        self.x, self.y = 100, 500
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.total_frame=0
        self.dir = 0
        self.up = 0
        self.jumpstate=0
        self.updir=0
        self.ystate=0
        self.xstate=0
        self.state = self.RIGHT_STAND
        self.index=0
        self.pistolfire=0
      # if Cat.image==None: 인경우
        Cat.image = load_image('cat_animation.png')
        if Cat.jump_sound==None:
            Cat.jump_sound=load_wav('Jump.wav')
            Cat.jump_sound.set_volume(32)
        if Cat.pistol_sound==None:
            Cat.pistol_sound=load_wav('pistol.wav')
            Cat.pistol_sound.set_volume(32)

    def jump(self):
        self.jump_sound.play()
    def pistol(self):
        self.pistol_sound.play()
    def set_easybg(self, bg):
        self.bg = bg
    def set_normalbg(self,bg):
        self.bg=bg
    def set_hardbg(self,bg):
        self.bg=bg
    def set_bossbg(self,bg):
        self.bg=bg

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Cat.RUN_SPEED_PPS * frame_time
        self.total_frames += Cat.FRAMES_PER_ACTION * Cat.ACTION_PER_TIME * frame_time
        self.total_frame += Cat.FRAMES_PER_ACTION * Cat.ACTION_PER_TIME*frame_time
        self.frame = int(self.total_frames+1) % 5
        self.x += (self.dir * distance)

        if self.ystate ==0:
            self.y +=(self.up*distance)

        self.x = clamp(0, self.x, self.bg.w)
        self.y = clamp(-120,self.y,self.bg.h)

        self.jumpstate = self.total_frame

        if self.jumpstate%8>7:
            self.up, self.updir=-2,1


        if self.y<-0:
            self.x ,self.y = 100,600


    def Cat_Dir(self):
        return self.x

    def Cat_x(self):
        return self.x

    def Cat_y(self):
        return self.y

    def draw(self):
        sx = self.x - self.bg.window_left
        sy = self.y - self.bg.window_bottom
        self.image.clip_draw(self.frame * 100, self.state * 100, 93, 100, sx, sy)

    def stop_easypipe(self):
        if self.up ==-2:
            self.up =0

        if self.x>430 and self.x<570 and self.y>65 and self.y<233:
            if self.dir==1:
                self.x-=3
            elif self.dir==-1:
                self.x+=3

    def stop_normalpipe(self):
        if self.up ==-2:
            self.up =0

        if self.x>1670 and self.x<1830 and self.y>65 and self.y<180:
            if self.dir==1:
                self.x-=3
            elif self.dir==-1:
                self.x+=3

    def stop(self):
        if self.up ==-2:
            self.up =0
            self.y +=5
        pass


    def stop_hard(self):
        self.ystate = 0
        if self.up ==-2:
            self.dir*=-1
            self.up=0
            self.y +=10

    def move_hard(self):
        if self.dir==-1:
            self.dir=1
            self.x+=5
        elif self.dir==1:
            self.dir=-1
            self.x-=5

    def normal_stop(self):
        if self.up==-2:
            self.up=0
        if self.dir==1 and self.up==0:
            self.x-=4
        if self.dir==-1 and self.up==0:
            self.x+=4

    def block_stop(self):
        if self.dir==1 and self.up==2:
            self.up=-12
        if self.dir==-1 and self.up==2:
            self.up=-12

    def help_stop(self):
        if self.up==-2:
            self.up =0

        pass

    def die(self):
        self.dir=0
        self.up=0
        Cat.image = load_image("blood.png")
        delay(0.05)
        if self.jumpstate%3>2:
            self.start()
            self.jumpstate=0
    def die_boss(self):
        self.start()

    def start(self):
        Cat.image = load_image("cat_animation.png")
        self.x = 100
        self.y = 700
        self.up =-2


    def get_bb(self):
        return self.x - 20-self.bg.window_left, self.y - 40-self.bg.window_bottom, self.x+25-self.bg.window_left, self.y+40-self.bg.window_bottom
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN,self.LEFT_JUMP,self.RIGHT_JUMP):
                self.ystate = 0
                self.state = self.LEFT_RUN
                self.dir = -1
                self.index=-1
                #normal_stage.a=0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.ystate = 0
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN,self.LEFT_JUMP,self.RIGHT_JUMP):
                self.state = self.RIGHT_RUN
                self.dir = 1
                self.index =1
                #normal_stage.a=0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.ystate = 0
            if self.state in (self.LEFT_RUN,self.RIGHT_STAND,self.RIGHT_RUN,self.LEFT_JUMP,self.RIGHT_JUMP):
                self.state = self.LEFT_STAND
                self.dir = 0
                #normal_stage.a=0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.ystate=0
            if self.state in (self.RIGHT_RUN,self.LEFT_STAND,self.LEFT_RUN,self.LEFT_JUMP,self.RIGHT_JUMP):
                self.state = self.RIGHT_STAND
                self.dir = 0
                #normal_stage.a=0
        elif (event.type, event.key)==(SDL_KEYDOWN,SDLK_UP):
            self.ystate = 0
            if self.state in(self.LEFT_STAND, self.LEFT_RUN,self.LEFT_JUMP):
                if self.up < 1 and self.up > -1:
                    self.state = self.LEFT_JUMP
                    self.up = 2
                    self.total_frame=0
                    self.jump()

            elif self.state in(self.RIGHT_RUN,self.RIGHT_STAND,self.RIGHT_JUMP):
                if self.up < 1 and self.up > -1:
                    self.state =  self.RIGHT_JUMP
                    self.up = 2
                    self.total_frame=0
                    self.jump()

        elif (event.type, event.key)==(SDL_KEYDOWN,SDLK_a):
            self.pistolfire=1
            self.pistol()


        elif (event.type, event.key)==(SDL_KEYUP,SDLK_a):
            self.pistolfire=0



#dddddddddddddddddddddddddddddddddddddddd






