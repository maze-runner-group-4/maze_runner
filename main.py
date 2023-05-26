import pygame


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

        self.maze = maze
        self.cell_width = self.window_width // len(self.maze[0])
        self.cell_height = self.window_height // len(self.maze)
        self.border_size = 5



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

            if self.check_find_goal():
                print("Congratulations! You Win!")
                running = False


            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


# Set up the maze grid
maze = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXXT XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX                 T  X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Create an instance of the MazeGame class
game = MazeGame(800, 600, maze)

# Run the game
game.run()
