import easy_stage
import game_framework
import random
from pico2d import *


name = "TitleState"
image = None
title_font = None
sub_font=None

def enter():
    global image
    global title_font
    global sub_font

    #open_canvas()
    image=load_image('title.png')

    title_font = load_font('ENCR10B.TTF', 60)  # 폰트파일 / 싸이즈  font.draw(x,y,'your text',(r,g,b))
    sub_font = load_font('ENCR10B.TTF', 50)  # 폰트파일 / 싸이즈  font.draw(x,y,'your text',(r,g,b))




def exit():
    global image, title_font,sub_font
    del(image)
    del(title_font)
    del(sub_font)
   # close_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key)==(SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(easy_stage)
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()





def draw(frame_time):
    clear_canvas()
    image.draw(400,300)
    title_font.draw(220, 500, 'Cat Mario' , (250, 150, 50))
    sub_font.draw(220, 280, 'Press Space', (0, 0, 0))
    image.opacify(random.random())
    update_canvas()







def update(frame_time):
    pass

def pause():
    pass


def resume():
    pass






