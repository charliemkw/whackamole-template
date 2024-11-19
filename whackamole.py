import pygame
import random

screen = pygame.display.set_mode((640, 512))
mole_image = pygame.image.load("mole.png")

def draw_grid(screen):
    # Creating grid:
    for i in range(1, 21):
        pygame.draw.line(screen, "dark blue", ((32 * i), 0), ((32 * i), 512))
    for i in range(0, 17):
        pygame.draw.line(screen, "dark blue", (0, (32 * i)), (640, (32 * i)))

def draw_mole(x, y):
    # screen.blit(mole_image, (x * 32, y * 32))
    screen.blit(mole_image, mole_image.get_rect(topleft=(x * 32, y * 32)))

def main():
    try:
        pygame.init()
        x, y = 0,0
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_x, click_y = event.pos
                        if (click_x // 32) == x and (click_y // 32) == y:
                            x = random.randrange(0,19)
                            y = random.randrange(0, 15)

            screen.fill("#d3f1ff")
            draw_grid(screen)
            draw_mole(x, y)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
