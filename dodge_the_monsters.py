import pygame
from main import MazeGame
from maze_maps import Maze_maps

class Dodge_the_monsters(MazeGame):
    
    def __init__(self, width, height, maze):
        super().__init__(width, height, maze)
        self.monster1_pos=self.find_character(maze,"M")
        self.monster2_pos=self.find_character(maze,"S")
        self.monster3_pos=self.find_character(maze,"R")
        self.player_health=3



    def run(self, multi=False):
        super().run(multi)
        pass       

if __name__ == "__main__":

    # Create an instance of the MazeGame class
    game = Dodge_the_monsters(1600, 900, Maze_maps.maze_treasure)

    # Run the game
    game.run()    