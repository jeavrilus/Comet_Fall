import pygame

# définir la classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses à faire à la création de l'entité
    def __init__(self, sprite_name) -> None:
        super().__init__()
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.current_image = 0 # commencer l'anim à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # définir une méthode pour animer le sprite
    def animate(self, loop=False):

        # vérifier si l'animation est active
        if self.animation:

            # passer à l'image suivante
            self.current_image += 1
            # vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remetttre l'animation à l'état initial
                self.current_image = 0

                # vérifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # désactivation de l'animation
                    self.animation = False

            # modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]


# définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # récupérer le chemin du dossier de ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"
    # boucler sur chaque image dans ce dossier pour les ajouter à la liste
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        # charger les images et les ajouter
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images


# définir un dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    "mummy" : load_animation_images("mummy"),
    "player" : load_animation_images("player")
}
