import pgzrun

WIDTH = 800
HEIGHT = 600

# add this and get warning disappear
screen: 'pgzrun.Screen'


def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    screen.draw.circle((400, 300), 30, 'white')


pgzrun.go()

