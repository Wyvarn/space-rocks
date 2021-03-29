import pygame

class SpaceRocks:
    """
    Defines our game
    """

    def __init__(self):
        self._init_game()
        self.screen = pygame.display.set_mode((800, 600))
    
    def _init_game(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")
    
    def start_game(self):
        """
        This will start the game.
        Each iteration of this loop(game loop) will generate a single frame of the game.
        Performs:

        1. input handling. Inputs is gathered & handled here, button presses, mouse movements
        2. game engine. Game mechanics/logic/engine. Rules of physics are applied, collisions are detected and handled, AI does its thing, etc.
        This part is also responsible for checking if the player has won or lost the game.
        3. drawing. If the game hasn’t ended yet, then this is where the frame will be drawn on screen. 
        It will include all the items that are currently in the game and are visible to the player.
        """
        while True:
            self._handle_input()
            self._game_engine()
            self._draw()

    def _handle_input(self):
        pass

    def _game_engine(self):
        pass

    def _draw(self):
        self.screen.fill((0,0, 255))
        pygame.display.flip()
