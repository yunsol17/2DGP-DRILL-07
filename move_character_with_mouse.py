from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

global hx, hy
hx = random.randint(1, TUK_WIDTH)
hy = random.randint(1, TUK_HEIGHT)
def change_hand_a():
    global hx, hy
    hx = random.randint(1, TUK_WIDTH)
    hy = random.randint(1, TUK_HEIGHT)

def move_ch(x,y,hx,hy,t):
    x=(1-t)*x+t*hx
    y = (1 - t) * y + t * hy
    return x,y

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
time=0
t=0.1
while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    time+=0.05
    if time>=2.0:
        change_hand_a()
        time=0
    hand_arrow.draw(hx,hy)
    x,y=move_ch(x,y,hx,hy,t)

    if hx>x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

close_canvas()




