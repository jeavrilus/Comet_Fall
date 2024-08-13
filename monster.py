import pygame

class Monster(pygame.sprite.Sprite):
    # Charger les caracteristiques de base du monstre lorsqu'on en cree un nouveau ds le jeu
    def __init__(self, jeu) -> None:
        super().__init__()
        self.jeu = jeu
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.speed = 1

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

    # Creer un jauge de vie
    def update_health_bar(self, surface):
        # definir une couleur pour le jauge (vert clair)
        bar_color = (111, 210, 46)
        # definir une couleur d'arriere plan pour le jauge (gris fonce)
        back_bar_color = (60, 63, 60)
        # definir la position, la largeur et l'epaisseur du jauge
        bar_position= [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        # definir la position de l'arriere plan du jauge
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        # dessiner le jauge
        pygame.draw.rect(surface,back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        



    def forward(self):
        # le deplacement ne se fera que s'il n'y a pas de collision avec un "groupe de joueur"
         if not self.jeu.check_collision(self, self.jeu.all_players):
            self.rect.x -= self.speed