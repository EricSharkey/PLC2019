#Importing needed plugins
import sys, pygame
pygame.init()


class button(pygame.sprite.Sprite):
    def __init__(self, callimage, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = callimage
        self.rect = callimage.get_rect(topleft=(x, y))
    def putimage(self, display):
        display.blit(self.image,self.rect)
    def clicked (self, pos):
        return self.rect.collidepoint(pos)
        
class main():
    def __init__(self, display):
        self.buttons=[]
        self.rect =[]
    def addbutton(self, button):
        self.buttons.append(button)
    def placebuttons(self, display):
        for button in self.buttons:
            button.putimage(display)
    def call(self):
        for button in self.button:
            buttona.rect = button.image.get_rect(center=(


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
gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Submarine Game Test, Version 1.0')


clock = pygame.time.Clock()

#Defining start and quit button variables
sbutton = pygame.image.load("SP_Start.png")


x1 = display_width * 0.3
y1 = display_height * 0.1

qbutton = pygame.image.load("SP_Quit.png")


x3 = display_width * 0.3
y3 = display_height * 0.7

opbutton = pygame.image.load("SP_Options.png")


x2 = display_width * 0.3
y2 = display_height * 0.4


startbutton = button(sbutton, x1, y1)
optionbutton = button(opbutton, x2, y2)
quitbutton = button(qbutton, x3, y3)

pygame.mixer.music.load("Untitled.wav")

#Main function 
def main():
    stmenu = menu()
    stmenu.addbutton(startbutton)
    stmenu.addbutton(optionbutton)
    stmenu.addbutton(quitbutton)

pygame.mixer.music.play(loops=-1 start=0.0)
        
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
              print (event.pos)
              print (event.button)
              if optionbutton.clicked(event.pos):
                print ("Options")
              if quitbutton.clicked(event.pos):
                print ("Quit?")
                pygame.quit()
                return

        
        screen.fill(black)
        screen.blit(background, backgroundrect)
        stmenu.placebuttons(gamedisplay)
        pygame.display.flip()
        clock.tick(60)
if __name__ == '__main__':
    main()





