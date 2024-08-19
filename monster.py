import pygame
import random
import animation

# DEFINITION DE LA CLASSE MONSTER
class Monster(animation.AnimateSprite):
    # Charger les caractéristiques de base du monstre lorsqu'on en crée un nouveau dans le jeu
    def __init__(self, jeu) -> None:
        super().__init__("mummy")
        self.jeu = jeu
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 280)
        self.rect.y = 540
        self.speed = random.randint(1,2)
        self.start_animation()

    def damage(self, amount):
        # infliger les dégâts
        self.health -= amount
        # vérifier si son nouveau nombre de points de vie est inférieur à 0
        if self.health <= 0:
            # Réapparaître comme un nouveau monstre avec des caractéristiques différentes en x, health et en speed
            self.rect.x = 1000 + random.randint(0, 280)
            self.health = self.max_health
            self.speed = random.randint(1, 2)

            # si la barre d'événement est chargée à son maximum
            if self.jeu.comet_event.is_full_loaded():
                # retirer les monstres du jeu
                self.jeu.all_monsters.remove(self)

                # appel de la méthode pour essayer de déclencher la pluie des comètes
                self.jeu.comet_event.attempt_fall()

    # méthode qui s'occupe de l'animation
    def update_animation(self):
        self.animate(loop=True)

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