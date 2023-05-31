# import pygame
# import spritesheet
# # from maze_maps import Maze_maps
# pygame.init()

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 500

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Spritesheets')

# sprite_sheet_image = pygame.image.load('Assets/spriteimages/coins/coins_2.png').convert_alpha()
# sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)


# BG = (50, 50, 50)
# BLACK = (0, 0, 0)
# animation_list_coins= []
# animation_steps=6
# last_update= pygame.time.get_ticks()
# animation_cooldown= 200
# frame=0
# for x in range(animation_steps):
#  animation_list_coins.append(sprite_sheet.get_image(x, 190, 234, 1, BLACK))


# # run = True
# # while run:
# #     # Update background
# #     screen.fill(BG)

# #     current_time= pygame.time.get_ticks()
# #     if current_time - last_update >= animation_cooldown:
# #        frame+=1
# #        last_update = current_time
# #        if frame >= animation_steps:
# #           frame=0

# #     # Show frame image
       
# #     screen.blit(animation_list[frame], (0, 0))

# #     # Event handling
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False

# #     pygame.display.update()

# # # Quit the game
# # pygame.quit()
