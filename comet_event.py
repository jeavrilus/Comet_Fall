import pygame
from comet import Comet

# CREER UNE CLASSE POUR GERER CET EVENEMENT
class CommetFallEvent:

    # créer un compteur au chargement
    def __init__(self, jeu) -> None:
        self.percent = 0
        self.percent_speed = 5
        self.jeu = jeu 
        self.fall_mode = False

        # définir un groupe de sprite pour stocker les comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
    
    def comet_fall(self):
        # Faire apparaître entre 1 et 10  comètes
        for i in range(1, 10):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # quand la barre est totalement remplie
        if self.is_full_loaded() and len(self.jeu.all_monsters) == 0:
            self.comet_fall()
            self.fall_mode = True # activer l'événement
        
    def update_bar(self, surface): # créer une barre d'événement au bas de l'écran

        # ajouter du pourcentage à la barre
        self.add_percent()

        # barre noir (arrière plan de la barre d'événement)
        pygame.draw.rect(surface, (0, 0, 0),[
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            surface.get_width(), # longueur de la fenetre
            10 # épaisseur de la barre
        ])
        # barre rouge (barre d'événement qui va s'actualiser)
        pygame.draw.rect(surface, (187, 11, 11),[
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            (surface.get_width() / 100) * self.percent, # longueur de la fenetre
            10 # épaisseur de la barre
        ])
        