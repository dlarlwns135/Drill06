from pico2d import *
import random
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global click_positions
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click_positions.append((event.x, TUK_HEIGHT - 1 - event.y))

running = True
frame = 0
mx, my = 0, 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()
click_positions = []  # 클릭한 위치 저장 리스트
current_target = None
see_right = True

while running:
    handle_events()
    if not running:
        break
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if see_right:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    hand.draw(mx, my)
    for pos in click_positions:
        hand.draw(pos[0], pos[1])
    update_canvas()
    frame = (frame + 1) % 8
    if click_positions:
        for pos in click_positions:
            hand.draw(pos[0],pos[1])
        if current_target is None:
            current_target = click_positions[0]
            dx, dy = current_target
            sx, sy = x, y

            for i in range(0, 300 + 1, 1):
                t = (i / 300)
                x = (1 - t) * x + t * dx
                y = (1 - t) * y + t * dy
                clear_canvas()
                TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
                if sx >= dx:
                    character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
                    see_right = False
                else:
                    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
                    see_right = True
                handle_events()
                if not running:
                    break
                hand.draw(mx, my)
                for pos in click_positions:
                    hand.draw(pos[0], pos[1])
                frame = (frame + 1) % 8
                dis = math.sqrt((dx - x) ** 2 + (dy - y) ** 2)
                if dis < 1:
                    current_target = None
                    click_positions.pop(0)
                    break
                update_canvas()

                delay(0.01)

    delay(0.01)

close_canvas()
