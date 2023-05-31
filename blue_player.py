# import pygame
# import spritesheet
# # from maze_maps import Maze_maps
# pygame.init()

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 500

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Spritesheets')

# sprite_sheet_image = pygame.image.load('Assets/spriteimages/blue_player/blue_player_down.png-removebg-preview.png').convert_alpha()
# sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

# sprite_sheet_image_left = pygame.image.load('Assets/spriteimages/blue_player/blue_player_left.png-removebg-preview.png').convert_alpha()
# sprite_sheet_left = spritesheet.SpriteSheet(sprite_sheet_image_left)

# sprite_sheet_image_right = pygame.image.load('Assets/spriteimages/blue_player/blue_player_right-removebg-preview.png').convert_alpha()
# sprite_sheet_right = spritesheet.SpriteSheet(sprite_sheet_image_right)

# sprite_sheet_image_up = pygame.image.load('Assets/spriteimages/blue_player/blue_player_up-removebg-preview.png').convert_alpha()
# sprite_sheet_up = spritesheet.SpriteSheet(sprite_sheet_image_up)

# # sprite_sheet_image = pygame.image.load('Assets/spriteimages/blue_player_down-removebg-preview2.png').convert_alpha()
# # sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

# BG = (50, 50, 50)
# BLACK = (0, 0, 0)
# animation_list_down_blue_player= []
# animation_list_left_blue_player= []
# animation_list_right_blue_player= []
# animation_list_up_blue_player = []
# animation_steps=3
# last_update= pygame.time.get_ticks()
# animation_cooldown= 200
# frame=0
# # for x in range(animation_steps):
# #  animation_list_down.append(sprite_sheet.get_image(x, 32, 50, 1, BLACK))

# for x in range(animation_steps):
#  animation_list_down_blue_player.append(sprite_sheet.get_image(x, 32, 50, 1, BLACK))

# for x in range(animation_steps):
#  animation_list_left_blue_player.append(sprite_sheet_left.get_image(x, 32, 50, 1, BLACK))

# for x in range(animation_steps):
#  animation_list_right_blue_player.append(sprite_sheet_right.get_image(x, 32, 50, 1, BLACK))

# for x in range(animation_steps):
#  animation_list_up_blue_player.append(sprite_sheet_up.get_image(x, 32, 50, 1, BLACK))

# # run = True
# # while run:
# #     # Update background
# #     screen.fill(BG)

# #     #update animation
# #     current_time= pygame.time.get_ticks()
# #     if current_time - last_update >= animation_cooldown:
# #        frame+=1
# #        last_update = current_time
# #        if frame >= animation_steps:
# #           frame=0

# #     # Show frame image
# #     screen.blit(animation_list_down[frame], (0, 0))

# #     screen.blit(animation_list_left[frame], (0,55))

# #     screen.blit(animation_list_right[frame], (0, 110))

# #     screen.blit(animation_list_up[frame], (0, 165))        
# #     # Event handling
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False

# #     pygame.display.update()

# # # Quit the game
# # pygame.quit()
