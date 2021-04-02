from pygame.math import Vector2
from pygame.transform import rotozoom
from . import GameObject
from ..utils.asset_utils import load_sprite

# Pygame’s y-axis goes from top to bottom, so a negative value actually points upwards
UP = Vector2(0, -1)


class Spaceship(GameObject):
    """
    Represents a spaceship

    In this game, when you press Up, the spaceship’s speed will increase. When you release the key, the spaceship will
    maintain its current speed but should no longer accelerate. So in order to slow it down, you’ll have to turn the
    spaceship around and press Up again.

    MANEUVERABILITY: determines how fast your spaceship can rotate. This value represents an angle in degrees by which
    your spaceship’s direction can rotate each frame. Using a larger number will rotate the spaceship faster, while a
    smaller number will allow more granular control over the rotation.
    ACCELERATION: constant number describing how fast the spaceship can speed up each frame.
    BULLET_SPEED
    """
    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    BULLET_SPEED = 3

    def __init__(self, position: tuple):
        # Make a copy of the original UP vector
        self.direction = Vector2(UP)
        super().__init__(position, load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        """
        Changes the direction by rotating it either clockwise or counterclockwise. The rotate_ip() method of the Vector2
        class rotates it in place by a given angle in degrees. The length of the vector doesn’t change during this
        operation. You can learn a bit more about the advanced math behind 2D vector rotation from here:
        https://www.youtube.com/watch?v=OYuoPTRVzxY
        """
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        """
        Overrides the draw method of a Game Object

        Note that rotozoom() returns a new surface with a rotated image. However, in order to keep all the contents of
        the original sprite, the new image might have a different size. In that case, Pygame will add some additional,
        transparent background.

        The size of the new image can be significantly different than that of the original image. That’s why draw()
        recalculates the blit position of rotated_surface. Remember that blit() starts in the upper-left corner, so to
        center the rotated image, you also need to move the blit position by half the size of the image.
        """
        # uses the angle_to() method of the Vector2 class to calculate the angle by which one vector needs to be rotated
        # in order to point in the same direction as the other vector. This makes it painless to translate the
        # spaceship’s direction into the rotation angle in degrees.
        angle = self.direction.angle_to(UP)

        # rotates the sprite using rotozoom(). It takes the original image, the angle by which it should be rotated,
        # and the scale that should be applied to the sprite. In this case, you don’t want to change the size,
        # so you keep the scale as 1.0.
        rotated_surface = rotozoom(self.sprite, angle, 1.0)

        # recalculate the blit position, using the size of rotated_surface. The process is described below.
        rotated_surface_size = Vector2(rotated_surface.get_size())

        # contains the rotated_surface_size * 0.5 operation. That’s another thing you can do with vectors in Pygame.
        # When you multiply a vector by a number, all its coordinates are multiplied by that number.
        # As a result, multiplying by 0.5 will return a vector with half the length of the original.
        blit_position = self.position - rotated_surface_size * 0.5

        # uses the newly calculated blit position to put the image on the screen.
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        """
        You can calculate the change in velocity by multiplying the direction vector by the ACCELERATION value and
        adding the result to the current velocity. This happens only when the engine is on—that is, when the player
        presses Up. The new position of the spaceship is calculated by adding the current velocity to the current
        position of the spaceship. This happens each frame, regardless of the engine status.
        """
        self.velocity += self.direction * self.ACCELERATION
