import pygame
from player import Player
from monster import Monster

class Jeu:
    def __init__(self) -> None:
        # générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # definir un groupe de montre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster() # generer automatiquement un monstre au demarrage du jeu
        


    def check_collision(self, sprite, group): # comparaison d'1 sprite a un groupe de sprite
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # renvoyer la comparaison de collision


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster) # ajouter un monstre au groupe a chaque apel de spawn_monster