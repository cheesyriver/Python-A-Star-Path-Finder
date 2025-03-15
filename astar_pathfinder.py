import pygame
import math
from queue import PriorityQueue

WIN_WIDTH = 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))
pygame.display.set_caption("A* Visual Path Finder")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neightbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_wall(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == CYAN
    
    def reset(self):
        self.color = WHITE

    def set_closed(self):
        self.color = RED
    
    def set_open(self):
        self.color = GREEN
    
    def set_wall(self):
        self.color = BLACK
    
    def set_start(self):
        self.color = ORANGE
    
    def set_end(self):
        self.color = CYAN
    
    def set_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def udpate_neighbours():
        pass
    
    def __lt__(self, other):
        return False