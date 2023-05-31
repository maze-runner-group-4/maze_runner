import pygame
import spritesheet
# from maze_maps import Maze_maps
# from yellow_monester import *
# from blue_player import *
# from coins_sheet import *
pygame.init()
animation_steps=3
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

BG = (0,0,0)
BLACK = (0, 0, 0)

"""
blue monster
"""
blue_monster_front_sheet = pygame.image.load('Assets/spriteimages/blue_monster_frams/blue monster front.png').convert_alpha()
blue_monster_front = spritesheet.SpriteSheet(blue_monster_front_sheet)

blue_monster_back_sheet = pygame.image.load('Assets/spriteimages/blue_monster_frams/blue_monster back.png').convert_alpha()
blue_monster_back = spritesheet.SpriteSheet(blue_monster_back_sheet)


# # front frames blue monster
frame_0_blue_monster_front = blue_monster_front.get_image(0, 240, 275, 1, BLACK)
frame_1_blue_monster_front = blue_monster_front.get_image(1, 240, 275, 1, BLACK)
frame_2_blue_monster_front = blue_monster_front.get_image(2, 240, 275, 1, BLACK)
frame_3_blue_monster_front= blue_monster_front.get_image(3, 240, 275, 1, BLACK)
list_of_frams_blue_monster_front = [frame_0_blue_monster_front, frame_1_blue_monster_front, frame_2_blue_monster_front, frame_3_blue_monster_front]
# # back frames blue monster
frame_0_blue_monster_back = blue_monster_back.get_image(0, 240, 275, 1, BLACK)
frame_1_blue_monster_back = blue_monster_back.get_image(1, 240, 275, 1, BLACK)
frame_2_blue_monster_back = blue_monster_back.get_image(2, 240, 275, 1, BLACK)
frame_3_blue_monster_back = blue_monster_back.get_image(3, 240, 275, 1, BLACK)
list_of_frames_blue_monster_back = [frame_0_blue_monster_back, frame_1_blue_monster_back, frame_2_blue_monster_back, frame_3_blue_monster_back]

# """
# red monster
# """

red_monster_front_sheet = pygame.image.load('Assets/spriteimages/red_monster_frams/red monster front.png').convert_alpha()
red_monster_front = spritesheet.SpriteSheet(red_monster_front_sheet)

red_monster_back_sheet = pygame.image.load('Assets/spriteimages/red_monster_frams/red monster back.png').convert_alpha()
red_monster_back = spritesheet.SpriteSheet(red_monster_back_sheet)

# # BG = (0,0,0)
# # BLACK = (0, 0, 0)

# # front frames red monster
frame_0_red_monster_front = red_monster_front.get_image(0, 235, 275, 1, BLACK)
frame_1_red_monster_front = red_monster_front.get_image(1, 235, 275, 1, BLACK)
frame_2_red_monster_front = red_monster_front.get_image(2, 235, 275, 1, BLACK)
frame_3_red_monster_front= red_monster_front.get_image(3, 235, 275, 1, BLACK)
list_of_frames_red_monster_front = [frame_0_red_monster_front, frame_1_red_monster_front, frame_2_red_monster_front, frame_3_red_monster_front]
# # back frames red monster
frame_0_red_monster_back = red_monster_back.get_image(0, 240, 275, 1, BLACK)
frame_1_red_monster_back = red_monster_back.get_image(1, 240, 275, 1, BLACK)
frame_2_red_monster_back = red_monster_back.get_image(2, 240, 275, 1, BLACK)
frame_3_red_monster_back = red_monster_back.get_image(3, 240, 275, 1, BLACK)
list_of_frames_red_monster_back = [frame_0_red_monster_back,frame_1_red_monster_back,frame_2_red_monster_back,frame_3_red_monster_back]
# """
# red player
# """

red_player_front_sheet = pygame.image.load('Assets/spriteimages/red_player/red player front.jpg').convert_alpha()
red_player_front = spritesheet.SpriteSheet(red_player_front_sheet)

red_player_back_sheet = pygame.image.load('Assets/spriteimages/red_player/red player back.jpg').convert_alpha()
red_player_back = spritesheet.SpriteSheet(red_player_back_sheet)


red_player_left_sheet = pygame.image.load('Assets/spriteimages/red_player/red player left.jpg').convert_alpha()
red_player_left = spritesheet.SpriteSheet(red_player_left_sheet)

red_player_right_sheet = pygame.image.load('Assets/spriteimages/red_player/red player right.jpg').convert_alpha()
red_player_right = spritesheet.SpriteSheet(red_player_right_sheet)


# left frames red player
frame_0_red_player_left = red_player_left.get_image(0, 50, 60, 1, BLACK)
frame_1_red_player_left = red_player_left.get_image(1, 50, 60, 1, BLACK)
frame_2_red_player_left = red_player_left.get_image(2, 50, 60, 1, BLACK)
list_of_frams_red_player_left = [frame_0_red_player_left,frame_1_red_player_left,frame_2_red_player_left]
# # right frames red player
frame_0_red_player_right = red_player_right.get_image(0, 50, 60, 1, BLACK)
frame_1_red_player_right = red_player_right.get_image(1, 50, 60, 1, BLACK)
frame_2_red_player_right = red_player_right.get_image(2, 50, 60, 1, BLACK)
list_of_frames_red_player_right = [frame_0_red_player_right, frame_1_red_player_right,frame_2_red_player_right]
# front frames red player
frame_0_red_player_front = red_player_front.get_image(0, 50, 60, 1, BLACK)
frame_1_red_player_front = red_player_front.get_image(1, 50, 60, 1, BLACK)
frame_2_red_player_front = red_player_front.get_image(2, 50, 60, 1, BLACK)
list_of_frames_red_player_front = [frame_0_red_player_front, frame_1_red_player_front,frame_2_red_player_front]
# back frames red player 

frame_0_red_player_back = red_player_back.get_image(0, 50, 60, 1, BLACK)
frame_1_red_player_back = red_player_back.get_image(1, 50, 60, 1, BLACK)
frame_2_red_player_back = red_player_back.get_image(2, 50, 60, 1, BLACK)
list_of_frames_red_player_back = [frame_0_red_player_back, frame_1_red_player_back,frame_2_red_player_back]

# """
# hearts
# """

hearts_sheet1 = pygame.image.load('Assets/spriteimages/hearts/heart_1.png').convert_alpha()
hearts_sheet2= pygame.image.load('Assets/spriteimages/hearts/heart_2.png').convert_alpha()
hearts_sheet3= pygame.image.load('Assets/spriteimages/hearts/heart_3.png').convert_alpha()
hearts_sheet4 = pygame.image.load('Assets/spriteimages/hearts/heart_4.png').convert_alpha()
hearts_sheet5= pygame.image.load('Assets/spriteimages/hearts/heart_5.png').convert_alpha()
hearts_sheet6= pygame.image.load('Assets/spriteimages/hearts/heart_6.png').convert_alpha()
hearts1 = spritesheet.SpriteSheet(hearts_sheet1)
hearts2 = spritesheet.SpriteSheet(hearts_sheet2)
hearts3 = spritesheet.SpriteSheet(hearts_sheet3)
hearts4 = spritesheet.SpriteSheet(hearts_sheet4)
hearts5 = spritesheet.SpriteSheet(hearts_sheet5)
hearts6 = spritesheet.SpriteSheet(hearts_sheet6)

frame_0_hearts = hearts1.get_image(0, 120, 120, 1, BLACK)
frame_1_hearts = hearts2.get_image(0, 120, 120, 1, BLACK)
frame_2_hearts = hearts3.get_image(0, 120, 120, 1, BLACK)
frame_3_hearts = hearts4.get_image(0, 120, 120, 1, BLACK)
frame_4_hearts = hearts5.get_image(0, 120, 120, 1, BLACK)
frame_5_hearts = hearts6.get_image(0, 120, 120, 1, BLACK)
list_of_frames_hearts = [frame_0_hearts, frame_1_hearts, frame_2_hearts, frame_3_hearts, frame_4_hearts, frame_5_hearts]
cooldown = 500
delay=pygame.time.get_ticks()
frame= 0

########################################################################################################################
sprite_sheet_image = pygame.image.load('Assets/spriteimages/blue_player/blue_player_down.png-removebg-preview.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

sprite_sheet_image_left = pygame.image.load('Assets/spriteimages/blue_player/blue_player_left.png-removebg-preview.png').convert_alpha()
sprite_sheet_left = spritesheet.SpriteSheet(sprite_sheet_image_left)

sprite_sheet_image_right = pygame.image.load('Assets/spriteimages/blue_player/blue_player_right-removebg-preview.png').convert_alpha()
sprite_sheet_right = spritesheet.SpriteSheet(sprite_sheet_image_right)

sprite_sheet_image_up = pygame.image.load('Assets/spriteimages/blue_player/blue_player_up-removebg-preview.png').convert_alpha()
sprite_sheet_up = spritesheet.SpriteSheet(sprite_sheet_image_up)




# BG = (50, 50, 50)
# BLACK = (0, 0, 0)
animation_list_down_blue_player= []
animation_list_left_blue_player= []
animation_list_right_blue_player= []
animation_list_up_blue_player = []



for x in range(animation_steps):
 animation_list_down_blue_player.append(sprite_sheet.get_image(x, 32, 50, 1, BLACK))

for x in range(animation_steps):
 animation_list_left_blue_player.append(sprite_sheet_left.get_image(x, 32, 50, 1, BLACK))

for x in range(animation_steps):
 animation_list_right_blue_player.append(sprite_sheet_right.get_image(x, 32, 50, 1, BLACK))

for x in range(animation_steps):
 animation_list_up_blue_player.append(sprite_sheet_up.get_image(x, 32, 50, 1, BLACK))


###############################################################################################################################################

sprite_sheet_image1 = pygame.image.load('Assets/spriteimages/coins/coin_1.png').convert_alpha()
sprite_sheet_image2 = pygame.image.load('Assets/spriteimages/coins/coin_2.png').convert_alpha()
sprite_sheet_image3 = pygame.image.load('Assets/spriteimages/coins/coin_3.png').convert_alpha()
sprite_sheet_image4 = pygame.image.load('Assets/spriteimages/coins/coin_4.png').convert_alpha()
sprite_sheet_image5 = pygame.image.load('Assets/spriteimages/coins/coin_5.png').convert_alpha()
sprite_sheet_image6 = pygame.image.load('Assets/spriteimages/coins/coin_6.png').convert_alpha()
sprite_sheet1 = spritesheet.SpriteSheet(sprite_sheet_image1)
sprite_sheet2 = spritesheet.SpriteSheet(sprite_sheet_image2)
sprite_sheet3 = spritesheet.SpriteSheet(sprite_sheet_image3)
sprite_sheet4 = spritesheet.SpriteSheet(sprite_sheet_image4)
sprite_sheet5 = spritesheet.SpriteSheet(sprite_sheet_image5)
sprite_sheet6 = spritesheet.SpriteSheet(sprite_sheet_image6)


# BG = (50, 50, 50)
# BLACK = (0, 0, 0)
animation_list_coins= [sprite_sheet1.get_image(0, 234, 234, 1, BLACK),sprite_sheet2.get_image(0, 234, 234, 1, BLACK), sprite_sheet3.get_image(0, 234, 234, 1, BLACK), sprite_sheet4.get_image(0, 234, 234, 1, BLACK),sprite_sheet5.get_image(0, 234, 234, 1, BLACK),sprite_sheet6.get_image(0, 234, 234, 1, BLACK)]

# for x in range(animation_steps+3):
#  animation_list_coins.append(sprite_sheet.get_image(x, 234, 234, 1, BLACK))
#############################################################################################################################################

sprite_sheet_image = pygame.image.load('Assets/spriteimages/yellow_monster/yellow monster_down.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

sprite_sheet_image_left = pygame.image.load('Assets/spriteimages/yellow_monster/yellow monster_left.png').convert_alpha()
sprite_sheet_left = spritesheet.SpriteSheet(sprite_sheet_image_left)

sprite_sheet_image_right = pygame.image.load('Assets/spriteimages/yellow_monster/yellow monster_right.png').convert_alpha()
sprite_sheet_right = spritesheet.SpriteSheet(sprite_sheet_image_right)

sprite_sheet_image_up = pygame.image.load('Assets/spriteimages/yellow_monster/yellow monster_up.png').convert_alpha()
sprite_sheet_up = spritesheet.SpriteSheet(sprite_sheet_image_up)


# BG = (50, 50, 50)
# BLACK = (0, 0, 0)
animation_list_down= []
animation_list_left= []
animation_list_right= []
animation_list_up = []

for x in range(animation_steps):
 animation_list_down.append(sprite_sheet.get_image(x, 222, 250, 1, BLACK))

for x in range(animation_steps):
 animation_list_left.append(sprite_sheet_left.get_image(x, 222, 250, 1, BLACK))

for x in range(animation_steps):
 animation_list_right.append(sprite_sheet_right.get_image(x, 222, 250, 1, BLACK))

for x in range(animation_steps):
 animation_list_up.append(sprite_sheet_up.get_image(x, 222, 250, 1, BLACK))

############################################################################################################################################


# run = True
# while run:

# 	#update background
# 	screen.fill(BG)

# 	current_time = pygame.time.get_ticks()
# 	if current_time - delay>=cooldown:
# 		frame+=1
# 		delay = current_time
# 		if frame >=len(list_of_frames_hearts):
# 			frame = 0
# 	screen.blit(list_of_frames_hearts[frame], (0, 0))
			
# 	#show frame image
	
# 	# screen.blit(frame_1_hearts, (180, 0))
# 	# screen.blit(frame_2_hearts, (360, 0))
# 	# screen.blit(frame_3_hearts, (540, 0))
# 	# # # show back image
# 	# screen.blit(frame_4_hearts, (720, 0))
# 	# screen.blit(frame_5_hearts, (900, 0))
# 	# screen.blit(frame_2_hearts, (100, 100))
# 	# screen.blit(frame_3_hearts, (150, 100))

# 	#event handler
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			run = False

# 	pygame.display.update()

# pygame.quit()