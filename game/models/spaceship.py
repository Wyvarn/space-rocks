from pygame import Vector2
from . import GameObject
from ..utils.asset_utils import load_sprite


class Spaceship(GameObject):
    """
    Represents a spaceship
    """

    def __init__(self, position: tuple):
        super().__init__(position, load_sprite("spaceship"), Vector2(0))
