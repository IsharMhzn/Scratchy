import pygame
import os
from objects import *

#initializing pygame essential modules
pygame.init()

#global variables
screensize = 1200, 720
color = (255,0,0) #default color is red (at the start of program)
draw = True
brush = Brush()

pixel = Grid(screensize, (4,4))

clock = pygame.time.Clock()
font = pygame.font.SysFont('times new roman', 15)
brushbutton = Button((130, 690), (20,20), image=pygame.transform.scale(pygame.image.load(os.path.join('icons', 'brush.png')), (20,20)))
pixelbutton = Button((130,660), (65,20), text=font.render('Pixel mode', False, (0,0,0))) 

#making main window
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Scratchy')
screen.fill(colors.get('white'))
colorpanel = ColorPanel((20,690))


#active mode is pencil mode
active = brush

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
                elif key == pygame.K_KP_PLUS:
                    active.increasesize()
                elif key == pygame.K_KP_MINUS:
                    active.decreasesize()
                
            except AttributeError:
                print('This is not allowed in current mode.')

    colorpanel.draw(screen)
    brushbutton.draw(screen)
    pixelbutton.draw(screen)
    pygame.draw.rect(screen, (255,255,255), (0,0, 130, 100))
    screen.blit(font.render('Current color: ', False, (0,0,0)), (5,5))
    pygame.draw.rect(screen, color, (20, 25, 40, 20))
    screen.blit(font.render(f'Current mode: {active}', False, (0,0,0)), (5,50))
    screen.blit(font.render(f'Size: {active.size}', False, (0,0,0)), (5,70))
    
    #if a mouse left click is pressed
    if pygame.mouse.get_pressed() == (1,0,0):
        pos = pygame.mouse.get_pos()
        if not (pos[1] > 595 and pos[0] < 200):
            if draw:
                active.draw(screen, color, pos)
            else:
                pygame.draw.circle(screen, colors.get('white'), pos, 30)
        else:
            if pos[0] > 120:
                if brushbutton.isclicked(pos):
                    active = brush
                if pixelbutton.isclicked(pos):
                    active = pixel
            else:
                color = colorpanel.changecolor(pos)

    #updating the main Surface
    pygame.display.flip()
    clock.tick(120)