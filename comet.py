import pygame
import random

# DEFINITION DE LA CLASSE COMET (Cette fameuse boule de feu céleste)
class Comet(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        # définir l'image associé à cette comète
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.speed = random.randint(1, 3)
        self.rect.x = random.randint(20, 700)
        self.rect.y = - random.randint(0, 700)
        
    def fall(self):
        self.rect.y += self.speed