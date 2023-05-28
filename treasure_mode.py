from main import MazeGame
from maze_maps import Maze_maps
import pygame

BLACK = (0, 0, 0)
WHITE = "indigo"
RED = (255, 0, 0)
GREEN = (0, 255, 0)
class Treasure(MazeGame):
    def __init__(self, width, height, maze):
        super().__init__(width, height, maze)
        self.treasure_score = 0
        self.treasure2_score = 0
        self.score_FONT = pygame.font.SysFont('comicsans',30)


    def calculate_score_for_treasure(self,player):
        if player==1:
            self.treasure2_score +=1
        if player==2: 
            self.treasure_score += 1
 
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

             
    def sound_for_tresure():
        pass

    def move_player(self, direction, player):
        super().move_player(direction, player)
        if self.maze[self.new_row][self.new_col] == "T":
                    # Remove the treasure from the maze
                    self.maze[self.new_row][self.new_col] = " "
                    # self.treasure_sound.play()  # Play the sound effect
                    self.calculate_score_for_treasure(player)
              

    def run(self):
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

            self.draw_maze()
            self.draw_player(self.player_pos[0],self.player_pos[1],1)
            self.draw_player(self.player_2_pos[0],self.player_2_pos[1],2)
            self.draw_goal()
            self.draw_treasure()
            self.draw_score(10,10,1)
            self.draw_score(self.window_width-200,10,2)
            if self.check_find_goal():
                self.check_find_goal()
                running = False


            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


game = Treasure(1200, 900, Maze_maps.maze_treasure)

game.run()
