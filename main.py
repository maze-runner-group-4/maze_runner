import pygame
import os
from maze_maps import Maze_maps


BLACK = (0, 0, 0)
WHITE = "indigo"
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class MazeGame:
    def __init__(self, width, height, maze):
        pygame.init()
        pygame.font.init()
        self.window_width = width
        self.window_height = height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Maze Game")
        self.WINNER_FONT = pygame.font.SysFont('comicsans', 100)

        self.clock = pygame.time.Clock()

        self.player_pos = self.find_player_start(maze,"P")
        self.player_2_pos = self.find_player_start(maze,"L")
        self.goal = self.find_goal(maze)
        self.treasure = self.find_treasure(maze)
        self.maze = maze
        self.cell_width = self.window_width // len(self.maze[0])
        self.cell_height = self.window_height // len(self.maze)
        

    def find_player_start(self, maze,Char):
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if maze[row][col] == Char:
                    return [row, col]  
        return None  

    def find_goal(self, maze):
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if maze[row][col] == "G":
                    return [row, col]  
        return None  
    
    def find_treasure(self, maze):
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if maze[row][col] == "T":
                    return [row, col]   
        return None  
    
    def draw_treasure(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == "T":
                    treasure_cell_image = pygame.image.load(os.path.join("Assets","IMG_9986.png"))
                    treasure_image = pygame.transform.scale(treasure_cell_image,(self.cell_width,self.cell_height))
                    self.window.blit(treasure_image,(col* self.cell_width,row* self.cell_height))


    def draw_maze(self):
        for row in range(len(self.maze)):
            for column in range(len(self.maze[0])):
                if self.maze[row][column] == "X":
                    wall_cell_image = pygame.image.load(os.path.join("Assets","wall_cell.png"))
                    wall_cell = pygame.transform.scale(wall_cell_image,(self.cell_width,self.cell_height))
                    self.window.blit(wall_cell,(column * self.cell_width, row * self.cell_height))
    
    def draw_player(self,pos_x,pos_y,player):
        if player ==1:

            player_cell_image = pygame.image.load(os.path.join("Assets","IMG_0011.png"))
        else:
            player_cell_image = pygame.image.load(os.path.join("Assets","image.png"))
        player_cell = pygame.transform.scale(player_cell_image,(self.cell_width,self.cell_height))
        self.window.blit(player_cell,(pos_y * self.cell_width, pos_x * self.cell_height))


    def draw_goal(self):

        goal_cell_image = pygame.image.load(os.path.join("Assets","IMG_9998.png"))
        goal_cell = pygame.transform.scale(goal_cell_image,(self.cell_width,self.cell_height))
        self.window.blit(goal_cell,(self.goal[1] * self.cell_width, self.goal[0] * self.cell_height))

    def check_find_goal(self):
        if self.player_pos[0] == self.goal[0] and self.player_pos[1]==self.goal[1]:
            winner_text = "Congratulations! You Win!"
            self.draw_winner(winner_text)
            return True
        elif self.player_2_pos[0] == self.goal[0] and self.player_2_pos[1]==self.goal[1]:
            winner_text = "Congratulations! You Win!"
            self.draw_winner(winner_text)
            return True
        return False
    
    def draw_winner(self,text):
        draw_text = self.WINNER_FONT.render(text, 1, WHITE)
        self.window.blit(draw_text, (self.window_width/2 - draw_text.get_width() /
                         2,self.window_height/2 - draw_text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(1000)

    def move_player(self, direction,player):
        new_col = 0
        new_row = 0
        if player == 2:
         new_row = self.player_pos[0]
         new_col = self.player_pos[1]
        elif player == 1:
            new_row = self.player_2_pos[0]
            new_col = self.player_2_pos[1]
        if direction == "up":
            new_row -= 1
        elif direction == "down":
            new_row += 1
        elif direction == "left":
            new_col -= 1
        elif direction == "right":
            new_col += 1

        if direction == "w":
            new_row -= 1
        elif direction == "s":
            new_row += 1
        elif direction == "a":
            new_col -= 1
        elif direction == "d":
            new_col += 1
        if self.is_valid_move(new_row, new_col):
            if player == 2:
                self.player_pos = (new_row, new_col)
            if player == 1:
                self.player_2_pos = (new_row, new_col)
                

    def is_valid_move(self, row, col):
        if row < 0 or row >= len(self.maze) or col < 0 or col >= len(self.maze[0]):
            return False
        if self.maze[row][col] == "X":
            return False
        return True
    
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
            if self.check_find_goal():
                self.check_find_goal()
                running = False


            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()



if __name__ == "__main__":

    # Create an instance of the MazeGame class
    game = MazeGame(1000, 500, Maze_maps.maze_hard2)

    # Run the game
    game.run()
