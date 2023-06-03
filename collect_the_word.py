from main import MazeGame
from queue_word import Queue
import pygame
import pygame.mixer
from maze_maps import Maze_maps
import os
BLACK = (0, 0, 0)
indigo = "indigo"

class Collect_the_word(MazeGame):
    def __init__(self, maze):
        super().__init__( maze)

    def draw_the_letter(self):
        pass
    
    def move_player(self, direction, player): 
        super().move_player(direction, player)

    def showing_score(self):
        pass


    def check_find_goal(self):
        pass  


    def run(self):
        self.running = True
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move_player("up",1)
                    elif event.key == pygame.K_DOWN:
                        self.move_player("down",1)
                    elif event.key == pygame.K_LEFT:
                        self.move_player("left",1)
                    elif event.key == pygame.K_RIGHT:
                        self.move_player("right",1)
                    if event.key == pygame.K_w:
                        self.move_player("w",2)
                    elif event.key == pygame.K_s:
                        self.move_player("s",2)
                    elif event.key == pygame.K_a:
                        self.move_player("a",2)
                    elif event.key == pygame.K_d:
                        self.move_player("d",2)
            self.window.fill(BLACK)
            self.draw_treasure_maze()
            self.draw_player(self.player_pos[1],self.player_pos[0],1,self.list_player_blue)
            if self.multi:
                self.draw_player(self.player_2_pos[1],self.player_2_pos[0],2,self.list_player_2_red)
            if self.goal_draw:    
                self.draw_goal()
                if self.check_find_goal():
                    pygame.mixer.music.stop()
                    self.running = False
            self.draw_score(10,10,1)
            if self.multi:
                self.draw_score(self.window_width-220,10,2)
            pygame.display.flip()
            self.clock.tick(60)
        # pygame.quit()

if __name__ == "__main__":
    game = Collect_the_word( Maze_maps.maze_treasure)

    game.run()
    