#Importing needed plugins
import sys, pygame
pygame.init()

#Defining size of screen, speed, colors needed.
size = width, height = 1280, 720
speed = [2, 2]
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)


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
        self.images[0] = pygame.transform.smoothscale(self.images[0],(s,s))
        self.images[1] = pygame.transform.smoothscale(self.images[1],(s,s))
        self.images[2] = pygame.transform.smoothscale(self.images[2],(s,s))
        self.images[3] = pygame.transform.smoothscale(self.images[3],(s,s))
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(x0,y0))
        self.origtop = self.rect.top
        self.facing = -1
    def move(self,x,y):
        self.rect.topleft = (x,y)

class grid():
    x0 = 25
    y0 = 25
    s = 40
    nh = 16
    nv = 16
    

    def __init__(self,x0,y0,s,nh,nv):
        self.x0 = x0
        self.y0 = y0
        self.s = s
        self.nh = nh
        self.nv = nv

    def Hdraw(self,xy,r,):
        pos = self.squarepos(xy)
        posbox = pos[0]-self.s*(r-1),pos[1]-self.s*(r-1)
        sizebox = r*self.s*2-1*self.s,r*self.s*2-1*self.s
        pygame.draw.rect(gamedisplay,red,pygame.Rect(posbox,sizebox))
        print (posbox,sizebox,xy)
        
    def draw(self):
        lh = 0
        lv = 0
        Xp = 0
        Yp = 0
        while (lh <= self.nh):
            pygame.draw.line(gamedisplay,white,(self.x0,self.y0+lh*self.s),(self.x0+(self.nv)*self.s,self.y0+lh*self.s),5)
            lh+=1
        while (lv <= self.nv):
            pygame.draw.line(gamedisplay,white,(self.x0+lv*self.s,self.y0),(self.x0+lv*self.s,self.y0+(self.nh)*self.s),5)
            lv+=1
            
    def gridcheck(self,x,y):
        if x>=(self.x0) and x<(self.x0+self.s*self.nh) and y>=(self.y0) and y<(self.y0+self.s*self.nv):
            return 1
            return 0
    
    def squarenumber(self,x,y):
        return int ((x - self.x0) / self.s), int ((y - self.y0) / self.s)

    def squarenumbertuple(self,xy):
        return int ((xy[0] - self.x0) / self.s), int ((xy[1] - self.y0) / self.s)

    def squarepos(self,xy):
        return xy[0]*self.s+self.x0,xy[1]*self.s+self.y0

#     _______________
#C = V(x1-x)+(y1-y)
        

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
torpedo = pygame.image.load("Torpedo.png")
radar = pygame.image.load("Radar.png")
move = pygame.image.load("Move.png")
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
    amenu = menu(display_width * 0.65, display_height * 0.0, display_width * 0.80, display_height * 1.0)
    Tbutton = button(torpedo)
    Rbutton = button(radar)
    Mbutton = button(move)
    amenu.addbutton(Tbutton)
    amenu.addbutton(Rbutton)
    amenu.addbutton(Mbutton)
    amenu.layout()
    sub.containers = all
    Sub = sub(25,25,40)
    Grid = grid(25,25,40,16,16)
    
    while 1:
        screen.fill(blue)
        all.clear(screen, gamedisplay)
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
              if Mbutton.clicked(event.pos):
                  Grid.Hdraw(Grid.squarenumbertuple(Sub.rect.topleft), 3)
              x=(event.pos[0])
              y=(event.pos[1])
              if Grid.gridcheck(x,y):
                  sn = Grid.squarenumber(x,y)
                  squarepos = Grid.squarepos(sn)
                  Sub.move(squarepos[0],squarepos[1])
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                Sub.image = Sub.images[0]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                Sub.image = Sub.images[1]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                Sub.image = Sub.images[2]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                Sub.image = Sub.images[3]                
#pos - 25 / s convert to intger * s

#     _______________
#C = V(x1-x)+(y1-y)                

        gmenu.placebuttons(gamedisplay)
        amenu.placebuttons(gamedisplay)
        all.update()
        all.draw(gamedisplay)
        Grid.draw()        
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
    sub.images = [img, pygame.transform.flip(img, 1, 0),pygame.transform.rotate(img, 90), pygame.transform.rotate(img,270)]

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





