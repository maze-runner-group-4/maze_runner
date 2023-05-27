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

        # self.player_pos = self.find_player_start(maze)
        # self.goal = self.find_goal(maze)
        # self.treasure = self.find_treasure(maze)
        self.maze = maze
        self.cell_width = self.window_width // len(self.maze[0])
        self.cell_height = self.window_height // len(self.maze)
        self.border_size = 5

    def draw_maze(self):
        for row in range(len(self.maze)):
            for column in range(len(self.maze[0])):
                if self.maze[row][column] == "X":
                    wall_cell_image = pygame.image.load(os.path.join("Assets","wall_cell.png"))
                    wall_cell = pygame.transform.scale(wall_cell_image,(self.cell_width,self.cell_height))
                    self.window.blit(wall_cell,(column * self.cell_width, row * self.cell_height))

    
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # elif event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_UP:
                #         self.move_player("up")
                #     elif event.key == pygame.K_DOWN:
                #         self.move_player("down")
                #     elif event.key == pygame.K_LEFT:
                #         self.move_player("left")
                #     elif event.key == pygame.K_RIGHT:
                #         self.move_player("right")

            self.window.fill(BLACK)

            self.draw_maze()
            # self.draw_player()
            # self.draw_goal()
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
