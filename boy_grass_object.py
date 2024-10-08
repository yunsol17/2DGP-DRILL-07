from pico2d import *
import random

from pygame.examples.cursors import image


# Game object class here
class Grass:
    def __init__(self):
        #모양없는 납작한 붕어빵의 초기 상태를 설정
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)
class Boy:
    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame=0
        self.image=load_image('run_animation.png')
    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')
    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        if self.y>30:
            self.y -=  random.randint(0, 5)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')
    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        if self.y>30:
            self.y -=  random.randint(0, 5)
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
def reset_world():
    global running
    global grass
    global team
    global balls
    global bigballs

    running = True
    grass = Grass() #잔디를 찍어낸다,생성한다.
    team=[Boy()for i in range(11)]
    balls=[Ball()for i in range(10)]
    bigballs = [BigBall() for i in range(10)]
running = True

def update_world():
    grass.update()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    for bigball in bigballs:
        bigball.update()
    pass
def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    for bigball in bigballs:
        bigball.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()
# game main loop code
running=True
while running:
    #game logic
    handle_events()
    update_world() #상호작용을 시뮬레이션
    render_world() #그 결과 보여준다
    delay(0.05)
# finalization code

close_canvas()
