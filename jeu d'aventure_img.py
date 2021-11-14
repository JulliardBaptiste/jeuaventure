"""
Programme réalisé par Julliard, Baptiste, 1G7
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((1000, 800))
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
image11=pygame.image.load("Entré clé.jpg")
image12=pygame.image.load("Salon clé.jpg")
image13=pygame.image.load("Escalier clé.jpg")
image14=pygame.image.load("Sous Sol clé.jpg")
image15=pygame.image.load("Piece clé.jpg")
image16=pygame.image.load("Salle de Bain clé.jpg")
image17=pygame.image.load("Bibliotheque clé.jpg")
image18=pygame.image.load("Chambre clé.jpg")
image19=pygame.image.load("Chambre 2 clé.jpg")
text1 = font.render("Voici l'entrée, cet endroit semble inhabité ...", True, (255, 255, 255))
text2 = font.render("Voilà le salon, il y beaucoup de poussières ...", True, (255, 255, 255))
text3 = font.render("Ici les escaliers, qu'est ce qu'il y a en bas ?", True, (255, 255, 255))
text4 = font.render("Voici le sous-sol, tout ces crânes me rendent mal à l'aise ...", True, (255, 255, 255))
text5 = font.render("Une pièce étrange, quelle est cette pièce ? Il n'y a rien dedans ...", True, (255, 255, 255))
text6 = font.render("La salle de bain, jamais je ne me laverais ici ...", True, (255, 255, 255))
text7 = font.render("Voilà une bibliothèque, il y a beaucoup de livres ici !", True, (255, 255, 255))
text8 = font.render("Voici une chambre, la décortion est très ancienne ...", True, (255, 255, 255))
text9 = font.render("J'ai la clé, je dois sortir d'ici !", True, (255, 255, 255))
text10 = font.render("Je sors du chateau, enfin !", True, (255, 255, 255))
text19 = font.render("La deuxième chambre, je trouve la clé !", True, (255, 255, 255))




dansQuellePierceEstLePersonnage=1


def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))  #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(40,680)) #afficher le texte à la prochaine actualisation
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(40,680))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(40,680))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(40,680))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(40,680))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(40,680))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(40,680))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(40,680))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text19,(40,680))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(40,680))
    elif piece==11:
        fenetre.blit(image11,(0,0))
        fenetre.blit(text9,(40,680))
    elif piece==12:
        fenetre.blit(image12,(0,0))
        fenetre.blit(text9,(40,680))
    elif piece==13:
        fenetre.blit(image13,(0,0))
        fenetre.blit(text9,(40,680))
    elif piece==14:
        fenetre.blit(image14,(0,0))
        fenetre.blit(text9,(40,680))
    elif piece==15:
        fenetre.blit(image15,(0,0))
        fenetre.blit(text9,(40,680))
    elif piece==16:
        fenetre.blit(image16,(0,0))
        fenetre.blit(text9,(40,680))
    elif piece==17:
        fenetre.blit(image17,(0,0))
        fenetre.blit(text9,(40,680))
    elif piece==18:
        fenetre.blit(image18,(0,0))
        fenetre.blit(text9,(40,680))
    elif piece==19:
        fenetre.blit(image19,(0,0))
        fenetre.blit(text9,(40,680))


def decision(direction,piece):
    print("Vous désirez allez au",direction)
    memorisePiece=piece
    #N : le personnage désire aller au nord
    if direction=='z':
        if piece==1:
            piece=2
        elif piece==5:
            piece=6
        elif piece==2:
            piece=7
        elif piece==3:
            piece=8
        elif piece==15:
            piece=16
        elif piece==12:
            piece=17
        elif piece==13:
            piece=18
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
        elif piece==16:
            piece=15
        elif piece==17:
            piece=12
        elif piece==18:
            piece=13
        elif piece==12:
            piece=11
        elif piece==11:
            piece=10
    #E : le personnage désire aller à l'est
    elif direction=='d':
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
        elif piece==16:
            piece=17
        elif piece==17:
            piece=18
        elif piece==18:
            piece=19
        elif piece==12:
            piece=13
        elif piece==13:
            piece=14
        elif piece==15:
            piece=12
    #O : le personnage désire aller à l'ouest
    elif direction=='q':
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
            piece=18
        elif piece==18:
            piece=17
        elif piece==17:
            piece=16
        elif piece==19:
            piece=18
        elif piece==13:
            piece=12
        elif piece==14:
            piece=13
        elif piece==12:
            piece=15


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
            if event.key == pygame.K_ESCAPE or event.unicode == 'e': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

