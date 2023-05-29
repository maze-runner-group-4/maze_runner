import pygame
from main import MazeGame

class Dodge_the_monsters(MazeGame):
    
    def __init__(self, width, height, maze):
        super().__init__(width, height, maze)
        self.monster1_pos=self.find_character(maze,"M")
        self.monster2_pos=self.find_character(maze,"S")
        self.monster3_pos=self.find_character(maze,"R")
        self.player_health=3
