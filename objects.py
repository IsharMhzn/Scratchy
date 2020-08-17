import pygame

colors = {
    'white' : (255,255,255),
    'black' : (0,0,0),
    'red'  : (255,0,0),
    'blue' : (0,0,255),
    'green': (0,255,0),
    'cyan': (0,255,255)
}

colorset = [(255,204,204), (255,153,153), (255,102,102), (255,51,51), (255,0,0), 
            (255,255,204), (255,255,153), (255,255,102), (255,255,51), (255,255,0), 
            (204,255,204), (153,255,153), (102,255,102), (51,255,51), (0,255,0), 
            (204,204,255), (153,153,255), (102,102,255), (51,51,255), (0,0,255), 
            (255,255,255), (192,192,192), (128,128,128), (64,64,64), (0,0,0), 
        ]

class Cell:
    color = 'white'
    def __init__(self, x, y, l=10, b=10):
        self.l = l
        self.b = b
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Cell of size {self.l} X {self.b} at ({self.x}, {self.y}). Color: {self.color}'
    
    def draw(self, surface, color):
        self.color = color
        pygame.draw.rect(surface, color, (self.x*self.l, self.y*self.b, self.l, self.b))


class Grid:
    grid = []
    def __init__(self, windowsize, cell_size=(10,10)):
        self.cell_size = cell_size  
        self.grid = [[Cell(i,j, *cell_size) for j in range(windowsize[1]//cell_size[1])] for i in range(windowsize[0]//cell_size[0])]
    
    def __str__(self):
        return f'{len(self.grid)}'
    
    def draw(self,screen, color, pos):
        cell = pos[0]//self.cell_size[0], pos[1]//self.cell_size[1] 
        self.grid[cell[0]][cell[1]].draw(screen, color)

class Pencil:
    color = 'white'
    def __init__(self, x=0, y=0, size=2):
        self.pos = x, y
        self.size = size
    
    def set_pos(self, x, y):
        self.pos = x, y
    
    def get_pos(self):
        return self.pos
    
    def increasesize(self):
        if self.size < 15:
            self.size += 1
    
    def decreasesize(self):
        if self.size > 2:
            self.size -= 1

    def draw(self, surface, color, pos):
        self.set_pos(*pos)
        pygame.draw.circle(surface, color, self.pos, self.size)

class Button:
    def __init__(self, pos, size, color=(195,195,195), image=None, text=None):
        self.pos = pos
        self.size = size
        self.color = color
        self.image = image  
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (*self.pos, *self.size))
        if self.image:
            surface.blit(self.image, self.pos)
        if self.text:
            surface.blit(self.text, self.pos)
    
    def isclicked(self, pos):
        if abs(pos[0] - self.pos[0]) <= self.size[0]  and abs(pos[1] - self.pos[1]) <= self.size[1] and pos[1] > self.pos[1] and pos[0] > self.pos[0]:
            return True
        return False


class Color(Button):
    def __init__(self, pos, color):
        super().__init__(pos, (20, 20),color)
        

class ColorPanel:
    group = []
    def __init__(self, pos):
        self.pos = pos
        count = 0
        for color in colorset:
            if count % 5 == 0 and count > 0:
                pos = self.pos[0]*0+10, pos[1] - 22
                count = 0
            else:
                pos = self.pos[0]*count+10, pos[1]
            count += 1
            self.group.append(Color(pos, color))

    
    def draw(self, surface):
        pygame.draw.rect(surface, (195,195,195), (self.pos[0]-25, self.pos[1]-95, 126, 120))
        for c in self.group:
            c.draw(surface)
    
    def changecolor(self, pos):
        for c in self.group[::-1]:
            if abs(pos[0] - c.pos[0]) <= 20  and abs(pos[1] - c.pos[1]) <= 20 and pos[1] > c.pos[1] and pos[0] > c.pos[0]:
                print(pos, c.pos, c.color)
                print(f'Color changed to {c.color}')
                return c.color
        return (0,0,0)
