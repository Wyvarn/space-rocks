from . import GameObject

from .utils import load_sprite


class Bullet(GameObject):
    """
    Represents a Bullet
    """

    def __init__(self, position, velocity):
        super().__init__(position, load_sprite("bullet"), velocity)
