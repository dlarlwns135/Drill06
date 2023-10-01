from pico2d import *

import random
import math
#뭐임?
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while (running):
    mx = (random.randint(0, TUK_WIDTH))
    my = (random.randint(0, TUK_HEIGHT))
    sx, sy = x, y


    for i in range(0, 200 + 1, 1):
        t = (i / 200)
        x = (1 - t) * x + t * mx
        y = (1 - t) * y + t * my
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(mx, my)
        if sx >= mx:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        handle_events()
        if (not running):
            break
        dis = math.sqrt((mx - x) ** 2 + (my - y) ** 2)
        if dis < 1:
            break
        delay(0.01)

close_canvas()



