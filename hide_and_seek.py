from main import MazeGame
import pygame
# import os

class Hide_and_seek(MazeGame):
    def __init__(self, maze,mode):
        super().__init__( maze,mode)
        self.start_time = 0
        self.str_start_time = " "
        # self.game_win_sound.play() 

    def check_find_goal(self):
        if self.player_pos[0] == self.goal[0] and self.player_pos[1]==self.goal[1]:
            winner_text = "Congratulations! Blue Win!"
            pygame.mixer.music.stop()
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            return True
        elif self.player_2_pos[0] == self.player_pos[0] and self.player_2_pos[1]==self.player_pos[1]:
            winner_text = "Congratulations! Red Win!"
            pygame.mixer.music.stop()

            self.game_win_sound.play()
            self.draw_winner(winner_text)
            return True
        return False
      
# if __name__ == "__main__":

    # Create an instance of the MazeGame class
    # game = Hide_and_seek( Maze_maps.maze_easy)

    # # Run the game
    # game.run(True)