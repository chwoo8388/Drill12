from pico2d import *
from sdl2 import SDLK_SPACE
from ball import Ball
from boy import Boy
from grass import Grass
from grass1 import Grass1

# 3분 5초 최종 커밋
def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if (event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and
                    boy.state in ('IDLE', 'RUN')):
                world.append(Ball(boy.x, boy.y - 40, boy.face_dir))
            boy.handle_event(event)


def reset_world():
    global world
    global boy

    world = []

    grass1 = Grass1()
    world.append(grass1)

    boy = Boy()
    world.append(boy)
    
    grass = Grass()
    world.append(grass)




def update_world():
    for o in world[:]:
        o.update()
    world[:] = [o for o in world if not getattr(o, 'is_out', False)]


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


running = True


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
