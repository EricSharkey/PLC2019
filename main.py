#Importing needed plugins
import sys, pygame
pygame.init()

#Defining size of screen, speed, colors needed.
size = width, height = 1280, 720
speed = [2, 2]
black = (0,0,0)
white = (255,255,255)

#Setting size of screen,
screen = pygame.display.set_mode(size)

#Setting background image
background = pygame.image.load("BG_Underwater720.png")
backgroundrect = background.get_rect()

display_width = 1280
display_height = 720

#Adding text to the top left of the outer window
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Submarine Game Test, Version 1.0')


clock = pygame.time.Clock()
crashed = False

#Defining start and quit button variables
sbutton = pygame.image.load("SP_Start.png")

def startbutton(x1,y1):
    gameDisplay.blit(sbutton, (x1,y1))

x1 = display_width * 0.3
y1 = display_height * 0.4

qbutton = pygame.image.load("SP_Quit.png")

def quitbutton(x,y):
    gameDisplay.blit(qbutton, (x,y))

x = display_width * 0.3
y = display_height * 0.7

def button(msg,x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

#Main function 
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
    screen.fill(black)
    screen.blit(background, backgroundrect)
    startbutton(x1,y1)
    quitbutton(x,y)
    pygame.display.flip()
   




