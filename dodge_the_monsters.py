import os
import pygame
from main import MazeGame
from maze_maps import Maze_maps
import pygame.freetype
from spritesheet_test import list_of_frames_blue_monster_back,list_of_frames_red_monster_back,list_of_frames_hearts,list_of_frames_red_monster_front,list_of_frams_blue_monster_front,animation_list_left,animation_list_right
BLACK = (0, 0, 0)
WHITE = "white"
class Dodge_the_monsters(MazeGame):
    
    def __init__(self, maze,mode):
        super().__init__( maze,mode)
        pygame.init()
        self.start_time = 0
        self.str_start_time = " "
        self.button_text_color = (255, 255, 255)
        self.font_path = "Fonts/font.ttf"
        self.font_size = 14
        self.font = pygame.freetype.Font(self.font_path, self.font_size)
        self.running=True
        self.multi2_maze = maze
        self.game_over_FONT = pygame.font.SysFont('comicsans', 100)
        self.game_over_FONT_player = pygame.font.SysFont('comicsans', 50)
        self.heart_sound = pygame.mixer.Sound(os.path.join("Assets","Heal_Sound_Effect_2.wav"))
        self.monster_sound_effect2 = pygame.mixer.Sound(os.path.join("Assets","Pac-Man Death - Sound Effect (HD).wav"))
        self.monster_sound_slap = pygame.mixer.Sound(os.path.join("Assets","SLAP - Sound Effect.wav"))
        self.sound_effect_played = False
        if self.multi2_maze == Maze_maps.maze_multi2:
            self.monster4_pos = self.find_character(maze,"K")
        self.monster1_pos=self.find_character(maze,"M")
        self.monster2_pos=self.find_character(maze,"S")
        self.monster3_pos=self.find_character(maze,"R")
        self.heart_pos=self.find_character(maze,"H")
        self.player_health=3
        self.player_2_health = 3
        self.heart_x = 5 + (self.cell_width + 5) # for heart left player one 
        self.heart2_x = self.window_width-self.cell_width*6
        self.frame_heart = 0
        if self.multi2_maze == Maze_maps.maze_multi2:
            # monster 1
            self.monster1_vel = -0.5
            self.monster_range_M = 9 
            self.delay_M = pygame.time.get_ticks()
            self.cooldown_M = 200
            self.frame_M = 0
            self.list_M = list_of_frames_blue_monster_back
            # monster 2
            self.monster2_vel = -0.5
            self.monster_range_S = 9 
            self.delay_S = pygame.time.get_ticks()
            self.cooldown_S = 200
            self.frame_S = 0
            self.list_S = list_of_frames_blue_monster_back
            # monster 3
            self.monster3_vel = 1
            self.monster_range_R = 35 
            self.delay_R = pygame.time.get_ticks()
            self.cooldown_R = 200
            self.frame_R = 0
            self.list_R = animation_list_right
            # monster 4
            self.monster4_vel = 1
            self.monster_range_K = 35 
            self.delay_K = pygame.time.get_ticks()
            self.cooldown_K = 200
            self.frame_K = 0
            self.list_K = animation_list_right
        else:
            self.monster1_vel = -0.5
            self.monster2_vel = -0.5
            self.monster3_vel = 1
            self.movement_range_M = 11
            self.movement_range_S = 11
            self.movement_range_R = 47
        # moving_the_monsters = self.monster_movement(self.movement_range_M,self.movement_range_S,self.movement_range_R)
            self.delay_M=pygame.time.get_ticks()
            self.cooldown_M = 200
            self.frame_M= 0
            self.list_M = list_of_frames_blue_monster_back
            self.delay_S=pygame.time.get_ticks()
            self.cooldown_S = 200
            self.frame_S= 0
            self.list_S = list_of_frames_red_monster_back
            self.delay_R=pygame.time.get_ticks()
            self.cooldown_R = 200
            self.frame_R= 0
            self.list_R = animation_list_right
        self.paragraph_text = """

  Welcome to the heart-pounding "Dodge the Monster" mode!\n\n

  Navigate with precision to evade the relentless monster's\n\n 

  attacks and keep your health intact. Keep your adrenaline\n\n 

  pumping as you collect life-saving hearts to stay in the\n\n  

  game.Victory awaits those who reach the goal with\n\n 

  unwavering determination and good health. Get ready\n\n  
  
  for an exhilarating challenge like no other!

         """
        self.paragraph_text2 = """
    Welcome to multiplayer "Dodge the Monster" mode!\n\n 

    Dodge the monster, collect hearts, and race against\n\n
    your opponent to reach the goal with good health.\n\n\n 
    
    Get ready for an exhilarating challenge!\n\n

    Enjoy the excitement! 

        
         """
    def draw_hearts(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == "H":
                    self.frame_heart += 0.5
                    if self.frame_heart >= len(list_of_frames_hearts):
                        self.frame_heart = 0

                    self.window.blit(list_of_frames_hearts[int(self.frame_heart)], ((col*35)+self.window_width//2-(self.cell_width*len(self.maze[0])//2), row*35+self.offsett))                    # treasure_cell_image = pygame.image.load(os.path.join("Assets","heart1.png"))
                    

    def draw_hearts_points(self,player_health,heart_x): 
        for i in range(player_health):
            heart_y = 0
            heart_image = pygame.image.load(os.path.join("Assets", "333-removebg-preview.png"))
            heart_image = pygame.transform.scale(heart_image, (self.cell_width, self.cell_height))
            self.window.blit(heart_image, (heart_x+(i*self.cell_width), heart_y+self.offsett))
        pygame.display.update()
        
    
    def draw_monster(self, pos_x, pos_y, monster,list):
        if self.multi2_maze == Maze_maps.maze_multi2:
            if monster =="M":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_M >= self.cooldown_M:
                    self.frame_M += 1
                    self.delay_M = current_time
                    if self.frame_M >= len(list):
                        self.frame_M = 0
                self.window.blit(list[self.frame_M], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), (pos_y*35)+self.offsett))
            elif monster == "S":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_S >= self.cooldown_S:
                    self.frame_S += 1
                    self.delay_S = current_time
                    if self.frame_S >= len(list):
                        self.frame_S = 0
                self.window.blit(list[self.frame_S], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), (pos_y*35)+self.offsett))
            elif monster == "R":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_R >= self.cooldown_R:
                    self.frame_R += 1
                    self.delay_R = current_time
                    if self.frame_R >= len(list):
                        self.frame_R = 0
                self.window.blit(list[self.frame_R], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett))
            elif monster == "K":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_K >= self.cooldown_K:
                    self.frame_K += 1
                    self.delay_K = current_time
                    if self.frame_K >= len(list):
                        self.frame_K= 0
                self.window.blit(list[self.frame_K], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett))
        else:

            if monster =="M":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_M >= self.cooldown_M:
                    self.frame_M += 1
                    self.delay_M = current_time
                    if self.frame_M >= len(list):
                        self.frame_M = 0
                self.window.blit(list[self.frame_M], (pos_x*35, (pos_y*35)+self.window_width//2-(self.cell_width*len(self.maze[0])//2)+self.offsett))
            elif monster == "S":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_S >= self.cooldown_S:
                    self.frame_S += 1
                    self.delay_S = current_time
                    if self.frame_S >= len(list):
                        self.frame_S = 0
                self.window.blit(list[self.frame_S], (pos_x*35, (pos_y*35)+self.window_width//2-(self.cell_width*len(self.maze[0])//2)+self.offsett))
            elif monster == "R":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_R >= self.cooldown_R:
                    self.frame_R += 1
                    self.delay_R = current_time
                    if self.frame_R >= len(list):
                        self.frame_R = 0
                self.window.blit(list[self.frame_R], (pos_x*35, pos_y*35+self.offsett))
        

       


    def monster_movement(self):
        if self.multi2_maze == Maze_maps.maze_multi2:
            # monster 1 movement
            self.monster1_pos[0] += self.monster1_vel
            if self.monster1_pos[0] <= 14:
                self.monster1_vel *= -1
                self.list_M = list_of_frams_blue_monster_front
            if self.monster1_pos[0] >= 23:
                self.monster1_vel *= -1
                self.list_M = list_of_frames_blue_monster_back
            # monster 2 movement
            self.monster2_pos[0] += self.monster2_vel
            if self.monster2_pos[0] <= 14:
                self.monster2_vel *= -1
                self.list_S = list_of_frames_red_monster_front
            if self.monster2_pos[0] >= 23:
                self.monster2_vel *= -1
                self.list_S = list_of_frames_red_monster_back
            
            # monster 3  movement
            self.monster3_pos[1] += self.monster3_vel
            if self.monster3_pos[1] >= 35:
                self.monster3_vel *= -1
                self.list_R = animation_list_left
            if self.monster3_pos[1] <= 2:
                self.monster3_vel *= -1
                self.list_R = animation_list_right
            
            # monster 4  movement
            self.monster4_pos[1] += self.monster4_vel
            if self.monster4_pos[1] >= 35:
                self.monster4_vel *= -1
                self.list_K = animation_list_left
            if self.monster4_pos[1] <= 2:
                self.monster4_vel *= -1
                self.list_K = animation_list_right
        else:
            # monster 1 movement
            self.monster1_pos[0] += self.monster1_vel
            if self.monster1_pos[0] <= 14:
                self.monster1_vel *= -1
                self.list_M = list_of_frams_blue_monster_front
            if self.monster1_pos[0] >= 25:
                self.monster1_vel *= -1
                self.list_M = list_of_frames_blue_monster_back
            # monster 2 movement
            self.monster2_pos[0] += self.monster2_vel
            if self.monster2_pos[0] <= 14:
                self.monster2_vel *= -1
                self.list_S = list_of_frames_red_monster_front
            if self.monster2_pos[0] >= 25:
                self.monster2_vel *= -1
                self.list_S = list_of_frames_red_monster_back
            
            # monster 3  movement
            self.monster3_pos[1] += self.monster3_vel
            if self.monster3_pos[1] >= 49:
                self.monster3_vel *= -1
                self.list_R = animation_list_left
            if self.monster3_pos[1] <= 2:
                self.monster3_vel *= -1
                self.list_R = animation_list_right

    def game_over(self,multi):
        if self.player_health == self.player_2_health ==0 :
            game_over_text = "Game Over"
            self.draw_game_over(game_over_text)
            pygame.mixer.music.stop()
            self.monster_sound_effect2.play()
            self.game_over_sound.play()
            pygame.display.update()
            pygame.time.delay(2000)
            self.running = False
            pygame.mixer.music.load('Assets/menu-_sound.wav')
            pygame.mixer.music.play(-1)
        if self.player_health == 0 and self.player_2_health != 0 :
            game_over_text = "Blue lost!"
            self.draw_game_over(game_over_text)
            if not self.sound_effect_played:
                self.monster_sound_effect2.play()  # Play sound effect_2
                self.sound_effect_played = True
            if not multi:
                 self.draw_game_over("Game Over")
                 pygame.display.update()
                 pygame.time.delay(2000)
                 pygame.mixer.music.stop()
                 self.running = False
                 pygame.mixer.music.load('Assets/menu-_sound.wav')
                 pygame.mixer.music.play(-1)    
            
        if self.player_2_health == 0 and self.player_health != 0 :
            game_over_text = "Red lost!"
            self.draw_game_over(game_over_text)
            if not self.sound_effect_played:
                self.monster_sound_effect2.play()  # Play sound effect_2
                self.sound_effect_played = True
               
            

 

    def draw_game_over(self,text):
        if text == "Game Over":
            draw_text = self.game_over_FONT.render(text, 1, WHITE)
            pos_x= self.window_width/2 - draw_text.get_width() /2
            pos_y = self.window_height/2 - draw_text.get_height()/2
        if text == "Blue lost!":
            draw_text = self.game_over_FONT_player.render(text, 1, WHITE)
            pos_x = 5 + ( draw_text.get_width())
            pos_y = 0
        if text == "Red lost!":
            draw_text = self.game_over_FONT_player.render(text, 1, WHITE)
            pos_x = self.window_width-draw_text.get_width()
            pos_y = 0
        self.window.blit(draw_text, (pos_x,pos_y+self.offsett))



    def health_points_count(self):
        if self.multi2_maze == Maze_maps.maze_multi2:
            if (self.player_pos[0] == self.monster1_pos[0] and self.player_pos[1] == self.monster1_pos[1]) or \
            (self.player_pos[0] == self.monster2_pos[0] and self.player_pos[1] == self.monster2_pos[1]) or \
            (self.player_pos[0] == self.monster3_pos[0] and self.player_pos[1] == self.monster3_pos[1]) or \
            (self.player_pos[0] == self.monster4_pos[0] and self.player_pos[1] == self.monster4_pos[1]):
                if self.player_health > 0:
                    self.player_health -= 1
                    self.monster_sound_slap.play()
            if (self.player_2_pos[0] == self.monster1_pos[0] and self.player_2_pos[1] == self.monster1_pos[1]) or \
                (self.player_2_pos[0] == self.monster2_pos[0] and self.player_2_pos[1] == self.monster2_pos[1]) or \
                (self.player_2_pos[0] == self.monster3_pos[0] and self.player_2_pos[1] == self.monster3_pos[1]) or \
                (self.player_2_pos[0] == self.monster4_pos[0] and self.player_2_pos[1] == self.monster4_pos[1])    :
                if self.player_2_health > 0:
                    self.player_2_health -= 1
                    self.monster_sound_slap.play()

            if self.player_2_health == 0:
                self.maze[self.player_2_pos[0]][self.player_2_pos[1]] = " "
            if self.player_health == 0:
                self.maze[self.player_pos[0]][self.player_pos[1]] = " "
        else:

            if (self.player_pos[0] == self.monster1_pos[0] and self.player_pos[1] == self.monster1_pos[1]) or \
            (self.player_pos[0] == self.monster2_pos[0] and self.player_pos[1] == self.monster2_pos[1]) or \
            (self.player_pos[0] == self.monster3_pos[0] and self.player_pos[1] == self.monster3_pos[1]):
                if self.player_health > 0:
                    self.player_health -= 1
                    self.monster_sound_slap.play()
            if (self.player_2_pos[0] == self.monster1_pos[0] and self.player_2_pos[1] == self.monster1_pos[1]) or \
                (self.player_2_pos[0] == self.monster2_pos[0] and self.player_2_pos[1] == self.monster2_pos[1]) or \
                (self.player_2_pos[0] == self.monster3_pos[0] and self.player_2_pos[1] == self.monster3_pos[1]):
                if self.player_2_health > 0:
                    self.player_2_health -= 1
                    self.monster_sound_slap.play()

            if self.player_2_health == 0:
                self.maze[self.player_2_pos[0]][self.player_2_pos[1]] = " "
            if self.player_health == 0:
                self.maze[self.player_pos[0]][self.player_pos[1]] = " "

    

    def move_player(self, direction, player):
        super().move_player(direction, player)
        if self.is_valid_move(self.new_row,self. new_col):
            if self.maze[self.new_row][self.new_col] == "H":
                    # Remove the hearts from the maze
                    self.maze[self.new_row][self.new_col] = " "
                    if player == 2:
                        self.player_health += 1
                    if player == 1:
                        self.player_2_health += 1
                    
                    self.heart_sound.play()  # Play the sound effect
    


    def run(self, multi=False):
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
                    if self.player_2_health > 0:
                        if event.key == pygame.K_UP:
                            self.move_player("up",1)
                        elif event.key == pygame.K_DOWN:
                            self.move_player("down",1)
                        elif event.key == pygame.K_LEFT:
                            self.move_player("left",1)
                        elif event.key == pygame.K_RIGHT:
                            self.move_player("right",1)
                    if self.player_health > 0:
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
                 if self.player_health > 0 :
                     self.draw_player(self.player_pos[1],self.player_pos[0],1,self.list_player_blue)
                 if multi and self.player_2_health > 0 :
                    self.draw_player(self.player_2_pos[1],self.player_2_pos[0],2,self.list_player_2_red)
                 self.draw_goal()
                 self.draw_treasure_maze()
                 self.draw_monster(self.monster1_pos[1],self.monster1_pos[0],"M",self.list_M)
                 self.draw_monster(self.monster2_pos[1],self.monster2_pos[0],"S",self.list_S)
                 self.draw_monster(self.monster3_pos[1],self.monster3_pos[0],"R",self.list_R)
                 if self.multi2_maze == Maze_maps.maze_multi2:
                     self.draw_monster(self.monster4_pos[1],self.monster4_pos[0],"K",self.list_K)

                 self.draw_hearts()    
                 self.draw_hearts_points(self.player_health,self.heart_x)
                 if multi:
                     self.draw_hearts_points(self.player_2_health,self.heart2_x)
                 self.health_points_count()
                 self.game_over(multi)
                 self.monster_movement()
         
                 if self.check_find_goal():
                     pygame.mixer.music.stop()
                     self.running = False
                     pygame.mixer.music.load('Assets/menu-_sound.wav')
                     pygame.mixer.music.play(-1)
            pygame.display.flip()
            self.clock.tick(60)

# if __name__ == "__main__":

#     # Create an instance of the MazeGame class
#     game = Dodge_the_monsters( Maze_maps.maze_multi)


#     # Run the game
#     game.run(True)