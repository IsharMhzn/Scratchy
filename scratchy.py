import pygame
from objects import *

#initializing pygame essential modules
pygame.init()

#global variables
screensize = 800, 600
colors = {
    'white' : (255,255,255),
    'black' : (0,0,0),
    'red'  : (255,0,0),
    'blue' : (0,0,255),
    'green': (0,255,0),
    'cyan': (0,255,255)
}

clock = pygame.time.Clock()

#making main window
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Scratchy')
screen.fill(colors.get('white'))

draw = True
cheats = {
    'cr': 'red',
    'cb': 'blue',
    'cg': 'green',
    'cc': 'cyan',
    'ckb': 'black',
    'cw': 'white'
}
cheat = ''
color = 'red'

g = Grid(screensize, (5,5))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_SPACE:
                draw = not draw
            elif key == pygame.K_ESCAPE:
                cheat = ''
                print('Cheat cleared.')
            else:
                cheat += chr(key)
            print(f'Cheat: "{cheat}"')

    if cheat in cheats.keys():
        color = cheats[cheat]
        print(f'Changed the color to {cheats[cheat]}.')
        cheat = ''


    if pygame.mouse.get_pressed() == (1,0,0):
        pos = pygame.mouse.get_pos()
        if draw:
            g.draw(screen, color, pos)
        else:
            pygame.draw.circle(screen, colors.get('white'), pos, 30)

    #updating the main Surface
    pygame.display.flip()
    clock.tick(120)