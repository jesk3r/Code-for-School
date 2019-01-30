import pygame as pg
import settings
import levels
from players import*
import time 
import atexit
import sys
import platforms



def main():
    """ Main Program """

    pg.mixer.init()
    pg.mixer.music.load("Gateway Galaxy.mp3")
    pg.mixer.music.play()
    
    
    pg.init()

    # Set the height and width of the screen
    screen_size = [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT]
    screen = pg.display.set_mode(screen_size)

    pg.display.set_caption("CivX")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []

    
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))
    level_list.append(levels.Level_04(player))

    # Set the current level
    current_level_number = 0
    current_level = level_list[current_level_number]

    active_sprite_list = pg.sprite.Group()
    player.level = current_level

    player.rect.x = 500
    player.rect.y = 500
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pg.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pg.event.get(): # User did something
            if event.type == pg.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    player.go_left()
                if event.key == pg.K_RIGHT:
                    player.go_right()
                if event.key == pg.K_UP:
                    player.jump()
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                    

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pg.K_RIGHT and player.change_x > 0:
                    player.stop()

 
            
        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_number < len(level_list)-1:
                current_level_number += 1
                current_level = level_list[current_level_number]
                player.level = current_level


        if current_level_number == 3:
            exit_handler()
            pg.quit()
            sys.exit()


        death_floor = pg.Rect( 0,600,800,1)


        if death_floor.colliderect(player.rect):
            exit_handle()
            main()
            
            
            

            
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        clock.tick(60)

        pg.display.flip()

    pg.quit()



def exit_handler():
    print("YOU WIN")
    time.sleep(3)
    pg.quit()
    sys.exit()

    

def exit_handle():
    print("You Died")
    time.sleep(1)
    print("Respawn in 5...")
    time.sleep(1)
    print("Respawn in 4...")
    time.sleep(1)
    print("Respawn in 3...")
    time.sleep(1)
    print("Respawn in 2...")
    time.sleep(1)
    print("Respawn in 1...")
    time.sleep(1)


    

    
atexit.register(exit_handler)

if __name__ == "__main__":
    main()

   
