# TODO: move to utils module
import random
from pygame.image import load
from pygame.math import Vector2


def load_sprite(name: str, with_alpha: bool = True):
    """
    Loads a sprite given the name. This will build a path to the sprite and load it

    """
    # You can find a better way for the extension for the asset to be added
    # this uses .png assets
    path = f"assets/sprites/{name}.png"

    # returns a Surface (https://www.pygame.org/docs/ref/surface.html)
    # that can be used to represent images which can be used to
    # draw on the screen
    loaded_sprite = load(path)

    # converts the image to either be transparent or not.
    # Generally, you could just use convert_alpha() for all types of images since it can also handle an image without
    # transparent pixels.
    # However, drawing transparent images is a bit slower than drawing nontransparent ones.
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


def wrap_position(position: tuple, surface):
    """
    An important element of this game is making sure that game objects don’t leave the screen.
    You can either have them bounce back off the edge or make them reappear on the opposite edge of the screen.
    In this game though we implement the latter.

    This function allows us to implement the latter.
    """
    x, y = position
    w, h = surface.get_size()
    # using the modulo operation makes sure that the position never leaves the area of the given surface.
    # In this game, that surface will be the screen.
    return Vector2(x % w, y % h)


def get_random_velocity(min_speed, max_speed):
    """
    The method will generate a random value between min_speed and max_speed and a random angle between 0 and 360 degrees
    Then it will create a vector with that value, rotated by that angle.
    """
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)
