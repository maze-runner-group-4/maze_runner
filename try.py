import pygame
import sys
import os
import pygame.freetype
from links_of_modules import links
# Initialize Pygame
pygame.init()
pygame.freetype.init()

# Set up the window
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu Example")

# Set up the colors
background_color = (255, 255, 255)
button_color = (101 ,103, 119)  # Grey color with opacity (R, G, B, A)
button_text_color = (255, 255, 255)
disabled_button_color = (191, 191, 191)
button_clicked_color = (53, 228, 128, 100)  # Grey color with decreased opacity (R, G, B, A)

# Set up the fonts
font_path = "Fonts/font.ttf"
font_size = 10
font = pygame.freetype.Font(font_path, font_size)


# set the image buttons
exit_button_img = pygame.image.load(os.path.join('Assets', 'StoneButtons.png'))
Single_Button_img = pygame.image.load(os.path.join('Assets', 'radiusbutton.png'))
Multi_button_img = pygame.image.load(os.path.join('Assets', 'radiusbutton.png'))
Gold_button_img = pygame.image.load(os.path.join('Assets', 'radiusbuttonclicked.png'))
Menu_buttons_img = pygame.image.load(os.path.join('Assets', 'menubutton.png'))
EZ_buttons_img = pygame.image.load(os.path.join('Assets', 'ez.png'))
Run_disabled_button_img = pygame.image.load(os.path.join('Assets', 'menubuttondisabled.png'))

Button_width=250
Button_height = 100


# Set up the buttons
button_x_center = screen_width // 2 - 100
button_width = 200
button_height = 1
button_padding = 10  # Space between buttons
border_radius = int(button_width * 0.25)
button_x = (screen_width - (2 * button_width + button_padding)) // 2  # Updated position for buttons
FindTreasure_button_y = (screen_height - button_height) // 2 - 120
exit_button_y = (screen_height - button_height) // 2 + 130
multiplayer_button_y = ((screen_height - button_height) // 4 - button_height // 2 ) - 50 # Updated position for Multiplayer button
singleplayer_button_y = ((screen_height - button_height) // 4 - button_height // 2 ) - 50 # Updated position for Single Player button
escape_button_y = (screen_height - button_height) // 2 - 35
run_button_y = (screen_height - button_height) // 2 + 50
dodge_button_y = (screen_height - button_height) // 2 + 80

# new img buttons
exitimg = pygame.transform.scale(exit_button_img,(Button_width , Button_height-20))
Singleimg = pygame.transform.scale(Single_Button_img,(Button_width , Button_height-10))
Multiimg = pygame.transform.scale(Multi_button_img,(Button_width , Button_height-10))
Goldimg = pygame.transform.scale(Gold_button_img,(Button_width , Button_height-10))
Menusimg = pygame.transform.scale(Menu_buttons_img,(Button_width , Button_height-20))
Ezimg = pygame.transform.scale(Menu_buttons_img,(Button_width , Button_height-20))
RunDisabledimg = pygame.transform.scale(Run_disabled_button_img,(Button_width , Button_height-20))

# Apply the backgrounds
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'maze2.jpg')), (screen_width, screen_height))
title_gif = pygame.image.load(os.path.join('Assets', 'mazetitle3.png'))
Background_menu=pygame.image.load(os.path.join('Assets', 'menubackgrounds.png'))
def mainloop():
   
    single_player_clicked = False
    multiplayer_clicked   = False
    escape_screen_active  = False
    # Main game loop 
    while True:
        # Handle events
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if FindTreasure_button.collidepoint(mouse_pos):
                    # if multiplayer_clicked:                    
                     game = links("treasure",multiplayer_clicked)
                     game.run()
                elif exit_button_rect.collidepoint(mouse_pos):
                    # print("Exiting the application...")
                    pygame.quit()
                    sys.exit()
                elif escape_button.collidepoint(mouse_pos):
                    # print("Escape the maze button pressed")
                    escape_screen_active = True
                elif multi_button_rect.collidepoint(mouse_pos):
                    # print("Multiplayer button pressed")
                    multiplayer_clicked = True
                    single_player_clicked = False
                elif single_button_rect.collidepoint(mouse_pos):
                    # print("Single Player button pressed")
                    single_player_clicked = True
                    multiplayer_clicked = False
                elif escape_screen_active and Back.collidepoint(mouse_pos):
                    # print("Back button pressed")
                    escape_screen_active = False
                    single_player_clicked = False
                    multiplayer_clicked = False
                elif dodge_button.collidepoint(mouse_pos):
                    # print("Starting the game...")
                    
                    game = links("multi",multiplayer_clicked)
                    game.run()
                elif run_button.collidepoint(mouse_pos):
                    # print("Starting the game...")
                    if multiplayer_clicked:
                        game = links("hide",multiplayer_clicked)
                        game.run()



        # Clear the screen
        screen.blit(SPACE, (0, 0))

        # screen.blit(Background_menu, ((screen_width//2)-200,180))

        if not escape_screen_active :
            screen.blit(title_gif, ((screen_width - title_gif.get_width()) // 2, 15))
            screen.blit(exitimg, (button_x_center-40, exit_button_y+125)) 
            screen.blit(Multiimg, (button_x-110, multiplayer_button_y)) 
            screen.blit(Singleimg, (button_x_center+130, singleplayer_button_y)) 
            screen.blit(Menusimg, (button_x_center-40, FindTreasure_button_y)) 
            screen.blit(Menusimg, (button_x_center-40, dodge_button_y+60)) 
            screen.blit(Menusimg, (button_x_center-40, escape_button_y)) 


            # Draw the buttons FOR TEXT
            FindTreasure_button = pygame.Rect(button_x_center-45, FindTreasure_button_y, Button_width, Button_height-20)
            escape_button = pygame.Rect(button_x_center-40, escape_button_y, Button_width, Button_height-20)
            dodge_button = pygame.Rect( button_x_center-40, dodge_button_y+60, Button_width, Button_height-20)
            multi_button_rect = pygame.Rect(button_x-110, multiplayer_button_y, Button_width, Button_height-10) 
            single_button_rect = pygame.Rect(button_x_center+130, singleplayer_button_y, Button_width, Button_height-10)
            run_button = pygame.Rect(button_x_center-40, run_button_y, Button_width, Button_height-20)
            exit_button_rect = pygame.Rect(button_x_center-45, exit_button_y+125, Button_width, Button_height-20)

            if multiplayer_clicked:
                screen.blit(Goldimg, (button_x-110, multiplayer_button_y)) 
                screen.blit(Menusimg, (button_x_center-40, run_button_y)) 

            elif single_player_clicked:
                screen.blit(Goldimg, (button_x_center+130, multiplayer_button_y)) 
                screen.blit(RunDisabledimg, (button_x_center-40, run_button_y)) 
            else:
                screen.blit(Goldimg, (button_x_center+130, multiplayer_button_y)) 
                screen.blit(RunDisabledimg, (button_x_center-40, run_button_y)) 

            # Draw the button labels for text position

            start_label,start_label_rect  = font.render("Find the treasure",button_text_color, None)
            start_label_rect = start_label.get_rect(center=FindTreasure_button.center)
            screen.blit(start_label, start_label_rect)

            exit_label,exit_label_rect = font.render("EXIT", button_text_color, None)
            exit_label_rect = exit_label.get_rect(center=exit_button_rect.center)
            screen.blit(exit_label, exit_label_rect)

            escape_label,escape_label_rect = font.render("Escape the maze", button_text_color, None)
            escape_label_rect = escape_label.get_rect(center=escape_button.center)
            screen.blit(escape_label, escape_label_rect)

            run_label,run_label_rect = font.render("Run and catch", button_text_color, None)
            run_label_rect = run_label.get_rect(center=run_button.center)
            screen.blit(run_label, run_label_rect)

            Multiplayer_label,Multiplayer_label_rect = font.render("Multiplayer", button_text_color, None)
            Multiplayer_label_rect = Multiplayer_label.get_rect(center=multi_button_rect.center)
            screen.blit(Multiplayer_label, Multiplayer_label_rect)

            button4_label,button4_label_rect = font.render("Single Player", button_text_color, None)
            button4_label_rect = button4_label.get_rect(center=single_button_rect.center)
            screen.blit(button4_label, button4_label_rect)

            dodge_label,dodge_label_rect = font.render("Dodge the monster", button_text_color, None)
            dodge_label_rect = dodge_label.get_rect(center=dodge_button.center)
            screen.blit(dodge_label, dodge_label_rect)
        else:
            # Draw the escape screen with new buttons

            screen.blit(SPACE, (0, 0))
            screen.blit(title_gif, ((screen_width - title_gif.get_width()) // 2, 30))

            # Set up the new buttons

            Inner_x = screen_width // 2 - button_width // 2 - 50
            Easy_y = screen_height // 2 - button_height // 2 - 250
            Medium_y = screen_height // 2 - button_height // 2 -125
            Hard_y = screen_height // 2 - button_height // 2 
            Back_y = screen_height // 2 - button_height // 2 + 125

            # Drawing the button img

            screen.blit(Menusimg, (Inner_x, Easy_y))
            screen.blit(Menusimg, (Inner_x, Medium_y))
            screen.blit(Menusimg, (Inner_x, Hard_y))
            screen.blit(Menusimg, (Inner_x, Back_y))

            # Draw the new buttons

            Easy = pygame.Rect(Inner_x, Easy_y,Button_width,Button_height)
            Medium = pygame.Rect(Inner_x, Medium_y, Button_width, Button_height)
            Hard = pygame.Rect(Inner_x, Hard_y, Button_width, Button_height)
            Back = pygame.Rect(Inner_x, Back_y, Button_width, Button_height)

            # Draw the new button labels
            Easy_label,Easy_label_rect = font.render("Easy", button_text_color, None)
            Easy_label_rect = Easy_label.get_rect(center=Easy.center)
            screen.blit(Easy_label, Easy_label_rect)

            Medium_label,Medium_label_rect = font.render("Medium", button_text_color, None)
            Medium_label_rect = Medium_label.get_rect(center=Medium.center)
            screen.blit(Medium_label, Medium_label_rect)

            Hard_label,Hard_label_rect = font.render("Hard", button_text_color, None)
            Hard_label_rect = Hard_label.get_rect(center=Hard.center)
            screen.blit(Hard_label, Hard_label_rect)

            Back_label,Back_label_rect = font.render("Back", button_text_color, None)
            Back_label_rect = Back_label.get_rect(center=Back.center)
            screen.blit(Back_label, Back_label_rect)

        if escape_screen_active:
             
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if Back.collidepoint(mouse_pos):
                        # print("Back button pressed")
                        escape_screen_active = False
                        single_player_clicked = False
                        multiplayer_clicked = False  
                    elif Easy.collidepoint(mouse_pos):
                        game1 = links("easy",multiplayer_clicked) 
                        game1.run()
                    elif Medium.collidepoint(mouse_pos):
                        game = links("medium",multiplayer_clicked) 
                        game.run() 
                    elif Hard.collidepoint(mouse_pos):
                        game = links("hard",multiplayer_clicked) 
                        game.run()
                  
        # Update the display
        pygame.display.flip()


mainloop()