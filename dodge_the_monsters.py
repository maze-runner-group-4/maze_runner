import pygame
from main import MazeGame
from maze_maps import Maze_maps
BLACK = (0, 0, 0)
indigo = "indigo"
class Dodge_the_monsters(MazeGame):
    
    def __init__(self, width, height, maze):
        super().__init__(width, height, maze)
        self.monster1_pos=self.find_character(maze,"M")
        self.monster2_pos=self.find_character(maze,"S")
        self.monster3_pos=self.find_character(maze,"R")
        # print(self.monster3_pos[1])
        self.player_health=3
        self.monster1_vel = -1
        self.monster2_vel = -1

        self.monster3_vel = 1
        self.movement_range_M = 11
        self.movement_range_S = 11
        self.movement_range_R = 47
        # moving_the_monsters = self.monster_movement(self.movement_range_M,self.movement_range_S,self.movement_range_R)

    def monster_movement(self):
        # monster 1 movement
        self.monster1_pos[0] += self.monster1_vel
        if self.monster1_pos[0] <= 14:
            self.monster1_vel *= -1
        if self.monster1_pos[0] >= 25:
            self.monster1_vel *= -1
        print(self.monster1_pos[0])
            
        # monster 2 movement
        # self.monster2_pos[0] += self.monster2_vel
        # if self.monster2_pos[0] <= 14:
        #     self.monster2_vel *= -1
        # if self.monster2_pos[0] >= 25:
        #     self.monster2_vel *= -1
        # print(self.monster2_pos[0])
        
        # # monster 3 2-49 movement
        # self.monster3_pos[1] += self.monster3_vel
        # if self.monster3_pos[1] >= 49:
        #     self.monster3_vel *= -1
        # if self.monster3_pos[1] <= 2:
        #     self.monster3_vel *= -1
        # print(self.monster3_pos[1])



    def run(self, multi=False):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
            self.draw_player(self.player_pos[0],self.player_pos[1],1)
            if multi:
                self.draw_player(self.player_2_pos[0],self.player_2_pos[1],2)
            self.draw_goal()
            self.draw_treasure_maze()
            if self.check_find_goal():
                running = False
            pygame.display.flip()
            self.clock.tick(60)
            self.monster_movement()      
        pygame.quit()

if __name__ == "__main__":

    # Create an instance of the MazeGame class
    game = Dodge_the_monsters(1600, 900, Maze_maps.maze_multi)

    # Run the game
    game.run(True)    