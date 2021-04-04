from pygame.transform import rotozoom
from . import GameObject
from .utils import load_sprite, get_random_velocity


class Asteroid(GameObject):
    """
    Represents an Asteroid

    Note that the setting of a random position is in one place &  setting of random velocity is in another(here).
    That’s because the position should be random only for the six asteroids you start with, so it’s being set where the
    game is initialized. However, the velocity is random for every asteroid, so you set it in the constructor here.
    """

    def __init__(self, position, create_asteroid, size=3):
        """
        :param position: Position of the Asteroid
        :param create_asteroid: Callback to create an asteroid when this asteroid is split up. it should be split up
        into smaller asteroids based on the scale of the new size
        :param size Initial size of the asteroid, starts at 3. When it is split by a bullet to 2, then 1, then it is
        destroyed
        This will assign a size to an asteroid, using the default value 3, which represents a big asteroid.
        It will also scale the original sprite by using rotozoom(). This method is used for scaling if the angle is 0
        and the scale is anything other than 0. the size_to_scale lookup table contains scales for different sizes
        """
        self.size = size
        self.create_asteroid = create_asteroid
        size_to_scale = {
            3: 1,
            2: 0.5,
            1: 0.25,
        }
        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite("asteroid"), 0, scale)

        # Notice the get_random_velocity uses the minimum value of 1,this is because the asteroid should always move
        # at least a bit.
        super().__init__(position, sprite, get_random_velocity(1, 3))

    def split(self):
        """
        Splits an Asteroid into smaller asteroids when hit by a bullet.
        This will create two new asteroids at the same position as the current one. Each of them will have a slightly
        smaller size. This logic will happen only if the current asteroid is a medium or large one.
        """
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(self.position, self.create_asteroid, self.size - 1)
                self.create_asteroid(asteroid)
