import pygame
import random

# DEFINITION DE LA CLASSE COMET (Cette fameuse boule de feu céleste)
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event) -> None:
        super().__init__()
        # définir l'image associé à cette comète
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.speed = random.randint(1, 3)
        self.rect.x = random.randint(20, 700)
        self.rect.y = - random.randint(0, 700)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # vérifier si le nombre de comètes est de 0
        if len(self.comet_event.all_comets) == 0:
            # réinitialiser la barre d'événement
            self.comet_event.reset_percent()
            # faire réapparaître les monstres
            self.comet_event.jeu.start()
        
    def fall(self):
        self.rect.y += self.speed

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            self.remove()

            # si il n'y a plus de comètes
            if len(self.comet_event.all_comets) == 0:
                # réinitialiser la barre d'événement
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # vérifier si la comète rentre en collision avec le joueur
        if self.comet_event.jeu.check_collision(self, self.comet_event.jeu.all_players):
            # retirer la comète du jeu
            self.remove()
            # faire subir des dégats au joueur
            self.comet_event.jeu.player.damage(20)