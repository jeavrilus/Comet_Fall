import pygame

# CREER UNE CLASSE POUR GERER CET EVENEMENT
class CommetFallEvent:

    # créer un compteur au chargement
    def __init__(self) -> None:
        self.percent = 0
        self.percent_speed = 5

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
    
    def attempt_fall(self):
        # qd la jauge est totalement chargé ou remplie
        if self.is_full_loaded():
            print(" Pluie de comètes")
            self.reset_percent()
        

    def update_bar(self, surface): # créer un jauge au bas de l'écran

        # ajouter du pourcentage à la barre
        self.add_percent()

        # barre noir (arrière plan du jauge d'événement)
        pygame.draw.rect(surface, (0, 0, 0),[
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            surface.get_width(), # longueur de la fenetre
            10 # épaisseur de la barre
        ])
        # barre rouge (jauge d'événement qui va s'actualiser)
        pygame.draw.rect(surface, (187, 11, 11),[
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            (surface.get_width() / 100) * self.percent, # longueur de la fenetre
            10 # épaisseur de la barre
        ])
        # appel de la méthode pour essayer de déclencher la pluie
        self.attempt_fall()