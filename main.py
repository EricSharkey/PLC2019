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

#Defining start and quit button variables
sbutton = pygame.image.load("SP_Start.png")

def startbutton(x1,y1):
    gameDisplay.blit(sbutton, (x1,y1))

x1 = display_width * 0.3
y1 = display_height * 0.1

qbutton = pygame.image.load("SP_Quit.png")

def quitbutton(x3,y3):
    gameDisplay.blit(qbutton, (x3,y3))

x3 = display_width * 0.3
y3 = display_height * 0.7

opbutton = pygame.image.load("SP_Options.png")

def optionsbutton(x2,y2):
    gameDisplay.blit(opbutton, (x2,y2))

x2 = display_width * 0.3
y2 = display_height * 0.4

def button(msg,x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

<<<<<<< HEAD
#Main function
=======
#Main function 
>>>>>>> 45d904fa9257f6ac79774c18db962318ecd16ba5
def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
<<<<<<< HEAD
        screen.fill(black)
        screen.blit(background, backgroundrect)
        startbutton(x1,y1)
        quitbutton(x,y)
        pygame.display.flip()
        clock.tick(60)
    
if __name__== '__main__':
    main()
=======
            if event.type == pygame.MOUSEBUTTONDOWN:
              print (event.pos)
              print (event.button)
              if opbutton.get_rect(topleft=(x2,y2)).collidepoint(event.pos):
                print ("Options")
              if opbutton.get_rect(topleft=(x3,y3)).collidepoint(event.pos):
                print ("Quit?")
                pygame.quit()
                return

        
        screen.fill(black)
        screen.blit(background, backgroundrect)
        startbutton(x1,y1)
        quitbutton(x3,y3)
        optionsbutton(x2,y2)
        pygame.display.flip()
        clock.tick(60)
if __name__ == '__main__':
    main()
    


>>>>>>> 45d904fa9257f6ac79774c18db962318ecd16ba5


