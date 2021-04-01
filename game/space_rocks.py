import pygame
from utils.asset_utils import load_sprite

class SpaceRocks:
    """
    Defines our game
    """

    def __init__(self):
        self._init_game()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
    
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
        # in each event loop in the game, we get the current event and perform actions based on the event.
        # pygame.event.get() allows us to get events in each frame of the game.
        # These can be used to process any type of event. In this case we exit the game if the user process the
        # ESC button on their keyboard or they exit by closing the game, the X button in the window or pressing
        # ALT + F4 on Windows or Linux or Cmd+W on MacOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()

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
        # use this if you want to fill the background with a color
        # self.screen.fill((0,0, 255))
        
        # this takes in the surface to draw on & the x,y coordinates to draw on
        # In Pygame, the coordinate system starts in the top-left corner. 
        # The x-axis goes from left to right, and the y-axis goes from top to bottom
        #     -------------> x
        #     ________________________
        #  | |                        |
        #  | |                        |
        #  | |                        |
        #  | |                        |
        #  Y |                        |
        #    |________________________|
        #
        # The UP vector, pointing upwards, will have a negative y-coordinate.
        # The coordinates passed to blit() are given as two values: X and Y. 
        # 
        # They represent the point where the top-left corner of the surface will be located after the operation
        #     ________________________
        #    |         | Big Surface  |
        #    |         |              |
        #    |         | Y            |
        #    | ----> X  ______        |
        #    |         |      |       | 
        #    |         |      |       | 
        #    |         |______|       | 
        #    |        Small surface   |
        #    |________________________|
        # 
        # The top-left corner is moved by the blit coordinates to calculate the correct position.
        # In this case, the new background has the same size as the screen (800 × 600 pixels), 
        # so the coordinates will be (0, 0), representing the top-left corner of the screen. 
        # That way, the background image will cover the entire screen.
        
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()