from main import MazeGame
from maze_maps import Maze_maps


class Hide_and_seek(MazeGame):
    def __init__(self, maze):
        super().__init__( maze)

    def check_find_goal(self):
        if self.player_pos[0] == self.goal[0] and self.player_pos[1]==self.goal[1]:
            winner_text = "Congratulations! Blue Win!"
            self.draw_winner(winner_text)
            return True
        elif self.player_2_pos[0] == self.player_pos[0] and self.player_2_pos[1]==self.player_pos[1]:
            winner_text = "Congratulations! Red Win!"
            self.draw_winner(winner_text)
            return True
        return False
      
if __name__ == "__main__":

    # Create an instance of the MazeGame class
    game = Hide_and_seek( Maze_maps.maze_easy)

    # Run the game
    game.run(True)