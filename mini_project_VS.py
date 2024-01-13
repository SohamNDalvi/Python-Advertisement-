import pygame
import time


pygame.init()


pygame.mixer.init()


# Load music file
pygame.mixer.music.load("song.mp3")


# Start playing the music
pygame.mixer.music.play()


# Set up the screen
screen_width = 1000
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((173, 216, 230))


   
#create rectangle for grass
pygame.draw.rect(screen,(0,255,0),pygame.Rect(0,510,1000,550))
#flag code
img_flag = pygame.image.load("flag.png")
screen.blit(img_flag,(0,200))
pygame.display.flip()


# Load the running man images
running_man_images = []
for i in range(1, 7):
    img = pygame.image.load(f"runningMan_{i}.png")
    running_man_images.append(img)


#load the falling man
running_man_images1 = []
for i in range(1,12):
    img1 = pygame.image.load(f"manStand_{i}.png")
    running_man_images1.append(img1)




# Set up the running man animation
animation_frame = 0
animation_speed = 50
animation_counter = 0
running_man_rect = running_man_images[0].get_rect()
running_man_rect.x = screen_width - running_man_rect.width
running_man_rect.y = screen_height - running_man_rect.height


# Set up the falling man animation
running_man_rect1 = running_man_images[0].get_rect()
running_man_rect1.x = screen_width //2
running_man_rect1.y = screen_height - running_man_rect.height


#set up for running man2 animation
animation_frame2 = 0
animation_speed2 = 30
animation_counter2 = 0
running_man_rect2 = running_man_images[0].get_rect()
running_man_rect2.x = (screen_width//2)- running_man_rect.width
running_man_rect2.y = screen_height - running_man_rect.height


# Game loop
running=True
running1=True
running2=True
imgValue=True


#def pop_up for popup window
def pop_up():
    pygame.display.set_caption('Energy Drink')
    img_box = pygame.image.load("DAS.png")
    imgrect=img_box.get_rect()
    imgrect.center=((screen_width//2),(screen_height//2))
    screen.blit(img_box,imgrect)
    pygame.display.flip()
    pygame.display.update()


   
   


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()




    # Update animation
    if running ==True:
        animation_counter += 1
        if animation_counter >= animation_speed:
            animation_frame = (animation_frame + 1) % len(running_man_images)
            running_man_rect.x -= 6
            animation_counter = 0


        # Draw the screen
        screen.fill((173, 216, 230))
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(0,510,1000,550))
        img_flag = pygame.image.load("flag.png")
        screen.blit(img_flag,(0,200))
        screen.blit(running_man_images[animation_frame], running_man_rect)
        pygame.display.flip()
   
   
    # Check if running man has reached the center
    if running_man_rect.x <= screen_width // 2:
        #code for falling man
        running = False  
        if running1==True:
            for i in range(11):
                time.sleep(0.4)
                # Set up the running man animation
                animation_frame1 = i
               
                # Draw the screen
                screen.fill((173, 216, 230))
                pygame.draw.rect(screen,(0,255,0),pygame.Rect(0,510,1000,550))
                img_flag = pygame.image.load("flag.png")
                screen.blit(img_flag,(0,200))
                screen.blit(running_man_images1[animation_frame1], running_man_rect1)
                pygame.display.flip()
               
               
            if animation_frame1 == 10:
                running1 = False
               
           
    #code for again running man2
    if running1 == False:


        if running2 == True:
            animation_counter2 += 1
            if animation_counter2 >= animation_speed2:
                animation_frame2 = (animation_frame2 + 1) % len(running_man_images)
                running_man_rect2.x -= 6
                animation_counter2 = 0


            # Draw the screen
            screen.fill((173, 216, 230))
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(0,510,1000,550))
            img_flag = pygame.image.load("flag.png")
            screen.blit(img_flag,(0,200))
            screen.blit(running_man_images[animation_frame2], running_man_rect2)
            running = False
            running1 = False
            pygame.display.flip()    
               
    if running_man_rect2.x<=1:
        running = False
        running1 = False
        running2=False
        pop_up()
