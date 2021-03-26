# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *

pygame.init()

class Menu:

        #Ouverture de la fenêtre Pygame
        fenetre = pygame.display.set_mode((1600, 900), RESIZABLE)

        #Nommer la page
        pygame.display.set_caption("Menu jeu")

        #Chargement et collage du fond
        fond = pygame.image.load("Textures/menu/ciel.png").convert()
        fenetre.blit(fond, (0,0))

        #Chargement et collage du bouton_1
        Bouton_1 = pygame.image.load("Textures/menu/bouton.png").convert_alpha()
        Bouton_1_pos = (540, 250)
        fenetre.blit(Bouton_1, Bouton_1_pos)

        #Chargement et collage du bouton_2
        Bouton_2 = pygame.image.load("Textures/menu/bouton.png").convert_alpha()
        Bouton_2_pos = (540,450)
        fenetre.blit(Bouton_2, Bouton_2_pos)

        #Chargement et collage du bouton_3
        Bouton_3 = pygame.image.load("Textures/menu/bouton.png").convert_alpha()
        Bouton_3_pos = (540,650)
        fenetre.blit(Bouton_3, Bouton_3_pos)

        #Chargement et collage du text_1
        Text_1_pos = (740, 310)
        font = pygame.font.Font(None, 70)
        Text_1 = font.render("PLAY",1,(10,10,10))
        fenetre.blit (Text_1, Text_1_pos)

        #Chargement et collage du text_2
        Text_2_pos = (700, 510)
        font = pygame.font.Font(None, 70)
        Text_2 = font.render("OPTION",1,(10,10,10))
        fenetre.blit (Text_2, Text_2_pos)

        #Chargement et collage du text_3
        Text_3_pos = (740, 710)
        font = pygame.font.Font(None, 70)
        Text_3 = font.render("QUIT",1,(10,10,10))
        fenetre.blit (Text_3, Text_3_pos)


continuer = 1


while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT:
            continuer = 0


    #Rafraichissement
    pygame.display.flip()