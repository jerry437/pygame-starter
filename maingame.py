import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
background = pygame.image.load('assets/background2.png').convert()
img = pygame.image.load('assets/hero/sliced/idle-2.png')
img = pygame.transform.scale(img, (50, 50))
background = pygame.transform.scale(background, (800, 600))
player = {
    "img" = pygame.image.load('assets/hero/sliced/idle-2.png')
    "x" = 200
    "y" = 200
    "hp" = 100
    "run" = True

}
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if img > 400:
        hp -= 1


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
       player["x"]-= 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player["x"] += 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player["y"] += 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player["y"] -= 1
    # DRAWS THE IMAGE,TEXT
        win.fill((0, 0, 0))
        win.blit(background,(0,0))
        win.blit(player["img"], (player["x"],player ["y"]))
        win.blit(player["hp"](0,3))

    pygame.display.update()

pygame.quit()
