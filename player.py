import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, jeu) -> None:
        super().__init__()
        self.jeu = jeu
        self.image = pygame.image.load("assets/player.png") # chargement de l'img. souhaité
        self.rect = self.image.get_rect() # récupération des coordonnées de l'img souhaité pr pouvoir la déplacer
        self.rect.x = 400
        self.rect.y = 500
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 4
        self.all_projectiles = pygame.sprite.Group()
         

    def launch_projectile(self):
        # creer une nouvelle instance de la classe Projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def move_right(self):
        # si le joueur n'entre pas en collision avec un monstre
        if not self.jeu.check_collision(self, self.jeu.all_monsters): # self represente "player" et self.jeu.all_monsters represente "le groupe de monstre"
            self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed