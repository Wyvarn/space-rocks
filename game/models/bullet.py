from . import GameObject


class Bullet(GameObject):
    """
    Represents a Bullet
    """

    def __init__(self, position, sprite, velocity):
        super().__init__(position, sprite, velocity)

    def move(self, surface):
        self.position = self.position + self.velocity
