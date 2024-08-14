from player import Player
from monster import Monster
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
        # définir un groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster() # générer automatiquement un monstre au démarrage du self
        self.spawn_monster()
        
    def update(self, win_surface):
        # application de l'image de l'instance "player"
        win_surface.blit(self.player.image, self.player.rect)

        # actualiser le jauge du joueur
        self.player.update_health_bar(win_surface)

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres du self
        for monster in self.all_monsters:
            monster.forward()
            # placer le jauge de vie
            monster.update_health_bar(win_surface)

        # application de l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(win_surface)

        # application de l'ensemble des images du groupe de monstres
        self.all_monsters.draw(win_surface)

        # vérifier si le joueur souhaite aller à droite ou à gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1280:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group): # comparaison d'1 sprite à un groupe de sprite
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # renvoyer la comparaison de collision

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster) # ajouter un monstre au groupe à chaque appel de spawn_monster