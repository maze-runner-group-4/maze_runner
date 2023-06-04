from main import MazeGame
from queue_word import Queue
import pygame
import pygame.mixer
from maze_maps import Maze_maps
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
            

        


    def draw_the_letter(self):
        pass
    
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
    