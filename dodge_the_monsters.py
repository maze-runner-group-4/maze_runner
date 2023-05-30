import os
import pygame
from main import MazeGame
from maze_maps import Maze_maps
BLACK = (0, 0, 0)
indigo = "indigo"
class Dodge_the_monsters(MazeGame):
    
    def __init__(self, width, height, maze):
        super().__init__(width, height, maze)
        
        self.game_over_FONT = pygame.font.SysFont('comicsans', 100)
        self.monster1_pos=self.find_character(maze,"M")
        self.monster2_pos=self.find_character(maze,"S")
        self.monster3_pos=self.find_character(maze,"R")
        self.heart_pos=self.find_character(maze,"H")
        # print(self.monster3_pos[1])
        self.player_health=3
        self.player_2_health = 3

        self.monster1_vel = -0.5
        self.monster2_vel = -0.5
        self.heart_x = 5 + (self.cell_width + 5)#for heart left player one 
        self.heart2_x = self.window_width-self.cell_width*4
        self.monster3_vel = 1
        self.movement_range_M = 11
        self.movement_range_S = 11
        self.movement_range_R = 47
        # moving_the_monsters = self.monster_movement(self.movement_range_M,self.movement_range_S,self.movement_range_R)

    def draw_hearts(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == "H":
                    treasure_cell_image = pygame.image.load(os.path.join("Assets","heart1.png"))
                    treasure_image = pygame.transform.scale(treasure_cell_image,(self.cell_width,self.cell_height))
                    self.window.blit(treasure_image,(col* self.cell_width,row* self.cell_height))

    def draw_hearts_points(self,player_health,heart_x): 
        for i in range(player_health):
            heart_y = 0
            heart_image = pygame.image.load(os.path.join("Assets", "333-removebg-preview.png"))
            heart_image = pygame.transform.scale(heart_image, (self.cell_width, self.cell_height))
            self.window.blit(heart_image, (heart_x+(i*self.cell_width), heart_y))
        pygame.display.update()

    def draw_monster(self, pos_x, pos_y, monster):
        if monster =="M":
            monster_cell_image = pygame.image.load(os.path.join("Assets","green-removebg-preview.png"))
        elif monster == "S":
            monster_cell_image = pygame.image.load(os.path.join("Assets","blue-removebg-preview.png"))
        elif monster == "R":
            monster_cell_image = pygame.image.load(os.path.join("Assets","yellow-removebg-preview.png"))
        else:
            monster_cell_image = pygame.image.load(os.path.join("Assets","wall_cell.png"))         
        monster_cell = pygame.transform.scale(monster_cell_image,(self.cell_width,self.cell_height))
        self.window.blit(monster_cell,(pos_y * self.cell_width, pos_x * self.cell_height))


    def monster_movement(self):
        # monster 1 movement
        self.monster1_pos[0] += self.monster1_vel
        if self.monster1_pos[0] <= 14:
            self.monster1_vel *= -1
        if self.monster1_pos[0] >= 25:
            self.monster1_vel *= -1
            
        # monster 2 movement
        self.monster2_pos[0] += self.monster2_vel
        if self.monster2_pos[0] <= 14:
            self.monster2_vel *= -1
        if self.monster2_pos[0] >= 25:
            self.monster2_vel *= -1
        
        # monster 3  movement
        self.monster3_pos[1] += self.monster3_vel
        if self.monster3_pos[1] >= 49:
            self.monster3_vel *= -1
        if self.monster3_pos[1] <= 2:
            self.monster3_vel *= -1

    def game_over(self):
        if self.player_health == 0 and self.player_2_health == 0:
            game_over_text = "Game Over"
            self.draw_game_over(game_over_text)
        elif self.player_health == 0:
            game_over_text = "Game Over - Blue lost!"
            self.draw_game_over(game_over_text)
        elif self.player_2_health == 0:
            game_over_text = "Game Over - Red lost!"
            self.draw_game_over(game_over_text)
 

    def draw_game_over(self,text):
        draw_text = self.game_over_FONT.render(text, 1, indigo)
        self.window.blit(draw_text, (self.window_width/2 - draw_text.get_width() /
                         2,self.window_height/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)


    def health_points_count(self):
        if (self.player_pos[0] == self.monster1_pos[0] and self.player_pos[1] == self.monster1_pos[1]) or \
        (self.player_pos[0] == self.monster2_pos[0] and self.player_pos[1] == self.monster2_pos[1]) or \
        (self.player_pos[0] == self.monster3_pos[0] and self.player_pos[1] == self.monster3_pos[1]):
            self.player_health -= 1
        elif (self.player_2_pos[0] == self.monster1_pos[0] and self.player_2_pos[1] == self.monster1_pos[1]) or \
            (self.player_2_pos[0] == self.monster2_pos[0] and self.player_2_pos[1] == self.monster2_pos[1]) or \
            (self.player_2_pos[0] == self.monster3_pos[0] and self.player_2_pos[1] == self.monster3_pos[1]):
            self.player_2_health -= 1 
        elif self.player_pos[0] == self.heart_pos[0] and self.player_pos[1] == self.heart_pos[1]:
            self.player_health += 1
        elif self.player_2_pos[0] == self.heart_pos[0] and self.player_2_pos[1] == self.heart_pos[1]:
            self.player_2_health += 1





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
            self.draw_monster(self.monster1_pos[0],self.monster1_pos[1],"M")
            self.draw_monster(self.monster2_pos[0],self.monster2_pos[1],"S")
            self.draw_monster(self.monster3_pos[0],self.monster3_pos[1],"R")
            self.draw_hearts()
            self.draw_hearts_points(self.player_health,self.heart_x)
            self.draw_hearts_points(self.player_health,self.heart2_x)
            self.health_points_count()
            self.game_over()
            if self.check_find_goal():
                running = False
            pygame.display.flip()
            self.clock.tick(60)
            self.monster_movement()      
        pygame.quit()

if __name__ == "__main__":

    # Create an instance of the MazeGame class
    game = Dodge_the_monsters(1200, 600, Maze_maps.maze_multi)

    # Run the game
    game.run(True)