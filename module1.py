#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      T.nsi08
#
# Created:     29/01/2021
# Copyright:   (c) T.nsi08 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
pygame.init()

# Générer la fenetre
pygame.display.set_caption("Paint 3.0")
window =  pygame.display.set_mode((992,680))

running = True
    # Initialing RGB Color
color = (26,82,118)
ORANGE = (225,143,16)
BLUE = (28,40,51)
window.fill(color)
pygame.display.update()



class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def redrawWindow():
    window.fill(color)
    start.draw(window, (0,0,0))

run = True
start = button(ORANGE,300,200,100,100,'start')

#LE LOGO
logo = pygame.image.load("donut.png").convert_alpha()
logo = pygame.transform.scale(logo,(150,150))
window.blit(logo, (25, 465)) # paint to screen

#LE TITRE
police = pygame.font.SysFont("Arial", 46)
image_texte = police.render("Paint 3.0", 1,(255,255,255))
window.blit(image_texte,(10, 620))


###LE BOUTON START
pygame.draw.rect(window,ORANGE,(20,20,150,75)) # On dessine un rectangle
zone_clic1 = pygame.Rect((20,20),(150,75)) #On définit la zone de clic
start_button = pygame.Surface(zone_clic1.size)
start_button.fill(ORANGE)
##
##
###LE BOUTON STOP
##pygame.draw.rect(window,ORANGE,(20,120,150,75)) # On dessine un rectangle
##zone_clic2 = pygame.Rect((20,120),(150,75)) #On définit la zone de clic
##stop_button = pygame.Surface(zone_clic2.size)
##stop_button.fill(ORANGE)





# Boucle tant que la condition est vrai
while running:
    redrawWindow()

    #Si le joueur ferme cette fenetre
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        # Que l'événement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

##        if event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
##            if event.button == 1: # 1= clique gauche
##                if zone_clic1.collidepoint(event.pos):
##                    print("Start")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start.isOver(pos):
                    print("Start")

        if event.type == pygame.MOUSEMOTION: # quand je relache le bouton
            if start.isOver(pos): # 1= clique gauche
                start.color(255,0,0)
            start.color(0,255,0)

    pygame.display.flip()

