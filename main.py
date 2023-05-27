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
        self.window_width = width
        self.window_height = height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Maze Game")

        self.clock = pygame.time.Clock()

        self.player_pos = self.find_player_start(maze)
        self.goal = self.find_goal(maze)
        self.treasure = self.find_treasure(maze)
        self.maze = maze
        self.cell_width = self.window_width // len(self.maze[0])
        self.cell_height = self.window_height // len(self.maze)
        self.border_size = 5

    def find_player_start(self, maze):
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if maze[row][col] == "P":
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
    
    def draw_player(self):
        player_rect = pygame.Rect(
            self.player_pos[1] * self.cell_width + self.border_size,
            self.player_pos[0] * self.cell_height + self.border_size,
            self.cell_width - self.border_size * 2,
            self.cell_height - self.border_size * 2
        )
        pygame.draw.rect(self.window, RED, player_rect)

    def draw_goal(self):
        goal_rect = pygame.Rect(
            self.goal[1] * self.cell_width + self.border_size,
            self.goal[0] * self.cell_height + self.border_size,
            self.cell_width - self.border_size * 2,
            self.cell_height - self.border_size * 2
        )
        pygame.draw.rect(self.window, GREEN, goal_rect)
    def move_player(self, direction):
        new_row = self.player_pos[0]
        new_col = self.player_pos[1]

        if direction == "up":
            new_row -= 1
        elif direction == "down":
            new_row += 1
        elif direction == "left":
            new_col -= 1
        elif direction == "right":
            new_col += 1

        if self.is_valid_move(new_row, new_col):
            self.player_pos = (new_row, new_col)

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
                        self.move_player("up")
                    elif event.key == pygame.K_DOWN:
                        self.move_player("down")
                    elif event.key == pygame.K_LEFT:
                        self.move_player("left")
                    elif event.key == pygame.K_RIGHT:
                        self.move_player("right")

            self.window.fill(BLACK)

            self.draw_maze()
            self.draw_player()
            self.draw_goal()
            self.draw_treasure()
            # if self.check_find_goal():
            #     print("Congratulations! You Win!")
            #     running = False


            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()





# Create an instance of the MazeGame class
game = MazeGame(1200, 900, Maze_maps.maze_treasure)

# Run the game
game.run()
