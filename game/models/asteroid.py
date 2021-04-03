from . import GameObject
from .utils import load_sprite, get_random_velocity


class Asteroid(GameObject):
    """
    Represents an Asteroid

    Note that the setting of a random position is in one place &  setting of random velocity is in another(here).
    That’s because the position should be random only for the six asteroids you start with, so it’s being set where the
    game is initialized. However, the velocity is random for every asteroid, so you set it in the constructor here.
    """

    def __init__(self, position):
        # Notice the get_random_velocity uses the minimum value of 1,this is because the asteroid should always move
        # at least a bit.
        super().__init__(position, load_sprite("asteroid"), get_random_velocity(1, 3))
