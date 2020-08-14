import pygame

#initializing pygame essential modules
pygame.init()

#global variables
screensize = 720, 480
colors = {
    'white' : (255,255,255),
    'black' : (0,0,0),
    'red'  : (255,0,0),
    'blue' : (0,0,255),
    'green': (0,255,0)
}

clock = pygame.time.Clock()

#making main window
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Scratchy')
screen.fill(colors.get('white'))

draw = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                draw = not draw


    if pygame.mouse.get_pressed() == (1,0,0):
        pos = pygame.mouse.get_pos()
        if draw:
            pygame.draw.rect(screen, colors.get('red'), (pos[0], pos[1], 5, 5))
        else:
            pygame.draw.circle(screen, colors.get('white'), pos, 30)

    #updating the main Surface
    pygame.display.flip()
    clock.tick(120)