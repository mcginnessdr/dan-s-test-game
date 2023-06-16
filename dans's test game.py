# import needed addons
import pygame
import time
import random

# initalize the font module
pygame.font.init()

# create game window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# title of the game window
pygame.display.set_caption("Dan's Test Game")

# set the background image
# if image is not correct size, use this code to fit image to screen:
# BG = pygame.transform.scale(pygame.image.load("background_image.jpeg"), (WIDTH, HEIGHT))
BG = pygame.image.load("background_image.jpg")

# set game font
FONT = pygame.font.SysFont("timesnewroman", 30)

# player dimensions
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# player movement velocity
PLAYER_VEL = 10

# !need player gravity!


# draw function
def draw(player, elapsed_time):

    # draw the background image
    WIN.blit(BG, (0, 0))

    # prints elapsed game time on screen
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # draw the player
    pygame.draw.rect(WIN, "red", player)

    # update the game screen
    pygame.display.update()




# main function
def main():
    run = True

    # creates game clock
    clock = pygame.time.Clock()

    # saves the start time of the game
    start_time = time.time()
    elapsed_time = 0

    # create player
    player = pygame.Rect(500, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)


    # main game loop
    while run:

        #locks game clock at 60fps
        clock.tick(60)

        # sets the game timer to 0:00
        elapsed_time = time.time() - start_time

        # if player presses red "x", game window will close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # player movement controls
        keys = pygame.key.get_pressed()
        # when press "a", go left
        # blocks player from going off screen to left
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        # when press "d", go right
        # blocks player from going off screen to right
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        # when press"space", go up
        # !need make flap function!
        if keys[pygame.K_SPACE]:
            player.y -= PLAYER_VEL
        

        # call draw function
        draw(player, elapsed_time)

    # close game
    pygame.quit()


# run the file directly, starts main function
if __name__ == "__main__":
    main()

