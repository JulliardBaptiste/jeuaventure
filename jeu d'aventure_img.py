"""
Programme réalisé par Julliard, Baptiste, 1G7
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
image1=pygame.image.load("Entré.jpg")
image2=pygame.image.load("Salon.jpg")
image3=pygame.image.load("Escalier.jpg")
image4=pygame.image.load("Sous Sol.jpg")
image5=pygame.image.load("Piece.jpg")
image6=pygame.image.load("Salle de Bain.jpg")
image7=pygame.image.load("Bibliotheque.jpg")
image8=pygame.image.load("Chambre.jpg")
image9=pygame.image.load("Chambre 2.jpg")
image10=pygame.image.load("Sortie.jpg")
text1 = font.render("Voici l'entré, cet endroit semble inhabité ...", True, (255, 255, 255))
text2 = font.render("Voilà le salon, il y beaucoup de poussières ...", True, (255, 255, 255))
text3 = font.render("Ici les escaliers, qu'est ce qu'il y a en bas ?", True, (255, 255, 255))
text4 = font.render("Voici le sous-sol, tout ces crânes me rendent mal à l'aise ...", True, (255, 255, 255))
text5 = font.render("Une pièce étrange, quelle est cette pièce ? Il n'y a rien dedans ...", True, (255, 255, 255))
text6 = font.render("La salle de bain, jamais je ne me laverais ici ...", True, (255, 255, 255))
text7 = font.render("Voilà une bibliothèque, il y a beaucoup de livres ici !", True, (255, 255, 255))
text8 = font.render("Voici une chambre, la décortion est très ancienne ...", True, (255, 255, 255))
text9 = font.render("La deuxième chambre, on se croirait dans un film d'horreur ...", True, (255, 255, 255))
text10 = font.render("Voici le chateau, on dirait un décor de film !", True, (255, 255, 255))



dansQuellePierceEstLePersonnage=1


def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))  #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(70,850)) #afficher le texte à la prochaine actualisation
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(70,850))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(70,850))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(70,850))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(70,850))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(70,850))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(70,850))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(70,850))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(70,850))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(70,850))



def decision(direction,piece):
    print("Vous désirez allez au",direction)
    memorisePiece=piece
    #N : le personnage désire aller au nord
    if direction=='n':
        if piece==1:
            piece=2
        elif piece==5:
            piece=6
        elif piece==2:
            piece=7
        elif piece==3:
            piece=8
        elif piece==10:
            piece=1
    #S : le personnage désire aller au sud
    elif direction=='s':
        if piece==2:
            piece=1
        elif piece==6:
            piece=5
        elif piece==7:
            piece=2
        elif piece==8:
            piece=3
        elif piece==1:
            piece=10
    #E : le personnage désire aller à l'est
    elif direction=='e':
        if piece==2:
            piece=3
        elif piece==3:
            piece=4
        elif piece==5:
            piece=2
        elif piece==6:
            piece=7
        elif piece==7:
            piece=8
        elif piece==8:
            piece=9
    #O : le personnage désire aller à l'ouest
    elif direction=='o':
        if piece==3:
            piece=2
        elif piece==4:
            piece=3
        elif piece==2:
            piece=5
        elif piece==7:
            piece=6
        elif piece==8:
            piece=7
        elif piece==9:
            piece=8
    if memorisePiece==piece:
        print("Déplacement impossible")
    else:
        print("C'est possible")
    return piece



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

