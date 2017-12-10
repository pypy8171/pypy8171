# json_players.py : load player data from .json file

import random
import json
from pico2d import *

running = None

class Easy_Monster:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    die_sound=None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 100
        self.frame = random.randint(0, 1)
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.total_frame = 0
        self.dir = 0
        self.up=0;
        self.run_frames = 0
        self.stand_frames = 0
        self.distance=0
        self.height=0;
        self.state = self.RIGHT_RUN
        self.name = 'noname'
        if Easy_Monster.image == None:
            Easy_Monster.image = load_image('monster.png')
        if Easy_Monster.die_sound==None:
            Easy_Monster.die_sound=load_wav('monsterdie.wav')
            Easy_Monster.die_sound.set_volume(64)

    def die(self):
        self.die_sound.play()
    def set_easybg(self, bg):
        self.bg = bg
    def set_normalbg(self, bg):
        self.bg = bg
    def set_hardbg(self, bg):
        self.bg = bg
    def handle_left_run(self):
        self.dir = -1
        self.state=self.LEFT_RUN
        if self.distance%30>29:
            self.dir=1
            self.state=self.RIGHT_RUN



    def handle_right_run(self):
        self.dir = 1
        self.state = self.RIGHT_RUN
        if self.distance%30>29:
            self.dir = -1
            self.state = self.LEFT_RUN

    handle_state = {
                LEFT_RUN: handle_left_run,
                RIGHT_RUN: handle_right_run
    }

    def update(self,frame_time):
        self.life_time += frame_time
        distance = Easy_Monster.RUN_SPEED_PPS * frame_time
        self.total_frames += Easy_Monster.FRAMES_PER_ACTION * Easy_Monster.ACTION_PER_TIME * frame_time
        self.total_frame += Easy_Monster.FRAMES_PER_ACTION * Easy_Monster.ACTION_PER_TIME * frame_time
        self.x += (self.dir * distance)
        self.y +=(self.up *self.height)
        self.height = self.y
        self.distance = self.x
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(0,self.state*40,40,40,self.x - self.bg.window_left, self.y - self.bg.window_bottom)

    def get_bb(self):
        return self.x-10-self.bg.window_left,self.y-10-self.bg.window_bottom,self.x+10-self.bg.window_left,self.y+10-self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



# team FACTORY
#"Asura2" :{"StartState":"RIGHT_RUN","x":random.randint(0,600),"y":random.randint(0,400)}
