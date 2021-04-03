import random

from pygame import Color
from pygame.math import Vector2
from pygame.mixer import Sound


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


def get_random_position(surface):
    """
    This will generate a random set of coordinates on a given surface and return the result as a Vector2 instance.
    """
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )


def get_random_velocity(min_speed, max_speed):
    """
    The method will generate a random value between min_speed and max_speed and a random angle between 0 and 360 degrees
    Then it will create a vector with that value, rotated by that angle.
    """
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)


def print_text(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, False, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)
