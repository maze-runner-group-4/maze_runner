from main import MazeGame

import pygame
import pygame.mixer
import pygame.freetype
import os
BLACK = (0, 0, 0)
WHITE = "white"

class Treasure(MazeGame):
    def __init__(self, maze,mode, multi = False):
        super().__init__( maze,mode)
        pygame.freetype.init()
        self.start_time = 0
        self.str_start_time = " "
        self.treasure_score = 0
        self.treasure2_score = 0
        self.half_treasures = self.treasure_counter//2
        self.treasure_sound = pygame.mixer.Sound(os.path.join("Assets","Mario_Coin_Sound_-_Sound_Effect_HD.wav"))
        ##
        self.font_path = "Fonts/font.ttf"
        self.font_size = 14
        self.font = pygame.freetype.Font(self.font_path, self.font_size)

        self.score_FONT = pygame.font.SysFont('comicsans',30)
        self.goal_draw = False
        self.running =  False
        self.multi = multi
        self.paragraph_text = """
  Welcome to the single player "Find The Treasures" mode!\n\n
  
  Explore the maze,collect all the treasures,\n\n

  and reach the goal to become the ultimate treasure hunter.\n\n

  Good luck on your quest!\n\n
         """
        self.paragraph_text2 = """     Welcome to multiplayer "Find Treasures" mode!\n\n 

     Collect more than half of the treasures to win.\n\n

     If you and your adversary collect the same number\n\n 

     of treasures,the goal will appear.\n\n

     The first player to reach the goal becomes the winner.\n\n

     Enjoy the exciting race for treasures and victory!\n\n
        """

    def calculate_score_for_treasure(self,player):
        if player==1:
            self.treasure2_score +=100
        if player==2: 
            self.treasure_score += 100
 
    def draw_score(self,pos1,pos2,player):
        if player==1: 
            text =f"Blue Player Score : { self.treasure_score}"
            draw_text = self.score_FONT.render(text, 1, WHITE)
            self.window.blit(draw_text, (pos1,pos2))
            pygame.display.update()

        if player==2:
            text2 =f"Red Player Score :{self.treasure2_score}"
            draw_text = self.score_FONT.render(text2, 1, WHITE)
            self.window.blit(draw_text, (pos1,pos2))
            pygame.display.update()


    def move_player(self, direction, player):
        super().move_player(direction, player)
        if self.maze[self.new_row][self.new_col] == "T":
                    # Remove the treasure from the maze
                    self.treasure_sound.play()  # Play the sound effect
                    self.maze[self.new_row][self.new_col] = " "# Remove ####Remove 
                    self.treasure_counter-=1
                    self.calculate_score_for_treasure(player)
                    
        if self.multi:           
            if self.treasure_score >self.half_treasures * 100 or self.treasure2_score >self.half_treasures * 100 :
                self.check_winner()
            elif self.treasure_score == self.half_treasures * 100 == self.treasure2_score and self.treasure_counter%2 ==0 :
                self.goal_draw =True
        else:
            if self.treasure_counter ==0:
                self.goal_draw =True

    
              
    def check_winner(self):
        if self.treasure_score > self.treasure2_score:
            winner_text = "Congratulations! Blue Win!"
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            pygame.mixer.music.stop()
            self.running =  False
            pygame.mixer.music.load('Assets/menu-_sound.wav')
            pygame.mixer.music.play(-1)
            
        elif self.treasure2_score > self.treasure_score:
            winner_text = "Congratulations! Red Win!"
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            pygame.mixer.music.stop()
            self.running = False
            pygame.mixer.music.load('Assets/menu-_sound.wav')
            pygame.mixer.music.play(-1)
            
    def run(self):
        self.running = True
        self.display_buttons = True
        self.display_game = False

        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    self.running = False
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
                if self.multi:
                    self.draw_para(self.paragraph_text2)
                else:
                    self.draw_para(self.paragraph_text)

            if self.display_game:   

                self.draw_treasure_maze()
                self.draw_player(self.player_pos[1],self.player_pos[0],1,self.list_player_blue)
                if self.multi:
                    self.draw_player(self.player_2_pos[1],self.player_2_pos[0],2,self.list_player_2_red)
                if self.goal_draw:    
                    self.draw_goal()
                    if self.check_find_goal():
                        pygame.mixer.music.stop()
                        self.running = False
                        pygame.mixer.music.load('Assets/menu-_sound.wav')
                        pygame.mixer.music.play(-1)
                self.draw_score(10,10,1)
                if self.multi:
                    self.draw_score(self.window_width-220,10,2)
                    
            pygame.display.flip()
            self.clock.tick(60)
        

# if __name__ == "__main__":
#     game = Treasure( Maze_maps.maze_treasure)

#     game.run()
