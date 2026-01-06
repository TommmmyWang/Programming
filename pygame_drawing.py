# Your Title Here
# Author:
# Date:

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Your Title Here")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        # draw a red rectangle in the middle of the secreen
        # pygame.draw.rect(screen, RED, (WIDTH / 2, HEIGHT / 2, 100, 40))
        # draw a blue circle on top of the red rectangle
        # pygame.draw.circle(screen, BLUE, (WIDTH / 2, HEIGHT / 2 - 100, 100))

        # pygame.draw.line(screen, GREEN, (WIDTH / 2 + 20, 20), (WIDTH - 20, HEIGHT / 2 - 20))
        i = 2
        colour = RED
        for i in range(7):
            if i == 1:
                colour = RED
            elif i == 2:
                colour = BLUE
            elif i == 3:
                colour = GREEN
            elif i == 4:
                colour = YELLOW
            elif i == 5:
                colour = PURPLE
            pygame.draw.rect(screen, colour, (200, 100, (480 - i * 80), (480 - i * 80)))
            i += 1

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
