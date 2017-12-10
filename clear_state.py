import easy_stage
import game_framework
import random
from pico2d import *


name = "TitleState"
image = None
finish_font=None

def enter():
    global image
    global finish_font
    #global subfont

    #open_canvas()
    image=load_image('title.png')

    finish_font = load_font('ENCR10B.TTF', 60)  # 폰트파일 / 싸이즈  font.draw(x,y,'your text',(r,g,b))



def exit():
    global image, finish_font
    del(image)
    del(finish_font)


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
    finish_font.draw(230, 330, 'GAME CLEAR' , (0, 0, 0))

    update_canvas()







def update(frame_time):
    pass

def pause():
    pass


def resume():
    pass


