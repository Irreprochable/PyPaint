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
pygame.Surface.blit(window,img_txt,(30,600))


le_start = pygame.Rect(20,20,150,75)
pygame.draw.rect(window,black,le_start)
start = pygame.image.load('Staart.png').convert()
pygame.Surface.blit(window, start, (20,20))


le_stop = pygame.Rect(20,115,150,75)
pygame.draw.rect(window,black,le_stop)
stop = pygame.image.load('Stoop.png').convert()
pygame.Surface.blit(window, stop, (20,115))

le_triangle = pygame.Rect(392,500,50,50)
pygame.draw.rect(window,black,le_triangle)
triangle = pygame.image.load('Triangle.png').convert()
pygame.Surface.blit(window, triangle, (392,500))

le_carre = pygame.Rect(592,500,50,50)
pygame.draw.rect(window,black,le_carre)
carre = pygame.image.load('Carré.png').convert()
pygame.Surface.blit(window, carre, (592,500))

le_rond = pygame.Rect(792,500,50,50)
pygame.draw.rect(window,black,le_rond)
rond = pygame.image.load('Rond.png').convert()
pygame.Surface.blit(window, rond, (792,500))



lerectancle = pygame.Rect(190, 100, 200, 200)
pygame.draw.rect(window, black,lerectancle )


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

                #test si la zone de clique correspond à la bonne reponse
            if lerectancle.collidepoint(zx, zy):
               print("ok")

            if le_start.collidepoint(zx, zy):
               print("start")

            if le_stop.collidepoint(zx, zy):
               print("stop")

            if le_triangle.collidepoint(zx, zy):
               print("triangle")

            if le_carre.collidepoint(zx, zy):
               print("carre")

            if le_rond.collidepoint(zx, zy):
               print("rond")


    pygame.display.flip()

pygame.quit()
