import pygame
import sys
import time
import random

restart = 0

check_errors = pygame.init()

if check_errors[1] > 0:
    print("found {} an error".format(check_errors[1]))
    sys.exit(-1)
else:
    print("game is successful")

# player Surface
playsurface = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Snake game")

# colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# fps
fps_controller = pygame.time.Clock()

# imp variable

snakepos = [100, 50]
snakebody = [[100, 50], [90, 50], [80, 50]]

# food
foodspawn = True
foodpos = [random.randrange(1, 70) * 10, random.randrange(1, 39) * 10]

direction = "RIGHT"
change_to = direction

score = 0

# display the greetings
playsurface.fill(white)
pfont = pygame.font.SysFont('monoco', 90)
psurf = pfont.render('Snake Game', True, blue)
prect = psurf.get_rect()
prect.midtop = (360, 170)
playsurface.blit(psurf, prect)
pygame.display.flip()
time.sleep(3)


def gameover():
    gfont = pygame.font.SysFont("monoco", 72)
    gsurf = gfont.render("GAME OVER", True, red)
    grect = gsurf.get_rect()
    grect.midtop = (360, 25)
    playsurface.blit(gsurf, grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# show_score
def show_score(choice=1):
    sfont = pygame.font.SysFont("monoco", 26)
    # Sfont = pygame.font.SysFont("monoco",40) # This variable was unused
    ssurf = sfont.render("Score : {0}".format(score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (40, 10)
    else:
        # Re-rendering the score text here to use the same font size for consistency
        ssurf = sfont.render("Final Score: {0}".format(score), True, black)
        srect.midtop = (340, 120)

    playsurface.blit(ssurf, srect)


# main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"  # <--- FIXED: 'change_to' typo
            elif event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"
            elif event.key == pygame.K_ESCAPE:
                gameover()

    # validating the direction
    if change_to == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and not direction == "DOWN":
        direction = "UP"
    if change_to == "DOWN" and not direction == "UP":
        direction = "DOWN"

    # more on directions
    if direction == "RIGHT":
        snakepos[0] += 10
    if direction == "LEFT":
        snakepos[0] -= 10
    if direction == "UP":
        snakepos[1] -= 10
    if direction == "DOWN":
        snakepos[1] += 10

    # snake mechanism (FIXED: The tail pop logic)
    snakebody.insert(0, list(snakepos))

    # Check if snake ate food
    if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
        score += 1
        foodspawn = False  # New food needed
    else:
        snakebody.pop()  # Remove the tail to simulate movement (no growth)

    # Food Spawning (FIXED: Logic ensures foodspawn is True only after new food is placed)
    if foodspawn == False:
        # Generate new food coordinates
        foodpos = [random.randrange(1, 70) * 10, random.randrange(1, 39) * 10]
        # Ensure new food doesn't spawn on the snake's body (a common refinement)
        while foodpos in snakebody:
            foodpos = [random.randrange(1, 70) * 10, random.randrange(1, 39) * 10]
        foodspawn = True

    # drawings
    playsurface.fill(white)

    for pos in snakebody:
        pygame.draw.rect(playsurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playsurface, red,
                     pygame.Rect(foodpos[0], foodpos[1], 10, 10))  # Changed food to red for better contrast/visibility

    # Boundary checks
    if snakepos[0] >= 700 or snakepos[0] < 0:
        gameover()
    if (snakepos[1] >= 400 or snakepos[1] < 0):
        gameover()

    # Self-collision check
    for block in snakebody[1:]:
        if snakepos[0] == block[0] and snakepos[1] == block[1]:
            gameover()

    show_score()
    pygame.display.flip()
    fps_controller.tick(20)