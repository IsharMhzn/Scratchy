import pygame

colors = {
    'white' : (255,255,255),
    'black' : (0,0,0),
    'red'  : (255,0,0),
    'blue' : (0,0,255),
    'green': (0,255,0),
    'cyan': (0,255,255)
}

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
        pygame.draw.rect(surface, colors[color], (self.x*self.l, self.y*self.b, self.l, self.b))


class Grid:
    grid = []
    def __init__(self, windowsize, cell_size=(10,10)):
        self.cell_size = cell_size  
        self.grid = [[Cell(i,j, *cell_size) for j in range(windowsize[1]//cell_size[1])] for i in range(windowsize[0]//cell_size[0])]
    
    def __str__(self):
        return f'{len(self.grid)}'
    
    def draw(self,screen, color, pos):
        cell = pos[0]//self.cell_size[0], pos[1]//self.cell_size[1] 
        print(cell)
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
        pygame.draw.circle(surface, colors.get(color), self.pos, self.size)  
