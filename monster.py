# json_players.py : load player data from .json file

import random
import json
from pico2d import *

running = None

class Title:
    def __init__(self):
        self.image = load_image('easy_mode.png')
        self.x = 0
        self.y = 300
    def update(self):
        pass

    def draw(self):
        self.image.draw(1550+self.x, self.y)


class Monster:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def handle_left_run(self)   :
        self.x -= 5
        self.run_frames += 1
        if self.x < 1500:
            self.state = self.RIGHT_RUN
            self.x = 1500
        if self.run_frames == 10:
            self.state = self.LEFT_STAND
            self.stand_frames = 0

    def handle_left_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 5:
            self.state = self.LEFT_RUN
            self.run_frames = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 700:
            self.state = self.LEFT_RUN
            self.x = 700
        if self.run_frames == 10:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 5:
            self.state = self.RIGHT_RUN
            self.run_frames = 0


    handle_state = {
                LEFT_RUN: handle_left_run,
                RIGHT_RUN: handle_right_run,
                LEFT_STAND: handle_left_stand,
                RIGHT_STAND: handle_right_stand
    }

    def update(self):
        self.frame = (self.frame+1)%3
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = random.randint(700,1500), 90
        self.frame = random.randint(0, 3)
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_RUN
        self.name = 'noname'
        if Monster.image == None:
            Monster.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        #self.image.draw(self.x,self.y)

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
        "LEFT_RUN" : Monster.LEFT_RUN,
        "RIGHT_RUN" : Monster.RIGHT_RUN,
        "LEFT_STAND" : Monster.LEFT_STAND,
        "RIGHT_STAND" : Monster.RIGHT_STAND
    }

    #team_data = json.loads(team_data_text)

    monster_data_file = open('monster_data.txt','r')
    monster_data = json.load(monster_data_file)
    monster_data_file.close()

    monster = []
    for name in monster_data:
        monsters = Monster()
        monsters.name = name
        monsters.x = monster_data[name]['x']
        monsters.y = monster_data[name]['y']
        monsters.state = player_state_table[monster_data[name]['StartState']]
        monster.append(monsters)

    return monster

def enter():
    global title, monster
    monster = Monster()
    title = Title()

    pass


def exit():
    global title, monster
    del(monster)
    del(title)
    pass


def main():

    open_canvas()

    global moster
    global running

    monster = create_team()

    title = Title()
    running = True
    while running:
        handle_events()

        for monsters in monster:
            monsters.update()

        clear_canvas()
        title.draw()
        for monsters in monster:
            monsters.draw()
        update_canvas()

        delay(0.04)

    close_canvas()

if __name__ == '__main__':
    main()