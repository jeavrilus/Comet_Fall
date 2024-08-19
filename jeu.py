from player import Player
from monster import Mummy
from monster import Alien
from comet_event import CommetFallEvent
import pygame


# DEFINITION DE LA CLASSE JEU
class Jeu:
    def __init__(self) -> None:
        # définir si le jeu a commencé ou non
        self.is_playing = False
        # générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # générer l'événement
        self.comet_event = CommetFallEvent(self)
        # définir un groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        # générer automatiquement les monstres au démarrage
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy) 
        self.spawn_monster(Alien)
        
    def game_over(self):
        # remettre le jeu à son état initial i.e (retirer les comètes, retirer les monstres, remettre le joueur a 100 points de vie, mettre le jeu en attente)
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self, win_surface):
        # application de l'image de l'instance "player"
        win_surface.blit(self.player.image, self.player.rect)

        # actualiser la jauge du joueur
        self.player.update_health_bar(win_surface)
        
        # actualiser l'animation du joueur
        self.player.update_animation()

        # actualiser la barre d'événement du jeu
        self.comet_event.update_bar(win_surface)

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            # placer la jauge de vie
            monster.update_health_bar(win_surface)
            monster.update_animation()

        # récupérer les comètes du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # application de l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(win_surface)

        # application de l'ensemble des images du groupe de monstres
        self.all_monsters.draw(win_surface)

        # application de l'ensemble des images du groupe comète
        self.comet_event.all_comets.draw(win_surface)

        # vérifier si le joueur souhaite aller à droite ou à gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1280:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group): # comparaison d'1 sprite à un groupe de sprite
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # renvoyer la comparaison de collision

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))