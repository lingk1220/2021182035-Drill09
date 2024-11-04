#world = []
#world[0] : 백그라운드
#world[1] : 포어그라운드
world = [[], [], []]

def add_object(o, depth):
    world[depth].append(o)

def update_world():

    pass


def render():
    for layer in world:
        for o in layer:
            o.draw()


def update():
    for layer in world:
        for o in layer:
            o.update()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    print('error: object not exist')