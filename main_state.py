from pico2d import *
import game_framework


name = "MainState"


right_pressed = None
left_pressed = None
up_pressed = None

class Cat:
    image = None

    RIGHT_STAND, RIGHT_RUN,LEFT_RUN, UP_RUN = 0,1,2,3

    def handle_right_stand(self):
        self.stand_frames +=1
        if right_pressed:
            self.state = self.RIGHT_RUN
            self.run_frames=0
        elif left_pressed:
            self.state = self.LEFT_RUN
            self.run_frames=0
        elif up_pressed:
            self.state = self.UP_RUN
            self.run_frames=0

    def handle_right_run(self):
        self.x +=10
        self.run_frames+=1
        if right_pressed == False:
            self.state = self.RIGHT_STAND
        elif left_pressed:
            self.state = self.LEFT_RUN
        elif up_pressed:
            self.state = self.UP_RUN


    def handle_left_run(self):
        self.x-=10
        self.run_frames-=1
        if left_pressed == False:
            self.state = self.RIGHT_STAND
        elif right_pressed:
            self.state=self.RIGHT_RUN
        elif up_pressed:
            self.state = self.UP_RUN

    def handle_up_run(self):
        if self.y<200:
            self.y+=80
        elif self.y==200:
            self.y-=80
        self.run_frames+=1
        if up_pressed == False:
            self.state = self.RIGHT_STAND
        elif right_pressed:
            self.x+=10
            self.state=self.RIGHT_RUN
        elif left_pressed:
            self.x-=10
            self.state = self.LEFT_RUN


    handle_state={RIGHT_STAND: handle_right_stand,
                  RIGHT_RUN: handle_right_run,
                  LEFT_RUN: handle_left_run,
                  UP_RUN: handle_up_run
                  }
    def update(self):
        self.frame = (self.frame+1)%3
        self.handle_state[self.state](self)

    def __init__(self):
        self.x, self.y = 0 ,120
        self.frame = 0
        self.run_frames = 0
        self.stand_frames = 0
        self.state = self.RIGHT_STAND
        if Cat.image ==None:
            Cat.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame*100,self.state%3+100,100,100,self.x, self.y)

class Title:
    def __init__(self):
        self.image = load_image('title.png')

    def draw(self):
        self.image.draw(400,300)




def handle_events():
    global running
    global right_pressed
    global left_pressed
    global up_pressed
    global a
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False
        elif (event.type, event.key) ==(SDL_KEYDOWN , SDLK_RIGHT):
            right_pressed = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            right_pressed = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            left_pressed = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            left_pressed = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            up_pressed = True
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            up_pressed = False
        pass




open_canvas()

cat=Cat()
title = Title()

running = True;


while (running):
    handle_events()

    cat.update()

    clear_canvas()
    title.draw()
    cat.draw()
    update_canvas()

    delay(0.02)

close_canvas()

