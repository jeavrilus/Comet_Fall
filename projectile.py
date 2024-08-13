import pygame


# DEFINITION DE LA CLASSE PROJECTILE
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player) -> None:
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) # redimensionnement de l'image (nom de l'img, (dimension de l'img))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.player = player
        # creation de 2 nouveaux attributs permettant de donner un effet de rotation aux projectiles
        self.origin_image = self.image # 1 garde l'image originelle sans la rotation (tres important)
        self.angle = 0 # 2 permettant de faire tourner sur lui-meme le projectile


    def rotate(self):
        # faire tourner le projectile
        self.angle += 3 # ajouter de 15 degres a l'angle
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1) # reaffection de l'image mais cette fois-ci en lui passant l'image avec la rotation
        self.rect = self.image.get_rect(center=self.rect.center) # pour permettre une rotation plus fluide par rapport au centre de l'image

    def remove(self):
        self.player.all_projectiles.remove(self) # recuperation depuis le joueur, le groupe de sprite et on supprime uniquement le sprite qui sort de l'ecran


    def move(self):
        self.rect.x += self.speed
        self.rotate()

        #  verifier si le projectile rentre en collision avec un monstre
        for monster in self.player.jeu.check_collision(self, self.player.jeu.all_monsters):
            # si oui supprimer le projectile
            self.remove()
            # infliger des degats aux monstres
            monster.damage(self.player.attack)

        # verifier si le projectile n'est plus present sur l'ecran
        if self.rect.x > 1280:
            # si oui, supprimer celui-ci (en dehors de l'ecran)
            self.remove()