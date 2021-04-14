import pygame

#INITIALISATION DE LA FENËTRE
pygame.init()
window = pygame.display.set_mode((992,680))
gray = (216,219,223)
black = (18,18,19)
white = (255,255,255)
window.fill(gray)
pygame.display.set_caption("Paint")
image = pygame.image.load("donut1.png").convert_alpha()
pygame.display.set_icon(image)
#--------------------------------------------


#Titre
font = pygame.font.SysFont("Carlito Bold", 54)
img_txt = font.render("Paint 3.0",True,black)
pygame.Surface.blit(window,img_txt,(35,600))


boutton_start = pygame.Rect(20,20,150,75)
pygame.draw.rect(window,black,boutton_start)
logo_start = pygame.image.load('Start.png').convert()
pygame.Surface.blit(window, logo_start, (20,20))


boutton_stop = pygame.Rect(20,115,150,75)
pygame.draw.rect(window,black,boutton_stop)
logo_stop = pygame.image.load('Stop.png').convert()
pygame.Surface.blit(window, logo_stop, (20,115))

boutton_triangle = pygame.Rect(392,520,50,50)
pygame.draw.rect(window,black,boutton_triangle)
logo_triangle = pygame.image.load('Triangle.png').convert()
pygame.Surface.blit(window, logo_triangle, (392,520))

boutton_carre = pygame.Rect(592,520,50,50)
pygame.draw.rect(window,black,boutton_carre)
logo_carre = pygame.image.load('Carré.png').convert()
pygame.Surface.blit(window, logo_carre, (592,520))

boutton_rond = pygame.Rect(792,520,50,50)
pygame.draw.rect(window,black,boutton_rond)
logo_rond = pygame.image.load('Rond.png').convert()
pygame.Surface.blit(window, logo_rond, (792,520))


lerectancle = pygame.image.load('rectancle.png').convert()
pygame.Surface.blit(window,lerectancle,(272,20))

boutton_color = pygame.Rect(30,400,178,178)
pygame.draw.rect(window,gray,boutton_color)
color = pygame.image.load('COLOR.png').convert_alpha()

dessin_carre = pygame.Surface(50,50)

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            coordinates = pygame.mouse.get_pos()

# mouse_position is in the form [x,y], we only want the x part
            zx = coordinates[0]
            zy = coordinates[1]

#test si la zone de clique correspond à la bonne réponse

            if boutton_start.collidepoint(zx, zy):
               print("start")

            if boutton_stop.collidepoint(zx, zy):
               print("stop")

            if boutton_triangle.collidepoint(zx, zy):

                pygame.Surface.blit(window, color, (30, 400))



            if boutton_carre.collidepoint(zx, zy):

                pygame.Surface.blit(window, color, (30, 400))
                pygame.draw.rect(lerectancle,black,dessin_carre,(100,100))


            if boutton_rond.collidepoint(zx, zy):

                pygame.Surface.blit(window, color, (30, 400))


            if boutton_color.collidepoint(zx, zy):

                pygame.draw.rect(window,gray,boutton_color)


    pygame.display.flip()

pygame.quit()
