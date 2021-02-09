from pygame.math import Vector3, Vector2


class Bille():
    def __init__(self):
            self.size = 10
            self.couleur = Vector3()
            self.position = Vector2()
            self.direction = Vector2()

    def mourir(self):
        pass