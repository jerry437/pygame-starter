import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
background = pygame.image.load('assets/background2.png').convert()
img = pygame.image.load('assets/hero/sliced/idle-2.png')
img = pygame.transform.scale(img, (50, 50))
background = pygame.transform.scale(background, (800, 600))
x = 200
y = 200

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

  #keys = pygame.key.get_pressed()
  #if keys[pygame.K_LEFT]:
   # x -= 1

    win.fill((0, 0, 0))
    win.blit(background,(0,0))
    win.blit(img, (x, y))
  

    pygame.display.update()

pygame.quit()