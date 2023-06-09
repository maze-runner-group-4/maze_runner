import pygame
import os
import pygame.freetype

from spritesheet_test import *

BLACK = (0, 0, 0)
WHITE = "white"


class MazeGame:
    def __init__(self,maze,mode):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.freetype.init()
        self.mode=mode
        self.window_width = 1820
        self.window_height = 945
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        #
        self.info_button_img = pygame.image.load(os.path.join('Assets', 'infobackground.png'))
        self.ok_button_img = pygame.image.load(os.path.join('Assets', 'okbutton.png'))
        self.button_text_color = (255, 255, 255)
        self.font_path = "Fonts/font.ttf"
        self.font_size = 14
        self.font = pygame.freetype.Font(self.font_path, self.font_size)
        self.info_button_x=(self.window_width//2)
        self.info_button_y=(self.window_height//2)

        self.info_button_width=950
        self.info_button_height = 600

        self.info_button_img1 = pygame.transform.scale(self.info_button_img, (self.info_button_width, self.info_button_height))
        self.info_button_img_rect = pygame.Rect(self.info_button_x, self.info_button_y, self.info_button_width, self.info_button_height)
        #for Ok button
        self.ok_button_width=150
        self.ok_button_height = 150
        self.ok_button_x=(self.window_width//2) 
        self.ok_button_y=(self.window_height//2)+100
        self.ok_button = pygame.transform.scale(self.ok_button_img, (self.ok_button_width, self.ok_button_height))

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
        self.start_time = 0
        self.str_start_time = " "

        
        self.paragraph_text = """
 Welcome to the exhilarating Escape The Maze mode\n\n
 in single-player! Prepare yourself for an incredible\n\n
 adventure filled with excitement as you navigate\n\n
 through the labyrinthine pathways.\n\n
 Get ready to indulge in the joy of playing and embark on\n\n
 a journey towards the ultimate victory by\n\n
 reaching the glorious goal.\n\n
 May your experience be nothing short of extraordinary!
 """
        if self.mode=="hide":
            self.paragraph_text2="""
  Welcome to the exciting Run and Catch mode!\n\n 

  The goal is simple: as the blue player, reach the goal\n\n  

  to emerge victorious. But beware! If the pink player\n\n  

  
  catches you, the red player wins\n\n 

  
  Get ready for an intense chase and may\n\n

  the quickest prevail!\n\n
      """
        else:
            self.paragraph_text2 = """
 Welcome to the heart-pounding multiplayer Escape\n\n
 The Maze mode! Brace yourself for an adrenaline-pumping\n\n
 challenge where the race to victory depends\n\n
 on your lightning-fast speed. Get ready\n\n
 to unleash your inner competitor\n\n
 and experience the thrill of a lifetime.
         """
        
    
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
                        
                            self.frame_coin += 0.15
                            
                            if self.frame_coin >= len(animation_list_coins):
                                self.frame_coin = 0
                            
                            self.window.blit(animation_list_coins[int(self.frame_coin)], ((col*35)+self.window_width//2-(self.cell_width*len(self.maze[0])//2), (row*35)+self.offsett))
                if self.maze[row][col] == "X":
                    wall_cell_image = pygame.image.load(os.path.join("Assets","wall_cell.png"))
                    wall_cell = pygame.transform.scale(wall_cell_image,(self.cell_width,self.cell_height))
                    self.window.blit(wall_cell,((col * self.cell_width)+self.window_width//2-(self.cell_width*len(self.maze[0])//2), row * self.cell_height+self.offsett))    


    def draw_para(self,paragraph_text):
        #for run and catch mode

        lines = paragraph_text.split("\n")
        line_surfaces = []
        max_width = 0
        total_height = 0
        for line in lines:
               line_surface, _ = self.font.render(line, self.button_text_color, None)
               line_surfaces.append(line_surface)
               line_width = line_surface.get_width()
               line_height = line_surface.get_height()
               if line_width > max_width:
                   max_width = line_width
                   total_height += line_height

        x = self.info_button_img_rect.x + (self.info_button_img_rect.width - max_width) // 2
        y = self.info_button_img_rect.y + (self.info_button_img_rect.height - total_height) // 2

        for line_surface in line_surfaces:
           self.window.blit(line_surface, (x-450, y-500))
           y += line_surface.get_height()


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
            pygame.mixer.music.load('Assets/menu-_sound.wav')
            pygame.mixer.music.play(-1)

            return True
        elif self.player_2_pos[0] == self.goal[0] and self.player_2_pos[1]==self.goal[1]:
            winner_text = "Congratulations! Red Win!"
            pygame.mixer.music.stop()
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            pygame.mixer.music.load('Assets/menu-_sound.wav')
            pygame.mixer.music.play(-1)
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
                
                self.player_pos = (self.new_row, self.new_col)
                if self.player_pos[0]*35 + self.offsett >= self.window_height-self.scroll_area and direction =="s" and self.player_pos[0]*35 - self.offsett < len(self.maze)*35 and len(self.maze)*35 > self.window_height :
                    self.offsett -= 140
                if (len(self.maze)-self.player_pos[0])*35 - self.offsett >= self.window_height+self.scroll_area and direction =="w" and self.player_pos[0]>4 and len(self.maze)*35 > self.window_height :
                    self.offsett += 140
                    
            if player == 1:
                self.player_2_pos = (self.new_row, self.new_col)
                if self.player_2_pos[0]*35 + self.offsett >= self.window_height-self.scroll_area and direction =="down" and self.player_2_pos[0]*35 - self.offsett < len(self.maze)*35 and len(self.maze)*35 > self.window_height :
                    self.offsett -= 140
                if (len(self.maze)-self.player_2_pos[0])*35 - self.offsett >= self.window_height+self.scroll_area and direction =="up" and self.player_2_pos[0]>4 and len(self.maze)*35 > self.window_height :

                    self.offsett += 140

    def is_valid_move(self, row, col):
        if row < 0 or row >= len(self.maze) or col < 0 or col >= len(self.maze[0]):
            return False
        if self.maze[row][col] == "X":
            return False
        return True
    
    def run(self,multi=False):
        running = True
        self.display_buttons = True
        self.display_game = False
        while running:

            self.window.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    running = False
                    pygame.mixer.music.load('Assets/menu-_sound.wav')
                    pygame.mixer.music.play(-1)
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

                if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                    
                        if self.ok_button_img_rect.collidepoint(mouse_pos) and self.display_buttons:
                            self.display_buttons=False
                            self.display_game = True

            self.window.fill(BLACK)
            if self.display_buttons:
                self.window.blit(self.info_button_img1 ,(self.info_button_x-450, self.info_button_y-350))
                self.window.blit(self.ok_button ,(self.ok_button_x-50, self.ok_button_y))
                self.ok_button_img_rect = pygame.Rect( self.ok_button_x-50, self.ok_button_y, self.ok_button_width, self.ok_button_height)
                names_button_label,Back_label_rect = self.font.render("OK", self.button_text_color, None)
                Back_label_rect = names_button_label.get_rect(center=self.ok_button_img_rect.center)
                self.window.blit(names_button_label, Back_label_rect)
                if multi:
                    self.draw_para(self.paragraph_text2)
                else:
                    self.draw_para(self.paragraph_text)

            if self.display_game:
                 self.draw_treasure_maze()
                 self.draw_player(self.player_pos[1],self.player_pos[0],1,self.list_player_blue)
                 if multi:
                     self.draw_player(self.player_2_pos[1],self.player_2_pos[0],2,self.list_player_2_red)
                 self.draw_goal()
        
                 if self.check_find_goal():
                     pygame.mixer.music.stop()
                     running = False
                     pygame.mixer.music.load('Assets/menu-_sound.wav')
                     pygame.mixer.music.play(-1) 
                     # mainloop()
            pygame.display.flip()
            self.clock.tick(60)
        


# if __name__ == "__main__":

#     # Create an instance of the MazeGame class
#     game = MazeGame(Maze_maps.maze_hard)

#     # Run the game
#     game.run(True)