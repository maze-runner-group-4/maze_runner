from main import MazeGame
from queue_word import Queue
import pygame
import pygame.mixer
from maze_maps import Maze_maps
from spritesheet_test import animation_list_Tletters,animation_list_Mletters,animation_list_Sletters,animation_list_Aletters,animation_list_Cletters,animation_list_Eletters,animation_list_numbers
import os
BLACK = (0, 0, 0)
WHITE = "white"

class Collect_the_word(MazeGame):
    def __init__(self, maze, multi=False):
        super().__init__(maze)
        # self.word_queue = Queue()
        self.goal_draw=False  
        self.score_FONT = pygame.font.SysFont('comicsans',30)
        "Create queue for the blue player "
        self.multi=multi
        self.player_blue_score=Queue()
        self.player_blue_score.enqueue("A")
        self.player_blue_score.enqueue("S")
        self.player_blue_score.enqueue("A")
        self.player_blue_score.enqueue("C")
        self.player_blue_score.enqueue("T")
        self.player_blue_score.enqueue("E")
        self.player_blue_score.enqueue("A")
        self.player_blue_score.enqueue("M")
        self.player_blue_score.enqueue("4")
        "Create queue for the red player"
        self.player_red_score=Queue()
        self.player_red_score.enqueue("A")
        self.player_red_score.enqueue("S")
        self.player_red_score.enqueue("A")
        self.player_red_score.enqueue("C")
        self.player_red_score.enqueue("T")
        self.player_red_score.enqueue("E")
        self.player_red_score.enqueue("A")
        self.player_red_score.enqueue("M")
        self.player_red_score.enqueue("4")
        self.player_2_pos = self.find_character(maze,"L")
        self.player_pos = self.find_character(maze,"P")
        self.A = animation_list_Aletters
        self.S = animation_list_Sletters  
        self.C = animation_list_Cletters  
        self.T = animation_list_Tletters  
        self.E = animation_list_Eletters  
        self.M = animation_list_Mletters  
        self.N4 = animation_list_numbers
        self.A_pos = self.find_character(maze,"A")
        self.S_pos = self.find_character(maze,"S")
        self.C_pos = self.find_character(maze,"C")
        self.T_pos = self.find_character(maze,"V")
        self.E_pos = self.find_character(maze,"E")
        self.M_pos = self.find_character(maze,"M")
        self.N4_pos = self.find_character(maze,"4")
        self.frame_A = 0
        self.frame_S = 0
        self.frame_C = 0
        self.frame_T = 0
        self.frame_E = 0
        self.frame_M = 0
        self.frame_N4 = 0
        self.delay_A = pygame.time.get_ticks()
        self.delay_S = pygame.time.get_ticks()
        self.delay_C = pygame.time.get_ticks()
        self.delay_T = pygame.time.get_ticks()
        self.delay_E = pygame.time.get_ticks()
        self.delay_M = pygame.time.get_ticks()
        self.delay_N4 = pygame.time.get_ticks()
        self.cooldown_A = 200
        self.cooldown_S = 200
        self.cooldown_C = 200
        self.cooldown_T = 200
        self.cooldown_E = 200
        self.cooldown_M = 200
        self.cooldown_N4 = 200

    def check_word(self, player):
        if player == 1: 
  
            front_of_queue = self.player_blue_score.peek()  
            if self.maze[self.player_pos[1]][self.player_pos[0]] == front_of_queue: # Update the maze 
                self.player_blue_score.dequeue()
                self.maze[self.player_pos[1]][self.player_pos[0]] == " " # Remove the letter 

            if self.maze[self.player_pos [1]][self.player_pos [0]] == "V" and front_of_queue == "T": # Update the maze 
                self.player_red_score.dequeue()
                self.maze[self.player_pos [1]][self.player_pos [0]] == " " # Remove the letter
        if player == 2:
            
            front_of_queue2 = self.player_red_score.peek()  
            if self.maze[self.player_2_pos [0]][self.player_2_pos [1]] == front_of_queue2: # Update the maze 
                self.player_red_score.dequeue()
                self.maze[self.player_2_pos [0]][self.player_2_pos [1]] == " " # Remove the letter 

            if self.maze[self.player_2_pos [0]][self.player_2_pos [1]] == "V" and front_of_queue2 == "T": # Update the maze 
                self.player_red_score.dequeue()
                self.maze[self.player_2_pos [0]][self.player_2_pos [1]] == " " # Remove the letter

        if self.player_blue_score.isEmpty() or self.player_red_score.isEmpty() :  
            self.goal_draw=True  
            

    
    def draw_the_letter(self,pos_x, pos_y,letter,list):
            if letter =="A":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_A >= self.cooldown_A:
                    self.frame_A += 1
                    self.delay_A = current_time
                    if self.frame_A >= len(list):
                        self.frame_A = 0
                self.window.blit(list[self.frame_A], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), (pos_y*35)+self.offsett))
            elif letter == "S":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_S >= self.cooldown_S:
                    self.frame_S += 1
                    self.delay_S = current_time
                    if self.frame_S >= len(list):
                        self.frame_S = 0
                self.window.blit(list[self.frame_S], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), (pos_y*35)+self.offsett))
            elif letter == "C":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_C >= self.cooldown_C:
                    self.frame_C += 1
                    self.delay_C = current_time
                    if self.frame_C >= len(list):
                        self.frame_C = 0
                self.window.blit(list[self.frame_C], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett))
            elif letter == "V":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_T >= self.cooldown_T:
                    self.frame_T += 1
                    self.delay_T = current_time
                    if self.frame_T >= len(list):
                        self.frame_T= 0
                self.window.blit(list[self.frame_T], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett))
            elif letter == "E":
                  current_time = pygame.time.get_ticks()
                  if current_time - self.delay_E >= self.cooldown_E:
                      self.frame_E += 1
                      self.delay_E = current_time
                      if self.frame_E >= len(list):
                          self.frame_E= 0
                  self.window.blit(list[self.frame_E], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett))
            elif letter == "M":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_M >= self.cooldown_M:
                    self.frame_M += 1
                    self.delay_M = current_time
                    if self.frame_M >= len(list):
                        self.frame_M= 0
                self.window.blit(list[self.frame_M], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett))
            elif letter == "4":
                current_time = pygame.time.get_ticks()
                if current_time - self.delay_N4 >= self.cooldown_N4:
                    self.frame_N4 += 1
                    self.delay_N4 = current_time
                    if self.frame_N4 >= len(list):
                        self.frame_N4= 0
                self.window.blit(list[self.frame_N4], (pos_x*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), pos_y*35+self.offsett)) 
    
    def move_player(self, direction, player): 
        super().move_player(direction, player)
        self.check_word(player)


    def showing_score(self,pos1,pos2,player):
        if player==1: 
            blue_score_text =f"Blue Player Word : { self.player_blue_score.__str__()}"
            draw_text = self.score_FONT.render(blue_score_text, 1, WHITE)
            self.window.blit(draw_text, (pos1,pos2))
            pygame.display.update()
        if player==2 and self.multi: 
            red_score_text =f"Red Player Word : {  self.player_red_score.__str__()}"
            draw_text = self.score_FONT.render(red_score_text, 1, WHITE)
            self.window.blit(draw_text, (pos1,pos2))
            pygame.display.update()


    def check_find_goal(self):
        pass  


    def run(self):
        self.running = True
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
            self.window.fill(BLACK)
            self.draw_treasure_maze()
            self.draw_the_letter(self.A_pos[1],self.A_pos[0],"A",self.A)
            self.draw_the_letter(self.S_pos[1],self.S_pos[0],"S",self.S)
            self.draw_the_letter(self.C_pos[1],self.C_pos[0],"C",self.C)
            self.draw_the_letter(self.T_pos[1],self.T_pos[0],"V",self.T)
            self.draw_the_letter(self.E_pos[1],self.E_pos[0],"E",self.E)
            self.draw_the_letter(self.M_pos[1],self.M_pos[0],"M",self.M)
            self.draw_the_letter(self.N4_pos[1],self.N4_pos[0],"4",self.N4)
            self.draw_player(self.player_pos[1],self.player_pos[0],1,self.list_player_blue)
            self.showing_score(5,5,1)
            if self.multi:
                self.showing_score(self.window_width-360,5,2)
                self.draw_player(self.player_2_pos[1],self.player_2_pos[0],2,self.list_player_2_red)
            if self.goal_draw:    
                self.draw_goal()
                if self.check_find_goal():
                    pygame.mixer.music.stop()
                    self.running = False
                    pygame.mixer.music.load('Assets/menu-_sound.wav')
                    pygame.mixer.music.play(-1)
            # self.draw_the_letter(10,10,1)
            # if self.multi:
            #     self.draw_the_letter(self.window_width-220,10,2)
            pygame.display.flip()
            self.clock.tick(60)
        # pygame.quit()

if __name__ == "__main__":
    game = Collect_the_word( Maze_maps.complete_the_word_maze,True)

    game.run()
    