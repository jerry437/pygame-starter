import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
img = pygame.image.load('background_18.png').convert()
img = pygame.transform.scale(img, (800, 600))
# Create the font

font = pygame.font.SysFont("arial", 50)

# Create the text object
text = font.render("welcome press start", True, (255, 255, 255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(img, (0, 0))
    win.blit(text, (200, 200))


    pygame.display.update()

pygame.quit()