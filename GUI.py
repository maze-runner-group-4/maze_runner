import pygame
import sys
import os
import pygame.freetype
from links_of_modules import links
from pygame.locals import *
import pygame.mixer
from spritesheet_test import animation_list_blue_player , animation_list_red_player

# Initialize Pygame
pygame.init()
pygame.freetype.init()

# Set up the window
screen_width = 1820
screen_height = 945
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu Example")
Click_sound = pygame.mixer.Sound(os.path.join("Assets","clickbutton.mp3"))


# Set up the colors
background_color = (255, 255, 255)
button_color = (101 ,103, 119)  # Grey color with opacity (R, G, B, A)
button_text_color = (255, 255, 255)
disabled_button_color = (191, 191, 191)
button_clicked_color = (53, 228, 128, 100)  # Grey color with decreased opacity (R, G, B, A)

# Set up the fonts
font_path = "Fonts/font.ttf"
font_size = 14
font_size_names = 32

font = pygame.freetype.Font(font_path, font_size)
fontName = pygame.freetype.Font(font_path, font_size_names)



# set the image buttons
exit_button_img = pygame.image.load(os.path.join('Assets', 'StoneButtons.png'))
Single_Button_img = pygame.image.load(os.path.join('Assets', 'radiusbutton.png'))
Multi_button_img = pygame.image.load(os.path.join('Assets', 'radiusbutton.png'))
Gold_button_img = pygame.image.load(os.path.join('Assets', 'radiusbuttonclicked.png'))
Menu_buttons_img = pygame.image.load(os.path.join('Assets', 'menubutton.png'))
EZ_buttons_img = pygame.image.load(os.path.join('Assets', 'ez.png'))
Run_disabled_button_img = pygame.image.load(os.path.join('Assets', 'menubuttons.png'))
About_us_button_img = pygame.image.load(os.path.join('Assets', 'About_us.png')) #About
About_us_border_img = pygame.image.load(os.path.join('Assets', 'card.png')) 
card = pygame.image.load(os.path.join('Assets', 'card.png')) 
card2=pygame.image.load(os.path.join('Assets', 'card.png'))
card3=pygame.image.load(os.path.join('Assets', 'card.png'))
card4=pygame.image.load(os.path.join('Assets', 'card.png'))
card5=pygame.image.load(os.path.join('Assets', 'card.png')) 


About_us_border_img_width = 850
About_us_border_img_height =800

Button_width=370
Button_height = 150

About_Button_width=150
About_Button_height = 150



# Set up the buttons
button_x_center = screen_width // 2 - 100
button_width = 200
button_height = 1
button_padding = 10  # Space between buttons
border_radius = int(button_width * 0.25)
button_x = (screen_width - (2 * button_width + button_padding)) // 2  # Updated position for buttons
FindTreasure_button_y = (screen_height - button_height) // 2 - 200
exit_button_y = (screen_height - button_height) // 2 + 190
multiplayer_button_y = ((screen_height - button_height) // 4 - button_height // 2 ) - 100 # Updated position for Multiplayer button
singleplayer_button_y = ((screen_height - button_height) // 4 - button_height // 2 ) - 100 # Updated position for Single Player button
escape_button_y = (screen_height - button_height) // 2 - 65
run_button_y = (screen_height - button_height) // 2 + 60
dodge_button_y = (screen_height - button_height) // 2 + 125

About_us_button_x = (screen_width - (2 * button_width + button_padding)) 
About_us_button_y = 10

About_us_border_img_x= screen_width // 2 - 100
About_us_border_img_y=(screen_height - button_height) // 2 - 65

card1_x=screen_width // 2 - 100
card1_y=(screen_height - button_height) // 2 - 200

card2_x=screen_width // 2 - 100
card2_y=(screen_height - button_height) // 2 + 190

card_width=400
card_height=150

name_stone_width=370
name_stone_height=110



team_width=300
team_height=300





# new img buttons
exitimg = pygame.transform.scale(exit_button_img,(Button_width , Button_height-20))
Singleimg = pygame.transform.scale(Single_Button_img,(Button_width , Button_height-10))
Multiimg = pygame.transform.scale(Multi_button_img,(Button_width , Button_height-10))
Goldimg = pygame.transform.scale(Gold_button_img,(Button_width , Button_height-10))
Menusimg = pygame.transform.scale(Menu_buttons_img,(Button_width , Button_height-20))
Ezimg = pygame.transform.scale(Menu_buttons_img,(Button_width , Button_height-20))
RunDisabledimg = pygame.transform.scale(Run_disabled_button_img,(Button_width , Button_height-20))
About_us=pygame.transform.scale(About_us_button_img,(About_Button_width-50, About_Button_height-60)) #About
border=pygame.transform.scale(About_us_border_img,(About_us_border_img_width,About_us_border_img_height)) 
card_1=pygame.transform.scale(card,(card_width,card_height))
card_2=pygame.transform.scale(card,(card_width+50,card_height))
card_3=pygame.transform.scale(card,(card_width,card_height))
card_4=pygame.transform.scale(card,(card_width+50,card_height))
card_5=pygame.transform.scale(card,(card_width,card_height))
back_about_us=pygame.transform.scale(card,(card_width-250,card_height-50))

# Apply the backgrounds
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'maze2_upscaled.jpg')), (screen_width, screen_height))
title_gif = pygame.image.load(os.path.join('Assets', 'mazetitle3.png'))
Background_menu=pygame.image.load(os.path.join('Assets', 'menubackgrounds.png'))
def mainloop():
# Defining the triggers
    
    single_player_clicked = False
    multiplayer_clicked   = False
    escape_screen_active  = False
    About_us_clicked = False #About
    Find_treasure_clicked = False
   
# Draw the animations
   
    Blue_player = animation_list_blue_player
    Red_player = animation_list_red_player  
    
    delay_Blue= pygame.time.get_ticks()
    delay_Red = pygame.time.get_ticks()
    
    cooldown = 200
    
    frame_Blue = 0
    frame_Red= 0


    


    pygame.mixer.music.load('Assets/menu-_sound.wav')
    pygame.mixer.music.play(-1)
   
    # Main game loop 
    while True:
        # Handle events
       
        
        # Clear the screen
        screen.blit(SPACE, (0, 0))


        if not escape_screen_active and not About_us_clicked and not Find_treasure_clicked :
            screen.blit(title_gif, ((screen_width - title_gif.get_width()) // 2, 15))
            screen.blit(exitimg, (button_x_center-40, exit_button_y+125)) 
            screen.blit(Multiimg, (button_x-110, multiplayer_button_y)) 
            screen.blit(Singleimg, (button_x_center+130, singleplayer_button_y)) 
            screen.blit(Menusimg, (button_x_center-40, FindTreasure_button_y)) 
            screen.blit(Menusimg, (button_x_center-40, dodge_button_y+60)) 
            screen.blit(Menusimg, (button_x_center-40, escape_button_y)) 
            screen.blit(About_us, (About_Button_width +1569,About_Button_height-150)) #About

            current_time = pygame.time.get_ticks()
            if current_time - delay_Blue >= cooldown:
                frame_Blue += 1
                delay_Blue = current_time
                if frame_Blue >= 3:
                    frame_Blue = 0
            screen.blit(Blue_player[int(frame_Blue)], (1350, 450))

    
            if multiplayer_clicked:
             current_time = pygame.time.get_ticks()
             if current_time - delay_Red >= cooldown:
                 frame_Red += 1
                 delay_Red = current_time
                 if frame_Red >= 3:
                     frame_Red = 0
             screen.blit(Red_player[int(frame_Red)], (400, 450))

            # Draw the buttons FOR TEXT
            FindTreasure_button = pygame.Rect(button_x_center-45, FindTreasure_button_y, Button_width, Button_height-20)
            escape_button = pygame.Rect(button_x_center-40, escape_button_y, Button_width, Button_height-20)
            dodge_button = pygame.Rect( button_x_center-40, dodge_button_y+60, Button_width, Button_height-20)
            multi_button_rect = pygame.Rect(button_x-110, multiplayer_button_y, Button_width, Button_height-10) 
            single_button_rect = pygame.Rect(button_x_center+130, singleplayer_button_y, Button_width, Button_height-10)
            run_button = pygame.Rect(button_x_center-40, run_button_y, Button_width, Button_height-20)
            exit_button_rect = pygame.Rect(button_x_center-45, exit_button_y+125, Button_width, Button_height-20)
            About_us_rect = pygame.Rect(About_us_button_x, About_us_button_y, Button_width - 20, Button_height - 20)
            About_us_border_rect = pygame.Rect(About_us_border_img_x, About_us_border_img_y, About_us_border_img_width - 20, About_us_border_img_height - 20)            

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

            start_label,start_label_rect  = font.render("Treasure Hunter",button_text_color, None)
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


            About_label, About_label_rect = font.render("About us", button_text_color, None,pygame.freetype.STYLE_DEFAULT, 0, 11)
            About_label_rect.topright = (About_us_rect.left + 405, About_us_rect.top + 30)
            screen.blit(About_label, About_label_rect)

            

            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
             elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()                
                 if FindTreasure_button.collidepoint(mouse_pos):
                      Click_sound.play()    
                      Find_treasure_clicked = True
                      escape_screen_active = False  
                      About_us_clicked = False            
                  
                 elif exit_button_rect.collidepoint(mouse_pos):
                     Click_sound.play()  
                     pygame.quit()
                     sys.exit()
                 elif escape_button.collidepoint(mouse_pos):
                     
                     Click_sound.play()  
                     escape_screen_active = True
                 elif multi_button_rect.collidepoint(mouse_pos):
                     Click_sound.play() 
                     multiplayer_clicked = True
                     single_player_clicked = False
                 elif single_button_rect.collidepoint(mouse_pos):
                     Click_sound.play() 
                     single_player_clicked = True
                     multiplayer_clicked = False

                 elif escape_screen_active and Back.collidepoint(mouse_pos):
                     escape_screen_active = False
                     single_player_clicked = False
                     multiplayer_clicked = False

                 elif About_us_rect.collidepoint(mouse_pos):#About
                     Click_sound.play()
                     About_us_clicked=True
                      
                 elif dodge_button.collidepoint(mouse_pos):
                     Click_sound.play() 
                     game = links("multi",multiplayer_clicked)
                     game.run()
                     
                 elif run_button.collidepoint(mouse_pos):

                    if multiplayer_clicked:
                        Click_sound.play() 
                        game = links("hide",multiplayer_clicked)
                        game.run()



        elif escape_screen_active and not About_us_clicked :
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

            Easy = pygame.Rect(Inner_x, Easy_y-5,Button_width,Button_height)
            Medium = pygame.Rect(Inner_x, Medium_y-5, Button_width, Button_height)
            Hard = pygame.Rect(Inner_x, Hard_y-5, Button_width, Button_height)
            Back = pygame.Rect(Inner_x, Back_y-5, Button_width, Button_height)

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

            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              elif event.type == pygame.MOUSEBUTTONDOWN:
                  mouse_pos = pygame.mouse.get_pos()
                  Click_sound.play()
                  if Back.collidepoint(mouse_pos):
                      Click_sound.play()
                      escape_screen_active = False
                      single_player_clicked = False
                      multiplayer_clicked = False  
                  elif Easy.collidepoint(mouse_pos):
                      Click_sound.play()
                      game1 = links("easy",multiplayer_clicked) 
                      game1.run()
                  elif Medium.collidepoint(mouse_pos):
                      Click_sound.play()
                      game = links("medium",multiplayer_clicked) 
                      game.run() 
                  elif Hard.collidepoint(mouse_pos):
                      Click_sound.play()  
                      game = links("hard",multiplayer_clicked) 
                      game.run()


        elif Find_treasure_clicked and not escape_screen_active and not About_us_clicked :
          # Draw new screen  

          screen.blit(SPACE, (0, 0))
          screen.blit(title_gif, ((screen_width - title_gif.get_width()) // 2, 30))
          # Define the button position
          Inner_x = screen_width // 2 - button_width // 2 - 50
          Treasuregoal_y = screen_height // 2 - button_height // 2 -125
          Lettercollect_y = screen_height // 2 - button_height // 2 
          Back_y = screen_height // 2 - button_height // 2 + 125

          # Showing the buttons image  
          screen.blit(Menusimg, (Inner_x, Treasuregoal_y))
          screen.blit(Menusimg, (Inner_x, Lettercollect_y))
          screen.blit(Menusimg, (Inner_x, Back_y))

          # Create rectangle for the images texts  
          Treasuregoal = pygame.Rect(Inner_x, Treasuregoal_y-5, Button_width, Button_height)
          Lettercollect = pygame.Rect(Inner_x, Lettercollect_y-5, Button_width, Button_height)  
          Back = pygame.Rect(Inner_x, Back_y-5, Button_width, Button_height)

          # Applying the text labels for the images  

          Treasure_goal_label,Treasure_goal_rect = font.render("Coin Collector", button_text_color, None)
          Treasure_goal_rect = Treasure_goal_label.get_rect(center=Treasuregoal.center)
          screen.blit(Treasure_goal_label, Treasure_goal_rect)  



          Letter_collect_label,Letter_collect_label_rect = font.render("Complete The Word", button_text_color, None)
          Letter_collect_label_rect = Letter_collect_label.get_rect(center=Lettercollect.center)
          screen.blit(Letter_collect_label, Letter_collect_label_rect)    
         
          
          Back_label,Back_label_rect = font.render("Back", button_text_color, None)
          Back_label_rect = Back_label.get_rect(center=Back.center)
          screen.blit(Back_label, Back_label_rect)  

          # Assiging the events when clicking to the buttons 

          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if Back.collidepoint(mouse_pos):
                      Click_sound.play()
                      escape_screen_active = False
                      single_player_clicked = False
                      multiplayer_clicked = False  
                      Find_treasure_clicked = False
                elif Treasuregoal.collidepoint(mouse_pos):
                     Click_sound.play() 
                     game = links("treasure",multiplayer_clicked)
                     game.run()
                elif Lettercollect.collidepoint(mouse_pos): 
                     Click_sound.play()
                     links.start_time = 0
                     links.str_start_time = " "
                     game = links("word",multiplayer_clicked)
                     game.run()


        elif About_us_clicked:
            # Draw the escape screen with new buttons

            screen.blit(SPACE, (0, 0))
            screen.blit(title_gif, ((screen_width - title_gif.get_width()) // 2, 30))

            screen.blit(border,(About_us_border_img_x-250, About_us_border_img_y-270)) 
            screen.blit(card_1,(card1_x +580, card1_y+145)) #right card half
            screen.blit(card_2,(card1_x-700, card1_y-50)) #left card up
            screen.blit(card_3,(card1_x+580, card1_y-90)) #first right
            screen.blit(card_4,(card1_x-700, card1_y+350)) #left card down
            screen.blit(card_5,(card1_x+580, card1_y+400)) #right card finall
            screen.blit(back_about_us,(0, 0)) 

            names_button=pygame.Rect(card1_x-675, card1_y-50,card_width,card_height)
            names_button_label,Back_label_rect = font.render("Abdulkareem Abunabhan", button_text_color, None)
            Back_label_rect = names_button_label.get_rect(center=names_button.center)
            screen.blit(names_button_label, Back_label_rect)
            
            names_button=pygame.Rect(card1_x-675, card1_y+350,card_width,card_height)
            names_button_label,Back_label_rect = font.render("Abdullah Shaghnoba", button_text_color, None)
            Back_label_rect = names_button_label.get_rect(center=names_button.center)
            screen.blit(names_button_label, Back_label_rect)

            names_button=pygame.Rect(card1_x+580, card1_y-90,card_width,card_height)
            names_button_label,Back_label_rect = font.render("Mustafa Mansour", button_text_color, None)
            Back_label_rect = names_button_label.get_rect(center=names_button.center)
            screen.blit(names_button_label, Back_label_rect)

            names_button=pygame.Rect(card1_x +580, card1_y+145,card_width,card_height)
            names_button_label,Back_label_rect = font.render("Jana Almomani", button_text_color, None)
            Back_label_rect = names_button_label.get_rect(center=names_button.center)
            screen.blit(names_button_label, Back_label_rect)

            names_button=pygame.Rect(card1_x+580, card1_y+400,card_width,card_height)
            names_button_label,Back_label_rect = font.render("Husam Zabian", button_text_color, None)
            Back_label_rect = names_button_label.get_rect(center=names_button.center)
            screen.blit(names_button_label, Back_label_rect)

            names_button=pygame.Rect(card1_x-933, card1_y-300 ,card_width,card_height)
            names_button_label,Back_label_rect = font.render("Back", button_text_color, None)
            Back_label_rect = names_button_label.get_rect(center=names_button.center)
            screen.blit(names_button_label, Back_label_rect)

            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              elif event.type == pygame.MOUSEBUTTONDOWN:
                  mouse_pos = pygame.mouse.get_pos()
                  if names_button.collidepoint(mouse_pos):
                      Click_sound.play()
                      escape_screen_active = False
                      single_player_clicked = False
                      multiplayer_clicked = False 
                      About_us_clicked =False


            # # Render the cards

            paragraph_text ="""          Experience an incredible and\n\n          enjoyable gaming adventure with\n\n
          Our Maze Game.Immerse yourself in\n\n
          carefully crafted mazes, intuitive\n\n    
          controls, and captivating visuals,\n\n
          as we aim to provide you with a\n\n 
          unique gaming experience.Whether\n\n  
          you're a seasoned gamer or a casual\n\n
          player, our game is designed\n\n  
          to cater to everyone. Join us on this\n\n 
          maze-filled journey, where you'll\n\n
          discover excitement,satisfaction,\n\n  
          and a profound sense of\n\n 
          accomplishment.Prepare yourself\n\n  
          for a world of thrilling challenges\n\n
          and unforgettable experiences.\n
          Good luck and happy gaming!"""

            lines = paragraph_text.split("\n") 

            line_surfaces = []
            max_width = 0
            total_height = 0
            
            for line in lines:
                line_surface,End_label_rect = font.render(line, button_text_color, None)
                # End_label_rect = line_surface.get_rect(center=About_us_border_rect.center)
             
                line_surfaces.append(line_surface)
            
                line_width = line_surface.get_width()
                line_height = line_surface.get_height()
            
                if line_width > max_width:
                    max_width = line_width
            
                total_height += line_height
            
            x = About_us_border_rect.x-300 + (About_us_border_rect.width - max_width) // 2
            y = About_us_border_rect.y-250 + (About_us_border_rect.height - total_height) // 2
                        
            for line_surface in line_surfaces:
                screen.blit(line_surface, (x, y))
                y += line_surface.get_height()
              
            # Render the cards:
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
              elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

       

        # Update the display
        pygame.display.flip()


mainloop()