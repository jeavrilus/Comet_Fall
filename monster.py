import pygame
import random


# DEFINITION DE LA CLASSE MONSTER
class Monster(pygame.sprite.Sprite):
    # Charger les caracteristiques de base du monstre lorsqu'on en cree un nouveau ds le jeu
    def __init__(self, jeu) -> None:
        super().__init__()
        self.jeu = jeu
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 280)
        self.rect.y = 540
        self.speed = random.randint(1,2)

    def damage(self, amount):
        # infliger les degats
        self.health -= amount
        # verifier si son nouveau nombre de points de vie est inferieur a 0
        if self.health <= 0:
            # Reapparaitre comme un nouveau montre avec des caracteristiques differentes en x, health et en speed
            self.rect.x = 1000 + random.randint(0, 280)
            self.health = self.max_health
            self.speed = random.randint(1, 2)

            # si la barre d'événement est chargée à son maximum
            if self.jeu.comet_event.is_full_loaded():
                # retirer les monstres du jeu
                self.jeu.all_monsters.remove(self)

                # appel de la méthode pour essayer de déclencher la pluie des comètes
                self.jeu.comet_event.attempt_fall()

    # Créer une jauge de vie
    def update_health_bar(self, surface):
        # dessiner la jauge
        pygame.draw.rect(surface,(60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        
    def forward(self):
        # le déplacement ne se fera que s'il n'y a pas de collision avec un "groupe de joueur"
         if not self.jeu.check_collision(self, self.jeu.all_players):
            self.rect.x -= self.speed
        # vérifier si le joueur est en collision avec le monstre
         else:
            #  infliger des dégats au joueur
            self.jeu.player.damage(self.attack)