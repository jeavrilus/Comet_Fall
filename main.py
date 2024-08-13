# Importer les bibliothèques nécessaires
import pygame
from jeu import Jeu

# INITIALISER PYGAME
pygame.init()

# GENERER LA FENETRE DU JEU (Parametres)
# dimension
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
win_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# titre
pygame.display.set_caption("Comet Fall")

# CADENCE DE RAFRAICHISSEMENT
FPS = 60

# CHARGEMENT DE L'IMAGE DE L'ARRIERRE PLAN
background_image = pygame.image.load("assets/bg.jpg")


# CHARGERGEMENT DU JEU
jeu = Jeu()

running = True
# BOUCLE PRINCIPALE DU JEU (Tant que le jeu est actif)
while running:
    # application de la fenêtre du jeu et de son arriere plan
    win_surface.blit(background_image, (0, -200))

    # application de l'image de l'instance "player"
    win_surface.blit(jeu.player.image, jeu.player.rect)

    # recuperer les projectiles du joueur
    for projectile in jeu.player.all_projectiles:
        projectile.move()

    # recuperer les monstres du jeu
    for monster in jeu.all_monsters:
        monster.forward()
        # placer le jauge de vie
        monster.update_health_bar(win_surface)

    # application de l'ensemble des images du groupe de projectiles
    jeu.player.all_projectiles.draw(win_surface)

    # application de l'ensemble des images du groupe de monstres
    jeu.all_monsters.draw(win_surface)

    # vérifier si le joueur souhaite aller à droite ou à gauche
    if jeu.pressed.get(pygame.K_RIGHT) and jeu.player.rect.x + jeu.player.rect.width < WINDOW_WIDTH:
        jeu.player.move_right()
    elif jeu.pressed.get(pygame.K_LEFT) and jeu.player.rect.x > 0:
        jeu.player.move_left()

    # print(jeu.player.rect.x)

    # mettre à jour la fenêtre (update/flip)
    pygame.display.flip()

    # On boucle sur les évenements
    for event in pygame.event.get():
        # si le type de l'évenement est fermeture de fenêtre (X)
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # détecter si une touche du clavier est pressée
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True

            # détecter si la touche "space" est pressée pr lancer un projectile
            if event.key == pygame.K_SPACE:
                jeu.player.launch_projectile()

        # détecter si cette touche du clavier est relachée
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False