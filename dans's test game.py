# import needed modules
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
###BG = pygame.transform.scale(pygame.image.load("background_image.jpeg"), (WIDTH, HEIGHT))
BG = pygame.image.load("background_image.jpg")

# set game font
FONT = pygame.font.SysFont("timesnewroman", 30)

# player dimensions
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# player movement velocity
PLAYER_VEL = 12

# asteroid movement velocity
ASTEROID_VEL = 10

# set gravity values
FALL_VEL = 0
GRAVITY = 0.7

# load player frames and asteroid image
PLAYER_FRAMES = [pygame.image.load('player_frame1.png'), pygame.image.load('player_frame2.png')]
ASTEROID_IMAGE = pygame.image.load('asteroid.png')

# draw function
def draw(player, elapsed_time, asteroids, player_frame_index):

    # draw the background image
    WIN.blit(BG, (0, 0))

    # prints elapsed game time on screen
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
    WIN.blit(time_text, (10, 10))

    # draw the player with current frame
    player_image = pygame.transform.scale(PLAYER_FRAMES[player_frame_index], (PLAYER_WIDTH, PLAYER_HEIGHT))
    WIN.blit(player_image, (player.x, player.y))

    # draw asteroids with current frame
    for asteroid in asteroids:
        steroid_image = pygame.transform.scale(ASTEROID_IMAGE, (asteroid.width, asteroid.height))
        WIN.blit(asteroid_image, (asteroid.x, asteroid.y))

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

    # starting asteroid generation speed
    asteroid_add_increment = 2000
    asteroid_count = 0

    asteroids = []
    hit = False

    # initialize the frame indices
    player_frame_index = 0

    # brings in global variable
    global FALL_VEL
     
    # call draw function
    draw(player, elapsed_time, asteroids, player_frame_index)

    # main game loop
    while run:

        # update the frame indices for animations
        player_frame_index = (player_frame_index + 1) % len(PLAYER_FRAMES)

        # asteroid dimensions, currently random within range
        ASTEROID_WIDTH = random.randint(20, 100)
        ASTEROID_HEIGHT = ASTEROID_WIDTH

        # locks game clock at 60fps, locks asteroid_count to time
        asteroid_count += clock.tick(60)

        # sets the game timer to 0:00
        elapsed_time = time.time() - start_time

        # generates asteroids randomly
        if asteroid_count > asteroid_add_increment:
            for _ in range(random.randint(1, 10)):
                # randomly places asteroid on x axis
                asteroid_x = random.randint(0, WIDTH - ASTEROID_WIDTH)
                # spawns asteroid above screen
                asteroid = pygame.Rect(asteroid_x, -ASTEROID_HEIGHT, ASTEROID_WIDTH, ASTEROID_HEIGHT)
                asteroids.append(asteroid)

            # controls how fast asteroids spawns
            # gets faster over time, sets max speed, sets increment speed
            asteroid_add_increment = max(200, asteroid_add_increment - 50)
            asteroid_count = 0

        # if player presses red "x", game window will close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # create gravity, act on player
        FALL_VEL += GRAVITY
        player.y += FALL_VEL

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
        # when press "space", go up
        if keys[pygame.K_SPACE]:
            # flap strength
            FALL_VEL = -8.5

        # move asteroids downward
        for asteroid in asteroids[:]:
            asteroid.y += ASTEROID_VEL
            # asteroids below screen get deleted
            if asteroid.y > HEIGHT:
                asteroids.remove(asteroid)
            # asteroid gets deleted if it hits player
            elif asteroid.colliderect(player):
                asteroids.remove(asteroid)
                hit = True
                break

        # if player hit, tell them they lose
        if hit:
            loser_text = FONT.render("You Lose Bitch!", 3, (255, 255, 255))
            # centers text
            WIN.blit(loser_text, (WIDTH/2 - loser_text.get_width()/2, HEIGHT/2 - loser_text.get_height()/2))
            # updates screen
            pygame.display.update()
            # pause for effect
            pygame.time.delay(3000)
            # reloop the game
            main()

        # call draw function
        draw(player, elapsed_time, asteroids, player_frame_index)

    # close game
    pygame.quit()


# run the file directly, starts main function
if __name__ == "__main__":
    main()
