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

while running:
    handle_events()
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    hand.draw(mx, my)
    update_canvas()

    frame = (frame + 1) % 8
    if not running:
        break
    delay(0.01)

close_canvas()

# def handle_events():
#     global running
#     global click_positions, mx, my
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_MOUSEMOTION:
#             mx, my = event.x, TUK_HEIGHT - 1 - event.y
#         elif event.type == SDL_MOUSEBUTTONDOWN:
#             if event.button == SDL_BUTTON_LEFT:
#                 click_positions.append((event.x, TUK_HEIGHT - 1 - event.y))
#
#
# running = True
# frame = 0
# x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
# mx, my, sx, sy = 0, 0, 0, 0
#
# click_positions = []  # 클릭한 위치 저장 리스트
# current_target = None
#
# while running:
#     handle_events()
#
#     if current_target is None:
#         if click_positions:
#             current_target = click_positions[0]  # 리스트에서 현재 목표 좌표를 가져옴
#             mx, my = current_target
#             sx, sy = x, y
#
#     for i in range(0, 200 + 1, 1):
#         t = (i / 200)
#         x = (1 - t) * sx + t * mx
#         y = (1 - t) * sy + t * my
#         clear_canvas()
#         TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
#
#         # 클릭한 모든 위치에 화살표 이미지를 그립니다.
#         for pos in click_positions:
#             hand.draw(pos[0], pos[1])
#
#         # 현재 목표 위치에 화살표 이미지를 그립니다.
#         if current_target:
#             hand.draw(mx, my)
#
#         if sx >= mx:
#             character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
#         else:
#             character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
#         update_canvas()
#         frame = (frame + 1) % 8
#
#         dis = math.sqrt((mx - x) ** 2 + (my - y) ** 2)
#         if dis < 1:
#             if current_target:
#                 x, y = mx, my  # 목표 위치에 도달하면 캐릭터 위치를 목표 위치로 설정
#                 current_target = None  # 현재 목표 위치를 비움
#                 if click_positions:
#                     click_positions.pop(0)  # 도착한 좌표를 리스트에서 삭제
#
#     if not running:
#         break
#     delay(0.01)
#
# close_canvas()
