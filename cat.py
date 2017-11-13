import random

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

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND,JUMP = 0, 1, 2, 3,4

    def __init__(self):
        self.x, self.y = 0, 120
        self.frame = random.randint(0, 3)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.up = 0
        self.state = self.RIGHT_STAND
        if Cat.image == None:
            Cat.image = load_image('run_animation.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        def clamp(minimum,y,maximum):
            return max(minimum,min(y,maximum))

        self.life_time += frame_time
        distance = Cat.RUN_SPEED_PPS * frame_time
        self.total_frames += Cat.FRAMES_PER_ACTION * Cat.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3
        self.x += (self.dir * distance)
        self.y +=(self.up*distance)

        self.x = clamp(0, self.x, 800)
        self.y = clamp(120,self.y,300)

        if self.up ==2:
            if self.y>299:
                self.up =-2
                if self.y<121:
                    self.up = 0

        if self.x>700:
            self.y =-100


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 40, self.y - 30, self.x+40, self.y+40
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
                self.state = self.JUMP
                self.up = 2






