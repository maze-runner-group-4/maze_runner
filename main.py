import pygame
import os
from maze_maps import Maze_maps
# from blue_player import *
# from coins_sheet import *
from spritesheet_test import *
# from yellow_monester import *
# from GUI import mainloop
BLACK = (0, 0, 0)
WHITE = "white"


class MazeGame:
    def __init__(self,maze):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.window_width = 1820
        self.window_height = 945
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Maze Game")
        self.WINNER_FONT = pygame.font.SysFont('comicsans', 100)
        self.treasure_counter = 0
        self.clock = pygame.time.Clock()
        self.player_pos = self.find_character(maze,"P")
        self.player_2_pos = self.find_character(maze,"L")
        self.goal = self.find_character(maze,"G")
        self.treasure = self.find_treasure(maze)
        self.maze = [[cell for cell in row] for row in maze]
        self.cell_width = 35
        self.cell_height = 35
        self.new_col = 0
        self.new_row = 0
        self.list_player_blue = animation_list_down_blue_player
        self.list_player_2_red = list_of_frames_red_player_front
        self.delay=pygame.time.get_ticks()
        self.cooldown = 200
        self.frame= 0
        self.delay_coin=pygame.time.get_ticks()
        self.cooldown_coin = 200
        self.frame_coin= 0
        self.game_over_sound = pygame.mixer.Sound(os.path.join("Assets","GameOver.wav"))
        self.game_win_sound =  pygame.mixer.Sound(os.path.join("Assets","WIN sound effect no copyright.wav"))
        pygame.mixer.music.load('Assets/background_mp3cut.net.wav') 
        self.offsett = 0
        self.scroll_area = 210
        pygame.mixer.music.play(-1)
        
    # def get_cell_width(self):
    #     return self.cell_width
    # def get_cell_height(self):
    #     return self.cell_height
    def find_character(self, maze,Char):
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if maze[row][col] == Char:
                    return [row, col]  
        return None  
    
    def find_treasure(self, maze):
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if maze[row][col] == "T":
                    self.treasure_counter+=1



    def draw_treasure_maze(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                if self.maze[row][col] == "T":
                        # current_time = pygame.time.get_ticks()
                        # if current_time - self.delay_coin >= self.cooldown_coin:
                            self.frame_coin += 0.15
                            # self.delay_coin = current_time
                            if self.frame_coin >= len(animation_list_coins):
                                self.frame_coin = 0
                            # if self.frame_coin%1==0:
                            self.window.blit(animation_list_coins[int(self.frame_coin)], ((col*35)+self.window_width//2-(self.cell_width*len(self.maze[0])//2), (row*35)+self.offsett))                    # treasure_cell_image = pygame.image.load(os.path.join("Assets","IMG_9986.png"))
                    # treasure_image = pygame.transform.scale(treasure_cell_image,(self.cell_width,self.cell_height))
                    # self.window.blit(treasure_image,(col* self.cell_width,row* self.cell_height))
                if self.maze[row][col] == "X":
                    wall_cell_image = pygame.image.load(os.path.join("Assets","wall_cell.png"))
                    wall_cell = pygame.transform.scale(wall_cell_image,(self.cell_width,self.cell_height))
                    self.window.blit(wall_cell,((col * self.cell_width)+self.window_width//2-(self.cell_width*len(self.maze[0])//2), row * self.cell_height+self.offsett))    



    def draw_player(self, pos_x, pos_y, player,list_player):
        current_time = pygame.time.get_ticks()
        if current_time - self.delay >= self.cooldown:
            self.frame += 1
            self.delay = current_time
            if self.frame >= len(list_player):
                self.frame = 0
        if player == 1:
            self.window.blit(list_player[self.frame], ((pos_x*35)+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett))
        else:
            self.window.blit(list_player[self.frame], ((pos_x*35)+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett))
    
    # def draw_player(self,pos_x,pos_y,player):
    #     if player == 1:
	

    #         player_cell_image = pygame.image.load(os.path.join("Assets","IMG_0011.png"))

    #     else:
            
    #         player_cell_image = pygame.image.load(os.path.join("Assets","image.png"))
    #     player_cell = pygame.transform.scale(player_cell_image,(self.cell_width,self.cell_height))
    #     self.window.blit(player_cell,(pos_y * self.cell_width, pos_x * self.cell_height))

    

    def draw_goal(self):

        goal_cell_image = pygame.image.load(os.path.join("Assets","IMG_9998.png"))
        goal_cell = pygame.transform.scale(goal_cell_image,(self.cell_width,self.cell_height))
        self.window.blit(goal_cell,((self.goal[1] * self.cell_width)+self.window_width//2-(self.cell_width*len(self.maze[0])//2), self.goal[0] * self.cell_height+self.offsett))

    def check_find_goal(self):
        if self.player_pos[0] == self.goal[0] and self.player_pos[1]==self.goal[1]:
            winner_text = "Congratulations! Blue Win!"
            pygame.mixer.music.stop()
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            return True
        elif self.player_2_pos[0] == self.goal[0] and self.player_2_pos[1]==self.goal[1]:
            winner_text = "Congratulations! Red Win!"
            pygame.mixer.music.stop()
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            return True
        return False
    
    def draw_winner(self,text):
        draw_text = self.WINNER_FONT.render(text, 1, WHITE)
        self.window.blit(draw_text, (self.window_width/2 - draw_text.get_width() /
                         2,self.window_height/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(2000)

    
    def change_frame(self,list,player):
        if player == 1:
            self.list_player_blue=list
        if player==2:
            self.list_player_2_red = list

        

    def move_player(self, direction,player):
        if player == 2:
         self.new_row = self.player_pos[0]
         self.new_col = self.player_pos[1]
        elif player == 1:
           self. new_row = self.player_2_pos[0]
           self. new_col = self.player_2_pos[1]
        if direction == "up":
            self.new_row -= 1
            self.change_frame(list_of_frames_red_player_back,2)
        elif direction == "down":
           self. new_row += 1
           self.change_frame(list_of_frames_red_player_front,2)
        elif direction == "left":
          self.  new_col -= 1
          self.change_frame(list_of_frams_red_player_left,2)
        elif direction == "right":
          self.  new_col += 1
          self.change_frame(list_of_frames_red_player_right,2)

        if direction == "w":
            self. new_row -= 1
            self.change_frame(animation_list_up_blue_player,1)
        elif direction == "s":
          self.  new_row += 1
          self.change_frame(animation_list_down_blue_player,1)
          
        elif direction == "a":
          self.  new_col -= 1
          self.change_frame(animation_list_left_blue_player,1)
        elif direction == "d":
          self.  new_col += 1
          self.change_frame(animation_list_right_blue_player,1)
        if self.is_valid_move(self.new_row,self. new_col):
            if player == 2:
                # print(self.player_pos)
                self.player_pos = (self.new_row, self.new_col)
                if self.player_pos[0]*35 + self.offsett >= self.window_height-self.scroll_area and direction =="s" and self.player_pos[0]*35 - self.offsett < len(self.maze)*35 and len(self.maze)*35 > self.window_height :
                    self.offsett -= 140
                if (len(self.maze)-self.player_pos[0])*35 - self.offsett >= self.window_height+self.scroll_area and direction =="w" and self.player_pos[0]>4:
                    self.offsett += 140
                    
            if player == 1:
                self.player_2_pos = (self.new_row, self.new_col)
                if self.player_2_pos[0]*35 + self.offsett >= self.window_height-self.scroll_area and direction =="down" and self.player_2_pos[0]*35 - self.offsett < len(self.maze)*35 and len(self.maze)*35 > self.window_height :
                    self.offsett -= 140
                if (len(self.maze)-self.player_2_pos[0])*35 - self.offsett >= self.window_height+self.scroll_area and direction =="up" and self.player_2_pos[0]>4:
                    self.offsett += 140

    def is_valid_move(self, row, col):
        if row < 0 or row >= len(self.maze) or col < 0 or col >= len(self.maze[0]):
            return False
        if self.maze[row][col] == "X":
            return False
        return True
    
    def run(self,multi=False):
        running = True
        while running:

            self.window.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
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
            self.draw_player(self.player_pos[1],self.player_pos[0],1,self.list_player_blue)
            if multi:
                self.draw_player(self.player_2_pos[1],self.player_2_pos[0],2,self.list_player_2_red)
            self.draw_goal()
            self.draw_treasure_maze()
            if self.check_find_goal():
                pygame.mixer.music.stop()
                running = False
                # mainloop()
            pygame.display.flip()
            self.clock.tick(60)
        # pygame.quit()


if __name__ == "__main__":

    # Create an instance of the MazeGame class
    game = MazeGame(Maze_maps.maze_hard)

    # Run the game
    game.run(True)
