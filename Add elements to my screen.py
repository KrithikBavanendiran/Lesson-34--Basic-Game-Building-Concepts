import pygame

pygame.init()

width, height = 500, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blue Rectangle Example")

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 36)
text = font.render("This is a blue rectangle", True, WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, BLUE, (150, 100, 200, 100))

    screen.blit(text, (125, 50))
    pygame.display.flip()

pygame.quit()



