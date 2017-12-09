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

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 100
        self.frame = random.randint(0, 1)
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.total_frame = 0
        self.dir = 0
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        self.name = 'noname'
        if Easy_Monster.image == None:
            Easy_Monster.image = load_image('monster.png')

    def set_easybg(self, bg):
        self.bg = bg

    def handle_left_run(self):
        self.dir = -1
        self.state=self.RIGHT_RUN
        if self.total_frames%50>45:
            self.dir=1
            self.state=self.LEFT_RUN


    def handle_right_run(self):
        self.dir = 1
        self.state = self.LEFT_RUN
        if self.total_frames % 100>95:
            self.dir = -1
            self.state = self.RIGHT_RUN


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
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(0,self.state*40,40,40,self.x - self.bg.window_left, self.y - self.bg.window_bottom)

    def get_bb(self):
        return self.x-20-self.bg.window_left,self.y-20-self.bg.window_bottom,self.x+20-self.bg.window_left,self.y+20-self.bg.window_bottom

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
def create_team():

    player_state_table = {
        "LEFT_RUN" : Easy_Monster.LEFT_RUN,
        "RIGHT_RUN" : Easy_Monster.RIGHT_RUN,
    }

    #team_data = json.loads(team_data_text)

    team_data_file = open('monster_data.txt','r')
    team_data = json.load(team_data_file)
    team_data_file.close()

    team = []
    for name in team_data:
        player = Easy_Monster()
        player.name = name
        player.x = team_data[name]['x']
        player.y = team_data[name]['y']
        player.state = player_state_table[team_data[name]['StartState']]
        team.append(player)

    return team
