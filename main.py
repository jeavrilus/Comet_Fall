# Importer les bibliothèques nécessaires
import pygame
import math
from jeu import Jeu


# INITIALISER PYGAME
pygame.init()

# GENERER LA FENETRE DU JEU (Parametres)
# dimension
win_surface = pygame.display.set_mode((1280, 720))
# titre
pygame.display.set_caption("Comet Fall")

# CADENCE DE RAFRAICHISSEMENT ou CLOCK
clock = pygame.time.Clock()
FPS = 100

# CHARGEMENT DE L'IMAGE DE L'ARRIERRE PLAN
background_image = pygame.image.load("assets/bg.jpg")

# CHARGEMENT DE LA BANNIERE
banner_image = pygame.image.load("assets/banner.png")
banner_image = pygame.transform.scale(banner_image, (500, 500))
banner_rect = banner_image.get_rect()
banner_rect.x = math.ceil(win_surface.get_width() / 4)

# CHARGEMENT DU BOUTON DE LANCEMENT
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(win_surface.get_width() / 3.33)
play_button_rect.y = math.ceil(win_surface.get_height() / 2)


# CHARGERGEMENT DU JEU
jeu = Jeu()

running = True
# BOUCLE PRINCIPALE DU JEU (Tant que le jeu est actif)
while running:
    # application de la fenêtre du jeu et de son arrière plan
    win_surface.blit(background_image, (0, -200))

    # vérifier si le jeu a commence ou non
    if jeu.is_playing:
        # déclencher les instructions de la partie
        jeu.update(win_surface)
    else:
        # Ajouter mon écran de Bienvenue
        win_surface.blit(play_button, play_button_rect)
        win_surface.blit(banner_image, banner_rect)
        

    # mettre à jour la fenêtre (update/flip)
    pygame.display.flip()

    # On boucle sur les évenements
    for event in pygame.event.get():
        # si le type de l'événement est fermeture de fenêtre (X)
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # détecter si une touche du clavier est pressée
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True

            # détecter si la touche "space" est pressée pr lancer un projectile
            if event.key == pygame.K_SPACE:
                if jeu.is_playing:
                    jeu.player.launch_projectile()
                else:
                    # mettre le jeu en mode "lancé"
                    jeu.start()  
                    # jouer le son
                    jeu.sound_manager.play("click")


        # détecter si cette touche du clavier est relachée
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérifier si le bouton de la souris est en collision avec le bouton play (play_button)
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                jeu.start()  
                # jouer le son
                jeu.sound_manager.play("click")

    # fixer le nombre de fps
    clock.tick(FPS)