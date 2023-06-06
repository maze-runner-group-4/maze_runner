from maze_maps import Maze_maps
from main import MazeGame
from treasure_mode import Treasure
from dodge_the_monsters import Dodge_the_monsters
from hide_and_seek import Hide_and_seek
from collect_the_word import Collect_the_word
import random
# from GUI import mainloop
class links:
    def __init__(self,mode,multiplayer):
        self.mode = mode
        self.check_multi = multiplayer
        self.easy = [Maze_maps.maze_easy, Maze_maps.maze_easy2 ,Maze_maps.maze_easy3]
        self.medium = Maze_maps.list_of_medium_maps
        self.hard = Maze_maps.list_of_hard_maps
        self.multi = Maze_maps.list_of_multi_maps
        self.treasure = Maze_maps.list_of_treasure_maps
        self.hide = Maze_maps.list_of_hide_maps
        self.collect_the_word = Maze_maps.complete_the_word_maze
        self.start_time = 0
        self.str_start_time = " "

    def get_rand_list (self,list):
       EMHT_index =  random.randint(0,2)
       multi_index = random.randint(0,1)
       hide_index = random.randint(0,8)
       if self.mode == "easy" or self.mode =="medium" or self.mode == "hard" or self.mode =="treasure":
            return list[EMHT_index]
       elif self.mode == "multi":
           return list[multi_index]
       else:
           return list[hide_index]
       
    def run(self):
        
        if self.mode == "easy" :
            game = MazeGame(self.get_rand_list(self.easy),self.mode)
        if self.mode =="medium" :
            game = MazeGame(self.get_rand_list(self.medium),self.mode)
        if self.mode == "hard":
            game = MazeGame(self.get_rand_list(self.hard),self.mode)
        if self.mode == "treasure":
            game = Treasure(self.get_rand_list(self.treasure),self.mode,self.check_multi)
        if self.mode == "multi":
            game = Dodge_the_monsters(self.get_rand_list(self.multi),self.mode)
        if self.mode == "hide":
            game = Hide_and_seek(self.get_rand_list(self.hide),self.mode)
        if self.mode == "word":
            game = Collect_the_word(self.collect_the_word,self.mode,self.check_multi)
        
        # check multi
        if self.check_multi == True and self.mode != "treasure" and self.mode != "word":
            game.run(self.check_multi)
        else:
            game.run()
        # or self.mode =="medium" or self.mode == "hard" or self.mode =="treasure":
        #     return list[EMHT_index]
        # elif self.mode == "multi":
        #    return list[multi_index]
        # else:
        #    return list[hide_index]
