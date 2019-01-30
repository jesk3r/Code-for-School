import pygame
import random
import time
from main import*


#This is where I put in some colours and their RGB code and where I set the screen size
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK =(255, 0, 159)
LIGHTBLUE = (51, 216, 252)
screen_width = 800
screen_height = 640
screen = pygame.display.set_mode([screen_width, screen_height])

# Where I displayed the messege to the player when  he/she crashes
def text_objects(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, textRect = text_objects("SHIP CRASHED!", largeText)
    textRect.center = ((screen_width/2),(screen_height/2))
    screen.blit(TextSurf, textRect)

    pygame.display.update()

    time.sleep(2)

    game()
    
#Class for the asteroid 
class Block(pygame.sprite.Sprite):
    
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

    def update(self):
        
        self.rect.y += 5
 
 #Pilot class or Player
class Pilot(pygame.sprite.Sprite):
    def __init__(self):
       
        # This calls on the parent class
        super().__init__()
 
        self.image = pygame.image.load("Main player Ship (1).png") #This loads my sprite art and fills
        #my pilot sprite

 
        self.rect = self.image.get_rect() #Since python sees  all objects  in rectangle/square form
        #I need to use this code
 
    def update(self):
        #Updates the pilot's possition
        
        
        pos = pygame.mouse.get_pos()
 
        #Since i wanted the ship to start at the horizontal plane of the screen  I set it to be at the
        # X axis possition of the mouse, which I find is more simple than assigning WASD
        # Or arrow keys to each individual movement
        self.rect.x = pos[0]
 
#This is the laser class 
class Laser(pygame.sprite.Sprite):
   
    def __init__(self):
        # 
        super().__init__()
        #code that is responsible for making the lazer sprite since it was simple
        # I did not need to use any external graphics or software for it
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(PINK) #Assigns the colour of the laser
 
        self.rect = self.image.get_rect()
 
    def update(self):
        #Moves the 3 spaces up the y axis vertically cause the asteroids will be coming down from
        #From the same axis
        self.rect.y -= 3
 
def game():
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("halo-ost-brothers-in-arms-extended-drum.mp3")
    pygame.mixer.music.play()
    
    # Forms the window the game will be in basically starts the game and keeps it running
     
    # Initialize Pygame
    pygame.init()
     
    # Set the height and width of the screen
    screen_width = 800
    screen_height = 640
    screen = pygame.display.set_mode([screen_width, screen_height])
     
    #My Sprite List
     
    #The list of all sprites that I can easily call opon
    all_sprites_list = pygame.sprite.Group()
     
    #Asteroid list
    asteroid_list = pygame.sprite.Group()
     
    #Laser list
    laser_list = pygame.sprite.Group()
    
    #Pilot list
    pilot_list = pygame.sprite.Group()
     
    # Creates the different asteroids type in game and all of their different speeds
    # and colours, and their location, the harder the set the higher they will be on
    #Y axis snd therefore come after the easier one.
     
    for i in range(300):
        # This represents a asteroid
        asteroid = Block(BLUE)
     
        # Set a random location for the asteroid
        asteroid.rect.x = random.randrange(screen_width)
        asteroid.rect.y = random.randrange(-3000,-20)
     
        # Add the asteroid to the list of objects
        asteroid_list.add(asteroid)
        all_sprites_list.add(asteroid)
        
    for i in range(500):
        # The second set of more challenging asteroids
        asteroid = Block(RED)
     
        # They are then again randomly set
        asteroid.rect.x = random.randrange(screen_width)
        asteroid.rect.y = random.randrange(-5000,-3000)
        asteroid_list.add(asteroid)
        all_sprites_list.add(asteroid)

    for i in range(700):
        # The second set of more challenging asteroids
        asteroid = Block(WHITE)
     
        # They are then again randomly set
        asteroid.rect.x = random.randrange(screen_width)
        asteroid.rect.y = random.randrange(-7000,-6000)
        asteroid_list.add(asteroid)
        all_sprites_list.add(asteroid)

    for i in range(800):
        # The second set of more challenging asteroids
        asteroid = Block(LIGHTBLUE )
     
        # They are then again randomly set
        asteroid.rect.x = random.randrange(screen_width)
        asteroid.rect.y = random.randrange(-9000,-8000)
        asteroid_list.add(asteroid)
        all_sprites_list.add(asteroid)



 


    
    


    
    
        

    
        
     
        # Add the asteroid to the list of objects
    asteroid_list.add(asteroid)
    all_sprites_list.add(asteroid)
    #Add Pilo to sprite list
    pilot = Pilot()
    pilot_list.add(pilot)
    all_sprites_list.add(pilot)
     
    # Game stays on till user closes window
    done = False
     
    #Refreshes the update speed of the screen
    clock = pygame.time.Clock()
     
    score = 0
    score + 1
    
    

    pilot.rect.y = 560
     
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pg.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pg.quit()
                        sys.exit()
     
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                laser = Laser()
                # This is where I set the lazer to be set at the x value of the pilot or player
                laser.rect.x = random.randrange(pilot.rect.x,pilot.rect.x + 76)
                laser.rect.y = pilot.rect.y
                # Add the laser to the lists
                all_sprites_list.add(laser)
                laser_list.add(laser)
     
        # --- Game logic
     
        # Call the update() method on all the sprites
        all_sprites_list.update()
     
        # Calculate mechanics for each laser
        for laser in laser_list:
     
            # See if it hit a asteroid
            asteroid_hit_list = pygame.sprite.spritecollide(laser, asteroid_list, True)
     
            # Each time an asteroid comes into contact with the lazer it is then removed from the list
            for asteroid in asteroid_hit_list:
                laser_list.remove(laser)
                all_sprites_list.remove(laser)
                score += 1
                print(score)
     
            # Removes lazer from the sprite list
            if laser.rect.y < 10:
                laser_list.remove(laser)
                all_sprites_list.remove(laser)
                
        for pilot in pilot_list:
     
            # See if it hit a asteroid
            pilot_hit_list = pygame.sprite.spritecollide(pilot, asteroid_list, True)
     
            # For each asteroid hit, remove the laser and add to the score
            for pilot in pilot_hit_list:
                laser_list.remove(pilot)
                all_sprites_list.remove(pilot)
                exit_handle()
                game()

                
                
            #If the first set of asteroids surpass the screed width (y) they are removed from the list
            
                    
                
                
        # --- Draw a frame
     
        #Sets the backround to my external graphics as a png
        bg = pygame.image.load("Backround.png.png")
        screen.blit(bg, (0,0))
        # Draw all the spites
        all_sprites_list.draw(screen)
     
        
        pygame.display.flip()
     
        
        clock.tick(60)

pygame.quit()
