from pygame.math import Vector2


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
