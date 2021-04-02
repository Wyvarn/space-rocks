from pygame.math import Vector2

from game.utils.game_utils import wrap_position


class GameObject:
    """
    This represents a typical object in the game & will encapsulate all generic
    behaviour of all objects. Other classes will inherit this & extend its behaviour

    This uses Vectors, which are similar to tuples. In a 2D world, vectors are represented by two values indicating x-
    and y-coordinates.
    These coordinates can point to a position, but they can also represent motion or acceleration in a given direction. 
    Vectors can be added, subtracted, or even multiplied to quickly update the position of a sprite. 
    Reference on this can be found here https://www.intmath.com/vectors/3-vectors-2-dimensions.php

    """

    def __init__(self, position: tuple, sprite, velocity):
        """
        Initializes a game object
        :param position: A point in the center of object on the 2D scree
        :type position tuple
        :param sprite: an image used to display the object
        :param velocity: a value used for movement
        :type velocity tuple or Vector
        radius A value representing the collision zone around the object’s position
        """
        self.position = Vector2(position)
        self.sprite = sprite
        self.velocity = Vector2(velocity)
        self.radius = sprite.get_width() / 2

    def draw(self, surface):
        """
        draw the object’s sprite on the surface passed as an argument.
        """
        # calculates the correct position for blitting the image. 
        # Notice that the Vector2() constructor receives a single number instead of a tuple. 
        # In that case, it will use that number for both values. So Vector2(self.radius) i
        # s the equivalent of Vector2((self.radius, self.radius))
        blit_position = self.position - Vector2(self.radius)

        # uses the newly calculated blit position to put the object’s sprite in a correct place on the given surface.
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        """
        Updates the position of the object

        """
        # adds the velocity to the position and gets an updated position vector as a result. 
        # Pygame makes manipulating vectors straightforward, allowing you to add them like numbers
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other) -> bool:
        """
        This is used to detect collisions with other objects
        :param other: Other game object
        :returns: Returns True if the distance between this object & another is smaller than the sum
        of the radiuses
        """
        # calculates the distance between two objects 
        distance = self.position.distance_to(other.position)

        # checks if that distance is smaller than the sum of the objects’ radiuses. If so, the objects collide.
        return distance < self.radius + other.radius
