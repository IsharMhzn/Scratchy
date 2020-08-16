import pygame
from objects import *

#initializing pygame essential modules
pygame.init()

#global variables
screensize = 1200, 720
cheat = ''
color = 'red' #default color is red (at the start of program)
draw = True
pencil = Pencil()

pixel = Grid(screensize, (4,4))
cheats = {
    'cr': 'red',
    'cb': 'blue',
    'cg': 'green',
    'cc': 'cyan',
    'ckb': 'black',
    'cw': 'white',
    'mpi': pixel,
    'mdp': pencil,
}

clock = pygame.time.Clock()

#making main window
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Scratchy')
screen.fill(colors.get('white'))
colorpanel = ColorPanel((20,690))


#active mode is pencil mode
active = pencil

def cheat_detector(c):
    #declared globally to change the value thoughout the program
    global cheat, color, active
    if c in cheats.keys():
        if cheat.startswith('c'):
            color = cheats.get(c)
            print(f'Changed the color to {cheats[c]}.')
        elif cheat.startswith('m'):
            active = cheats.get(c)
            print(f'Changed mode to {c}.')
        else:
            cheat = ''
        cheat = ''

while True:
    #all the events (i.e inputs: key or mouse) while running the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            key = event.key
            try:
                if key == pygame.K_SPACE:
                    draw = not draw
                elif key == pygame.K_ESCAPE:
                    cheat = ''
                    print('Cheat cleared.')
                elif key == pygame.K_KP_PLUS:
                    active.increasesize()
                elif key == pygame.K_KP_MINUS:
                    active.decreasesize()
                else:
                    cheat += chr(key)
            except AttributeError:
                print('This is not allowed in current mode.')
            print(f'Cheat: "{cheat}"')

    #reacts if a certain cheat is entered
    #cheatlist is declared globally to avoid memory redundancy
    cheat_detector(cheat)

    colorpanel.draw(screen)
    #if a mouse left click is pressed
    if pygame.mouse.get_pressed() == (1,0,0):
        pos = pygame.mouse.get_pos()
        if not (pos[1] > 595 and pos[0] < 120):
            if draw:
                active.draw(screen, color, pos)
            else:
                pygame.draw.circle(screen, colors.get('white'), pos, 30)

    #updating the main Surface
    pygame.display.flip()
    clock.tick(120)