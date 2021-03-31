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
        """
        Handles the game logic
        """
        pass

    def _draw(self):
        """
        Draws the content on the screen. It is called on every frame to draw the content on the screen.
        self.screen.fill takes a tuple with three values, representing three base colors: red, green, and blue. 
        Each color value ranges between 0 and 255, representing its intensity.
        therefore a tuple of (0, 0, 255) means that the color will consist only of blue, with no traces of red or green

        pygame.display.flip() updates the content of the screen. Because the game will eventually display moving objects, 
        this method is called on every frame to update the display. Because of this, the screen needs to be filled with color every frame, 
        as the method will clear the contents generated during the previous frame.
        """
        self.screen.fill((0,0, 255))
        pygame.display.flip()
