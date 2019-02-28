#Importing needed plugins
import sys, pygame
pygame.init()


class button(pygame.sprite.Sprite):
    def __init__(self, callimage):
        pygame.sprite.Sprite.__init__(self)
        self.image = callimage
        self.rect = callimage.get_rect()
    def putimage(self, display):
        display.blit(self.image,self.rect)
    def clicked (self, pos):
        return self.rect.collidepoint(pos)
        
class menu():
    def __init__(self, x1, y1, x2, y2):
        self.buttons=[]
        self.rect = pygame.Rect((x1, y1), (x2 - x1, y2 - y1))
    def addbutton(self, button):
        self.buttons.append(button)
    def placebuttons(self, display):
        for button in self.buttons:
            button.putimage(display)
    def layout(self):
        b = 0
        n = len(self.buttons)
        y1= (self.rect.top)
        h = (self.rect.h)
        for button in self.buttons:
            button.image = pygame.transform.smoothscale(button.image,(self.rect.w,int(self.rect.h/len(self.buttons))))
            button.rect = button.image.get_rect()
            button.rect.centerx = self.rect.centerx
            button.rect.centery = y1+(2*b+1)*h/(2*n)
            b+=1

class sub(pygame.sprite.Sprite):
    def __init__(self,x0,y0,s):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(25,25))
        self.origtop = self.rect.top
        self.facing = -1
        self.image = pygame.transform.smoothscale(self.image,(s,s))
        
    

def grid(x0,y0,s,nh,nv):
        lh = 0
        lv = 0

        while (lh < nh):
            pygame.draw.line(gamedisplay,white,(x0,y0+lh*s),(x0+(nv-1)*s,y0+lh*s),5)
            lh+=1
        while (lv < nv):    
            pygame.draw.line(gamedisplay,white,(x0+lv*s,y0),(x0+lv*s,y0+(nh-1)*s),5)
            lv+=1
        
        
#Defining size of screen, speed, colors needed.
size = width, height = 1280, 720
speed = [2, 2]
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)


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


sbutton = pygame.image.load("SP_Start.png")
qbutton = pygame.image.load("SP_Quit.png")
opbutton = pygame.image.load("SP_Options.png")
clock = pygame.time.Clock()
all = pygame.sprite.RenderUpdates()

#game function
def game():
    gmenu = menu(display_width * 0.85, display_height * 0.0, display_width * 1.0, display_height * 1.0)
    optionbutton = button(opbutton)
    quitbutton = button(qbutton)
    gmenu.addbutton(optionbutton)
    gmenu.addbutton(quitbutton)
    gmenu.layout()
    sub.containers = all
    x0 = 25
    y0 = 25
    s = 40
    nh = 16
    nv = 16
    Sub = sub(x0,y0,s)
    
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
                return

        screen.fill(blue)
        gmenu.placebuttons(gamedisplay)
        grid(x0,y0,s,nh,nv)
        all.clear(screen, gamedisplay)
        all.update()
        all.draw(gamedisplay)
        pygame.display.flip()
        clock.tick(60)
    
#Main function  
def main():
    #Defining start and quit button variable
    startbutton = button(sbutton)
    optionbutton = button(opbutton)
    quitbutton = button(qbutton)
    pygame.mixer.music.load("Untitled.wav")
    img = pygame.image.load("sub.png")
    sub.images = [img, pygame.transform.flip(img, 1, 0)]

    stmenu = menu(display_width * 0.3, display_height * 0.0, display_width * 0.7, display_height * 1.0)
    stmenu.addbutton(startbutton)
    stmenu.addbutton(optionbutton)
    stmenu.addbutton(quitbutton)
    stmenu.layout()
    pygame.mixer.music.play(loops=-1, start=0.0)
        
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
              print (event.pos)
              print (event.button)
              if startbutton.clicked(event.pos):
                game ()
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





