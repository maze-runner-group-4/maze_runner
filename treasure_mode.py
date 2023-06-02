from main import MazeGame
# from maze_maps import Maze_maps
import pygame
import pygame.mixer
import os
BLACK = (0, 0, 0)
indigo = "indigo"
# from GUI import mainloop
class Treasure(MazeGame):
    def __init__(self, maze):
        super().__init__( maze)
        
        self.treasure_score = 0
        self.treasure2_score = 0
        self.half_treasures = self.treasure_counter//2
        self.treasure_sound = pygame.mixer.Sound(os.path.join("Assets","Mario_Coin_Sound_-_Sound_Effect_HD.wav"))
        self.score_FONT = pygame.font.SysFont('comicsans',30)
        self.goal_draw = False


    def calculate_score_for_treasure(self,player):
        if player==1:
            self.treasure2_score +=100
        if player==2: 
            self.treasure_score += 100
 
    def draw_score(self,pos1,pos2,player):
        if player==1: 
            text =f"Blue Player Score : { self.treasure_score}"
            draw_text = self.score_FONT.render(text, 1, indigo)
            self.window.blit(draw_text, (pos1,pos2))
            pygame.display.update()

        if player==2:
            text2 =f"Red Player Score :{self.treasure2_score}"
            draw_text = self.score_FONT.render(text2, 1, indigo)
            self.window.blit(draw_text, (pos1,pos2))
            pygame.display.update()


    def move_player(self, direction, player):
        super().move_player(direction, player)
        if self.maze[self.new_row][self.new_col] == "T":
                    # Remove the treasure from the maze
                    self.maze[self.new_row][self.new_col] = " "
                    self.treasure_counter-=1
                    self.treasure_sound.play()  # Play the sound effect
                    self.calculate_score_for_treasure(player)
                    # self.treasure_sound.play()
                    
        if self.treasure_score >self.half_treasures * 100 or self.treasure2_score >self.half_treasures * 100 :
            self.check_winner()
        elif self.treasure_score == self.half_treasures * 100 == self.treasure2_score :
            self.goal_draw =True

              
    def check_winner(self):
        if self.treasure_score > self.treasure2_score:
            winner_text = "Congratulations! Blue Win!"
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            # mainloop()
        elif self.treasure2_score > self.treasure_score:
            winner_text = "Congratulations! Red Win!"
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            # mainloop()
    def run(self,multi=False):
        running = True
        while running:
            
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
            self.window.fill(BLACK)
            self.draw_treasure_maze()
            self.draw_player(self.player_pos[1],self.player_pos[0],1,self.list_player_blue)
            if multi:
                self.draw_player(self.player_2_pos[1],self.player_2_pos[0],2,self.list_player_2_red)
            if self.goal_draw:    
                self.draw_goal()
                if self.check_find_goal():
                    pygame.mixer.music.stop()
                    running = False
            self.draw_score(10,10,1)
            if multi:
                self.draw_score(self.window_width-220,10,2)
            pygame.display.flip()
            self.clock.tick(60)
        # pygame.quit()

if __name__ == "__main__":
    game = Treasure( Maze_maps.maze_treasure)

    game.run(True)
