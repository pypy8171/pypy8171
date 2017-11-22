import game_framework
import cProfile

from pico2d import *
import easy_stage
import normal_stage
import hard_stage
import start_state
import title_state
import boss_stage


open_canvas()
game_framework.run(start_state)
close_canvas()
