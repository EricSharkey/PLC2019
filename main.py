import sys, pygame
pygame.init()

size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

background = pygame.image.load("BG_Underwater.png")
backgroundrect = background.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



    screen.fill(black)
    screen.blit(background, backgroundrect)
    pygame.display.flip()
